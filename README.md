<h1 align="center">Welcome to Discord AI Bot 👋</h1>
<p>
  <a href="https://opensource.org/license/mit" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/naviamold" target="_blank">
    <img alt="Twitter: naviamold" src="https://img.shields.io/twitter/follow/naviamold.svg?style=social" />
  </a>
</p>

> A Discord bot which you lets you chat with a custom AI powered by Ollama and llama3

## Install

Make sure you have installed following apps

- [Python](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/download)

```sh
ollama serve
ollama run llama3
```

> Run those 2 ollama commands in separate terminal instances AKA DON'T CLOSE the terminal after `ollama serve`

```sh
pip install -r requirements.txt
ren example.env .env
```

### Poetry Install (Optional)

If you have [Poetry](https://python-poetry.org/), you can also install it for installation

```sh
poetry shell
poetry install
```

To also install dev dependencies

```sh
poetry install --with dev
```

## Usage

- Fill out `.env` file with Discord `Token`, Bot `Trigger` word and optionally with an AI `Prompt`

```sh
py main.py
```

## Author

👤 **Naviamold**

- Twitter: [@naviamold](https://twitter.com/naviamold)
- Github: [@Naviamold1](https://github.com/Naviamold1)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check issues page.

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2024 [Naviamold](https://github.com/Naviamold1).<br />
This project is [MIT](https://opensource.org/license/mit) licensed.

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
