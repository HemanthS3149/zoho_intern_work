class CustomException(Exception):
    """A custom execption for demonstration purposes"""
    pass

def perform_division(dividend,divisor):
    try:
        result=dividend/divisor
        return result
    except ZeroDivisionError as e:
        print(f"Error: Division by zero is not allowed. {e}")
    except TypeError as e:
        print(f"Error: Invalid type provided. Both dividend and divisor must be numbers. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def read_file(file_path):
    try:
        with open(file_path,'r') as file:
            content=file.read()
            return content
    except FileNotFoundError as e:
        print(f"Error: The file '{file_path}' was not found. {e}")
    except PermissionError as e:
        print(f"Error: Permission denied when trying to read the file '{file_path}'. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        print(f"Error: Cannot convert '{value}' to an integer. {e}")
    except TypeError as e:
        print(f"Error: Invalid type provided.{e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("Division Example:")
    perform_division(10,2)
    perform_division(10,0)
    perform_division(10,'a')

    print("\nFile Reading Example:")
    read_file("non_existing_file.txt")

    print("\nConversion to integer example:")
    convert_to_int("123")
    convert_to_int("abc")
    convert_to_int(None)

    print("\nCustom Exception Example:")
    try:
        raise CustomException("This is a custom exception.")
    except CustomException as e:
        print(f"Caught a custom exception: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__=="__main__":
    main()