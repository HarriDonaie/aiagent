import os, subprocess
def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        #print("a")
        absolute_working_directory = os.path.abspath(working_directory)
        #print("b")
        full_path = os.path.normpath(os.path.join(absolute_working_directory, file_path))
        #print("c")
        valid_target_dir = os.path.commonpath([absolute_working_directory, full_path]) == absolute_working_directory

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'
        
        #print("d")
        command = ["python", full_path]
        if args:
            command.extend(args)
        #print("e")
        result: subprocess.CompletedProcess = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=absolute_working_directory)
        #print("f")
        output_string = ""
        if result.returncode != 0:
            output_string += f"Process exited with code {result.returncode}\n"
        elif result.stderr is None and result.stdout is None:
            output_string += "No output produced\n"
        else:
            output_string += f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        return output_string
    except Exception as e:
        print(f"Error: executing Python file: {e}")

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}