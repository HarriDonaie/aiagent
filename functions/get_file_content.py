import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    
    try:
        
        absolute_working_directory = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(absolute_working_directory, file_path))

        valid_target_dir = os.path.commonpath([absolute_working_directory, full_path]) == absolute_working_directory

        if not valid_target_dir:
            return f'  Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(full_path):
            return f'  Error: File not found or is not a regular file: "{file_path}"'
        
        f = open(full_path)
        #print(f"reading {full_path}")
        file_contents = f.read(MAX_CHARS)
        if f.read(1):
            #print("truncating")
            file_contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_contents
    except Exception as e:
            return f"Error: {e}"