<h1 align="center">Welcome to Discord AI Bot 👋</h1>
<p>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff" style="max-width:100%;">
  </a>
  <a href="https://opensource.org/license/mit" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/naviamold" target="_blank">
    <img alt="Twitter: naviamold" src="https://img.shields.io/twitter/follow/naviamold.svg?style=social" />
  </a>
</p>

> A Discord bot which you lets you chat with a custom AI
> Powered by Ollama and llama3

## Install

Make sure you have installed following apps

- [Python](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/download)

To set up ollama:

```sh
ollama serve
```

Pull the model of your choice (i.e. llama)

```sh
ollama llama3.2
```

> DON'T CLOSE the terminal after `ollama serve`, run other commands in another terminal instance

```sh
git clone https://github.com/Naviamold1/Discord-AI-Bot
cd Discord-AI-Bot
copy config.example.ini config.ini
copy ollama.example.modelfile ollama.modelfile
```

- Fill out `config.ini` file
- If you want to customize the AI behaviour edit the `ollama.modelfile` file

After that run:

```sh
python model.py
```

### Traditional Install

> Preferably install with a virtual environment

```sh
pip install virtualenv
python -m venv env
source env/bin/activate
env/Scripts/activate      # Windows
source env/bin/activate   # Linux/Mac
```

```sh
pip install -r requirements.txt
python main.py
```

### Poetry Install (Optional)

> If you have [Poetry](https://python-poetry.org/), you can use that for installation

```sh
poetry shell
poetry install
poetry run python main.py
```

To also install dev dependencies:

```sh
poetry install --with dev
```

## Usage

- After the setup, simply send a message with a trigger word or on mention (which you set up in `config.ini` file) to start talking to a bot

- Use `!ai clear` to clear AI context history (Set `admin_users_whitelist` in `config.ini` to control who can run that)

## Author

👤 **Naviamold**

- Twitter: [@naviamold](https://twitter.com/naviamold)
- Github: [@Naviamold1](https://github.com/Naviamold1)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Naviamold1/Discord-AI-Bot/issues).

If you do plan to contribute please install and set this up via [Poetry](#poetry-install-optional) and install dev dependencies.

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2024 [Naviamold](https://github.com/Naviamold1).<br />
This project is [MIT](https://opensource.org/license/mit) licensed.

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
