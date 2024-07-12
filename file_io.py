class CustomException(Exception):
    """A custom exception for demonstration purposes."""
    pass

def create_large_file(file_path):
    try:
        with open(file_path,"w") as file:
            for i in range(100):
                file.write(f"This is line {i+1}\n")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def process_large_file(file_path):
    try:
        with open(file_path,'r') as file:
            for line in file:
                process_line(line)
    except FileNotFoundError as e:
        print(f"Error: The file '{file_path}' was not found. {e}")
    except PermissionError as e:
        print(f"Error: Permission denied when trying to read the file '{file_path}'")
    except Exception as e:
        print(f"An unexpected error occurred while processing the file:{e}")

def process_line(line):
    try:
        print(line.strip())
    except Exception as e:
        print(f"An error occurred while processing the line: {e}")

def main():
    file_path='large_file.txt'

    create_large_file(file_path)
    process_large_file(file_path)

if __name__=="__main__":
    main()