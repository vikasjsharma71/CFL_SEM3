import os

def main():
    # Get directory from user
    dir_path = input("Enter Directory: ")
    
    # Get first letter of file from user
    first_letter = input("Enter first letter of file: ")
    
    try:
        # List files in the directory
        files = os.listdir(dir_path)
        
        # Filter files that start with the specified letter
        filtered_files = [file for file in files if file.startswith(first_letter)]
        
        if not filtered_files:
            print("No files found starting with that letter.")
        else:
            for filename in filtered_files:
                print(filename)
                
    except FileNotFoundError:
        print("Either dir does not exist or is not a directory")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
