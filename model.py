import colorama
import ollama
from httpx import ConnectError


def create_model():
    with open("ollama.modelfile", "r") as f:
        modelfile = f.read()

    try:
        ollama.create(model="custom-discord-model", modelfile=modelfile)
        return f"{colorama.Fore.GREEN}Model created!{colorama.Style.RESET_ALL}"

    except ConnectError:
        raise ConnectError(
            f"{colorama.Fore.RED}Ollama server not running!{colorama.Fore.MAGENTA}\n ➜ Run `ollama serve`{colorama.Style.RESET_ALL}"
        )


print(create_model())
