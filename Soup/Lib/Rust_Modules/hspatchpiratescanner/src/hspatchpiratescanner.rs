use std::error::Error;
use std::fs::File;
use std::io::{BufReader, Write};
use std::time::{Duration, UNIX_EPOCH};
use serde::{Deserialize, Serialize};
use serde_json::Value;
use reqwest::header::{HeaderMap, HeaderValue, AUTHORIZATION};
use reqwest::Client;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use chrono::{DateTime, Utc};
use colored::*;
use std::process;

#[derive(Serialize, Deserialize, Debug)]
struct InputFileJSONFields {
    target: String,
    API_token: Option<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct Commit {
    repo: String,
    message: String,
    url: String,
    date: String,
    sha: String,
    email: String,
}

// Reads the input data given by the user from the input_file
fn read_input_file() -> Result<InputFileJSONFields, Box<dyn Error>> {
    // location of patch_pirate.py: Hackesoup/Soup/Tools
    let input_file = File::open("../Soup/Lib/Data/Input_Data/input.json")?;
    let reader = BufReader::new(input_file);
    let input_file_json: InputFileJSONFields = serde_json::from_reader(reader)?;
    Ok(input_file_json)
}

async fn handle_rate_limit(headers: &HeaderMap) -> Result<(), Box<dyn Error>> {
    let reset_timestamp = headers.get("X-RateLimit-Reset")
        .and_then(|h| h.to_str().ok())
        .and_then(|s| s.parse::<u64>().ok())
        .unwrap_or(0);
    
    // Convert the reset timestamp to a DateTime
    let reset_time = DateTime::<Utc>::from(UNIX_EPOCH + Duration::from_secs(reset_timestamp));
    let formatted_reset_time = reset_time.format("%H:%M:%S").to_string();

    let remaining = headers.get("X-RateLimit-Remaining")
        .and_then(|h| h.to_str().ok())
        .unwrap_or("0");

    // Colorful error messages
    println!("{}", "\nGitHub API rate limit exceeded.".red());
    println!("\nRemaining requests: {}", remaining.yellow());
    println!("\nRate limit resets at: {}", formatted_reset_time.yellow());
    println!("\nRate limit hit. Please wait for cooldown or use a personal access token.");

    // Terminates both this Rust program and the parent program
    process::exit(1);
}

// asynchronous wrapper for the get_user_commits() function
#[pyfunction]
fn get_user_commits_sync(py: Python) -> PyResult<()> {
    pyo3_asyncio::tokio::run(py, async {
        get_user_commits().await
    })
}

async fn get_user_commits() -> PyResult<()> {
    let mut repos = vec![];
    let mut commits: Vec<Commit> = Vec::new();
    let client = Client::new();
    let input_file_json = read_input_file().map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?;
    
    let mut headers = HeaderMap::new();
    headers.insert("User-Agent", HeaderValue::from_static("reqwest")); // Always include User-Agent

    // Add Authorization header if the token is provided
    if let Some(token) = input_file_json.API_token {
        headers.insert(
            AUTHORIZATION,
            HeaderValue::from_str(&format!("token {}", token)).map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?,
        );
    }

    let mut page = 1;
    // Grabs the repositories of the target GitHub user
    loop {
        let url = format!("https://api.github.com/users/{}/repos?page={}&per_page=100", input_file_json.target, page);
        let response = client.get(&url).headers(headers.clone()).send().await.map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?;
        
        match response.status() {
            reqwest::StatusCode::TOO_MANY_REQUESTS => {
                handle_rate_limit(response.headers()).await.map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?;
            }
            reqwest::StatusCode::OK => {
                let data: Vec<Value> = response.json().await.map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?;
                if data.is_empty() {
                    break; // No more repositories left
                }
                repos.extend(data);
            }
            reqwest::StatusCode::FORBIDDEN => {
                // The program has likely encountered a private repository, so it will just continue
                continue;
            }
            _ => {
                println!("Unexpected response: {}", response.status());
                break;
            }
        }
        page += 1;
    }
    // Write the number of repositories to a file
    let repo_len = repos.len();
    // location of patch_pirate.py: Hackesoup/Soup/Tools
    let mut repo_count_file = File::create("../Soup/Lib/Data/Special_Output_Data/repo_count.txt").map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?;
    writeln!(repo_count_file, "{}", repo_len).map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?;
    
    // Grabs the commits of the GitHub user
    for repo in repos {
        let repo_name = repo["name"].as_str().unwrap_or("");
        let owner = repo["owner"]["login"].as_str().unwrap_or("");
        let mut page = 1; // Reset page for each repository

        loop {
            let url = format!("https://api.github.com/repos/{}/{}/commits?author={}&page={}&per_page=100", owner, repo_name, input_file_json.target, page);
            let response = client.get(&url).headers(headers.clone()).send().await.map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?;
            
            match response.status() {
                reqwest::StatusCode::TOO_MANY_REQUESTS => {
                    handle_rate_limit(response.headers()).await.map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?;
                }
                reqwest::StatusCode::OK => {
                    let data: Vec<Value> = response.json().await.map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?;
                    if data.is_empty() {
                        break; // No more commits left for this repository
                    }
                    // Pushes the commits to the commits vector
                    for commit in data {
                        let commit_data = Commit {
                            repo: repo_name.to_string(),
                            message: commit["commit"]["message"].as_str().unwrap_or("").to_string(),
                            url: commit["html_url"].as_str().unwrap_or("").to_string(),
                            date: commit["commit"]["author"]["date"].as_str().unwrap_or("").to_string(),
                            sha: commit["sha"].as_str().unwrap_or("").chars().take(7).collect(),
                            email: commit["commit"]["author"]["email"].as_str().unwrap_or("").to_string(),
                        };
                        commits.push(commit_data);
                    }
                    page += 1; // Move to the next page of commits
                }
                reqwest::StatusCode::FORBIDDEN => {
                    // The program has likely encountered a private commit in private repository, so it will just continue
                    continue;
                }
                _ => {
                    println!("Unexpected response: {}", response.status());
                    break;
                }
            }
        }
    }

    // Converts the commits data to JSON format and writes it to a file
    let output_data = serde_json::to_string_pretty(&commits)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?;
    
    // Creates the output JSON file to write the commit data to
    // location of patch_pirate.py: Hackesoup/Soup/Tools
    let mut output_file = File::create("../Soup/Lib/Data/Output_Data/output.json")
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?;
    
    // Writes the commit data to the output file
    output_file.write_all(output_data.as_bytes())
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyException, _>(e.to_string()))?;

    Ok(())
}

#[pymodule]
fn hspatchpiratescanner(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_user_commits_sync, m)?)?; // Use the synchronous wrapper
    Ok(())
}
