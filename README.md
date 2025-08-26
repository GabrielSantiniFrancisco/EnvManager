# 👽 EnvManager: The Intergalactic Configurator 👽

Greetings, Earthling!  
Welcome to **EnvManager**, your cosmic companion for managing planetary (and Pythonic) environments.  
Brought to you by [Gabriel Santini Francisco](mailto:gabrielsantinifrancisco@outlook.com), this script is engineered for those who wish to boldly go where no configuration utility has gone before.

---

## 🚀 Mission Briefing

**EnvManager** is a utility class designed to:

- Beam up configuration from Python files
- Teleport environment variables into your system
- Equip your codebase with flexible, extensible, and nerd-approved config management

Perfect for cleaning, processing, and organizing historical JSON data across the galaxy.

---

## 🪐 Features

- **Universal Config Loader:** Reads Python config files from any quadrant.
- **Environment Variable Teleporter:** Instantly sets environment variables and class attributes.
- **Plug-and-Play:** Drop it into your project and start warping through configs.

---

## 🛠️ Installation
Clone the repo and drop `EnvManager.py` into your project like an alien artifact discovered in Area 51:  
```bash
git clone https://github.com/GabrielSantiniFrancisco/EnvManager.git
```

---

## 👾 Usage

```python
from EnvManager import EnvManager

# Initiate the EnvManager with your config file path
env = EnvManager('/path/to/your/config.py')

# Now, your config variables are accessible as attributes!
print(env.YOUR_CONFIG_VARIABLE)
```

---

## 🛠️ API: Starfleet Documentation

### `EnvManager(config_path: str)`

- **Purpose:** Initializes the EnvManager, loads config, sets environment variables.
- **Parameters:**  
  - `config_path` (str): Path to your Python config file.

### `read_config(file_path: str) -> dict`

- **Purpose:** Reads a Python config file and returns its variables as a dictionary.

### `set_env(config: dict) -> None`

- **Purpose:** Sets environment variables and instance attributes based on your config.

---

## 🧬 Example Config File (`config.py`)

```python
# config.py
GALACTIC_SECRET = "42"
PLANET_NAME = "Earth"
ENABLE_WARP_DRIVE = True
```

---

## 🛰️ Why Use EnvManager?

- **Alien-level Simplicity:** No more fumbling with `.env` files or cryptic config formats.
- **Pythonic Telepathy:** Reads native Python files—no translation needed.
- **Extensible:** Add your own cosmic features as you see fit.

---

## 🛸 Contact

Questions? Transmission issues?  
Contact [Gabriel Francisco](mailto:gabrielsantinifrancisco@outlook.com) via subspace comms (or email).

---

> _"May your configs always be clean, and your logs forever verbose."_  
> — The EnvManager Collective

---
