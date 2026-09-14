import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    if directory == ".":
        print("Result for current directory:")
    else: print(f"Result for '{directory}' directory:")
    try:

        absolute_working_directory = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(absolute_working_directory, directory))

        valid_target_dir = os.path.commonpath([absolute_working_directory, full_path]) == absolute_working_directory

        if not valid_target_dir:
            return f'  Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(full_path):
            return f'  Error: "{directory}" is not a directory'
        
        directory_contents = os.scandir(full_path)
        #print(str(directory_contents))
        
        files_info_list = []
        
        for file in directory_contents:
            file_name = file.name
            file_size = file.stat().st_size
            file_isdir = file.is_dir()
            """ print(file_name)
            print(file_size)
            print(file_isdir) """
            
            file_info = f"  - {file_name}: file_size={file_size} bytes, is_dir={file_isdir}"
            files_info_list.append(file_info)
        
        return "\n".join(files_info_list)
        """ return f'Success: "{directory}" is within the working directory' """
    
    except:
        return "  Error: Something went wrong outside of the planned parameters" 
    
    
schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}