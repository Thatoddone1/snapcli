import ollama
import os

prompt = 'You are an AI assistant to help developers create projects. Use tools to create files and folders as needed. After each action, ask if further actions are needed. If no more actions are needed, say "no further changes".'

def create_file_tool(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    return f"File '{filename}' created successfully."

def create_folder_tool(foldername):
    os.makedirs(foldername, exist_ok=True)
    return f"Folder '{foldername}' created successfully."

def ollama_chat(text):
    model = "llama3.2:1b"
    messages = [
        {
            'role': 'system',
            'content': prompt,
        },
        {
            'role': 'user',
            'content': text,
        },
    ]
    tools = [
        {
            'name': 'create_file',
            'function': create_file_tool,
            'description': 'Creates a new file with the given content.',
            'parameters': {
                'filename': 'string',
                'content': 'string'
            }
        },
        {
            'name': 'create_folder',
            'function': create_folder_tool,
            'description': 'Creates a new folder.',
            'parameters': {
                'foldername': 'string'
            }
        }
    ]

    while True:
        response = ollama.chat(
            model=model,
            messages=messages,
            tools=tools
        )
        messages.append({
            'role': 'assistant',
            'content': response['content']
        })
        if 'no further changes' in response['content'].lower():
            break
        messages.append({
            'role': 'system',
            'content': 'Do you need any further actions?'
        })
    return response
