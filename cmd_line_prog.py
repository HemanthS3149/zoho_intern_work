import sys
import os

def is_python_file(file_path):
    return file_path.endswith('.py')

def file_exists(file_path):
    return os.path.isfile(file_path)

def count_lines_of_code(file_path):
    try:
        with open(file_path,'r') as file:
            lines=file.readlines()

        code_lines=[line for line in lines if line.strip() and not line.strip().startswith("#")] #excluding comments and blank lines
        return len(code_lines)
    except Exception as e:
        print(f"An error occurred:{e}")
        sys.exit(1)

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Usage: python count_lines.py <file_path>")
        sys.exit(1)

    file_path=sys.argv[1]
    if not is_python_file(file_path):
        print("The specified file does not exist")
        sys.exit(1)

    lines_of_code=count_lines_of_code(file_path)
    print(f"Number of lines of code: {lines_of_code}")
