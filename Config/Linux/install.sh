#!/bin/sh

# ==============================================================================
# Hackesoup - Robust Installation Script for Linux
# ==============================================================================
#
# USAGE:
# This script MUST be run from the project's root directory.
# Example:
#   cd /path/to/Hackesoup
#   sh Config/Linux/install.sh
#
# ==============================================================================

# --- Script Settings ---
# Exit immediately if a command exits with a non-zero status.
set -e
# Treat unset variables as an error.
set -u

# --- Color Definitions (for readable output) ---
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# --- Helper Functions ---
log_info() {
    # Using printf for better portability than echo -e
    printf "${GREEN}[INFO]${NC} %s\n" "$1"
}

log_warn() {
    printf "${YELLOW}[WARN]${NC} %s\n" "$1"
}

log_error() {
    printf "${RED}[ERROR]${NC} %s\n" "$1" >&2
}

# ==============================================================================
#                              MAIN SCRIPT BODY
# ==============================================================================

# STEP 1: VERIFY SCRIPT LOCATION 
# ------------------------------------------------------------------------------
# We ensure the script is being run from the project's root directory by
# checking for the existence of key files and directories.
# This prevents all path-related errors.
#
log_info "Verifying execution location..."
if [ ! -f "requirements.txt" ] || [ ! -d "Interfaces" ] || [ ! -d "Soup" ] || [ ! -d "LICENSE"]; then
    log_error "This script must be run from the project root directory (the 'Hackesoup' folder)."
    printf "Please change your directory to the project root and try again.\n"
    printf "Example:\n"
    printf "  cd /path/to/your/Hackesoup\n"
    printf "  sh Config/Linux/install.sh\n"
    exit 1
fi
log_info "Execution location is correct. Proceeding with installation."
echo

# STEP 2: CHECK FOR SYSTEM DEPENDENCIES
# ------------------------------------------------------------------------------
log_info "Checking for required system dependencies (python3, pip, git)..."
for dep in python3 pip git; do
    if ! command -v "$dep" > /dev/null 2>&1; then
        log_error "Dependency '$dep' not found. Please install it using your system's package manager."
        exit 1
    fi
done

# Specifically check for the 'venv' module, which is sometimes a separate package.
if ! python3 -c "import venv" > /dev/null 2>&1; then
    log_error "Python3 'venv' module is not installed. It is required to create a virtual environment."
    printf "On Debian/Ubuntu, you can install it with: sudo apt-get install python3-venv\n"
    exit 1
fi
log_info "All system dependencies are met."
echo

# STEP 3: CREATE AND ACTIVATE PYTHON VIRTUAL ENVIRONMENT
# ------------------------------------------------------------------------------
VENV_DIR=".venv"
log_info "Setting up Python virtual environment..."

if [ -d "$VENV_DIR" ]; then
    log_warn "Virtual environment '$VENV_DIR' already exists. Skipping creation."
else
    log_info "Creating virtual environment in './$VENV_DIR'..."
    python3 -m venv "$VENV_DIR"
fi

# Activate the virtual environment for the rest of this script's execution.
# The '.' command is the POSIX-compliant equivalent of 'source'.
. "./$VENV_DIR/bin/activate"
log_info "Virtual environment activated. Python is now: $(python --version)"
echo

# STEP 4: INSTALL PYTHON DEPENDENCIES
# ------------------------------------------------------------------------------
# This step is now guaranteed to work because STEP 1 verified that
# 'requirements.txt' exists in the current directory.
#
log_info "Installing Python dependencies from 'requirements.txt'..."
pip install -q -r requirements.txt
log_info "All Python dependencies installed successfully."
echo

# STEP 5: SET FILE PERMISSIONS
# ------------------------------------------------------------------------------
# This is also guaranteed to work because STEP 1 verified that the
# 'Interfaces' and 'Soup' directories exist.
#
log_info "Setting executable permissions for tool scripts..."
find Interfaces Soup/Tools -type f -name "*.py" -exec chmod +x {} \;
log_info "File permissions have been set."
echo

# STEP 6: INSTALLATION COMPLETE
# ------------------------------------------------------------------------------
printf "${GREEN}==========================================\n"
log_info "Hackesoup installation is complete!"
printf "${GREEN}==========================================\n\n"

printf "INSTRUCTIONS TO RUN THE APPLICATION:\n"
printf "1. Activate the virtual environment in your terminal:\n"
printf "   ${YELLOW}. .venv/bin/activate${NC}\n\n"
printf "2. Run the main interface script:\n"
# This now points to the correct file as requested by the owner.
printf "   ${YELLOW}cd Interfaces\n"
printf "   ${YELLOW}python3 hsmi.py${NC}\n\n"
printf "3. When you are finished, deactivate the environment:\n"
printf "   ${YELLOW}deactivate${NC}\n"