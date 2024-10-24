import ollama


prompt = 'you are a ai designed to help developers start their projects quicker. You will be given a certain project/coding environment to create. Examples could be:"svelte project" or "start a new node.js/angular project" etc. You will take these tasks, and useing your tools, create the project'


def ollama_chat(text):
    model = "llama3.2"
    response = ollama.chat(model=model, messages=[
        {
            'role':'system',
            'content': prompt,
        },
        {
            'role': 'user',
            'content': text,
        },
    ])
    return response
