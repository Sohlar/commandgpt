import dcg_templates
def generate_code(parsed_command):
    action = parsed_command['action']
    parameters = parsed_command['parameters']

    action_to_function_map = {
        'create directory': dcg_templates.create_directory,
        'delete directory': dcg_templates.delete_directory,
        'rename directory': dcg_templates.rename_directory,
        'list directory content': dcg_templates.list_directory_content,
        'create file': dcg_templates.create_file,
        'delete file': dcg_templates.delete_file,
        'rename file': dcg_templates.rename_file,
        'append file': dcg_templates.append_file,
        'move file': dcg_templates.move_file,
        'copy file': dcg_templates.copy_file,
        'change file permissions': dcg_templates.change_file_permissions,
        'unzip files': dcg_templates.unzip_files,
        'undo file': dcg_templates.undo_file,
        'download file': dcg_templates.download_file,
        'run shell command': dcg_templates.run_shell_command,
        'schedule task': dcg_templates.schedule_task,
        'execute script': dcg_templates.execute_script,
        'terminate process': dcg_templates.terminate_process,
        'monitor system_resources': dcg_templates.monitor_system_resources
    }

    code_generation_function = action_to_function_map.get(action)

    if code_generation_function:
        return code_generation_function(**parameters)
    else:
        raise ValueError(f"Unsupported action for python code generation: {action}")
    pass
