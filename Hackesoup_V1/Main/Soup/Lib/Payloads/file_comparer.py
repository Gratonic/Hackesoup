def compare_files(file1_path, file2_path, output_path):
    # Read lines from the first file
    with open(file1_path, 'r') as file1:
        lines_file1 = set(file1.readlines())

    # Read lines from the second file
    with open(file2_path, 'r') as file2:
        lines_file2 = set(file2.readlines())

    # Find unique lines
    unique_to_file1 = lines_file1 - lines_file2
    unique_to_file2 = lines_file2 - lines_file1

    # Write unique lines to the output file
    with open(output_path, 'w') as output_file:
        output_file.write("Unique to {}:\n".format(file1_path))
        output_file.writelines(unique_to_file1)
        output_file.write("\nUnique to {}:\n".format(file2_path))
        output_file.writelines(unique_to_file2)

# Example usage
if __name__ == "__main__":
    file1 = 'file_1_name.txt'
    file2 = 'file_2_name.txt'
    output_file = 'output_file_name.txt'

    compare_files(file1, file2, output_file)
    print(f"Unique lines written to {output_file}")