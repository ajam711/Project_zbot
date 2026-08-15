import os 

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        cwd_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(cwd_abs, directory))
        valid_target_dir = os.path.commonpath([cwd_abs, target_dir]) == cwd_abs
        if not valid_target_dir:
            return f'Result for {directory} directory:\n\tError: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Result for {directory} directory:\n\tError: "{directory}" is not a directory'
        
        dir_list = sorted(os.listdir(target_dir))
        directory_info = []
        for item in dir_list:
            item_path = os.path.join(target_dir, item)
            item_info = f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
            directory_info.append(item_info)
        if directory == ".":
            header = "Result for current directory:"
        else:
            header = f"Result for '{directory}' directory:"
        return "\n\t".join([header] + directory_info)
    except Exception as e:
        return f"Error: {e}"


    




