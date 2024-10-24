import typer
import ollama_module

app = typer.Typer()


@app.command()
def create(project: str):
    #run some thing here
    response = ollama_module.ollama_chat(project)
    print(response)


if __name__ == "__main__":
    app()
