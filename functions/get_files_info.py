import os

def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:

        absolute_working_directory = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(absolute_working_directory, directory))

        valid_target_dir = os.path.commonpath([absolute_working_directory, full_path]) == absolute_working_directory

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(directory):
            return f'Error: "{directory}" is not a directory'
        
        return f'Success: "{directory}" is within the working directory'
    
    except:
        return "Error: Something went wrong outside of the planned parameters" 