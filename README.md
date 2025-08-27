# EnvManager

A professional, flexible, and structured environment configuration utility for Python applications. This module provides a simple interface for loading configuration from Python files and setting environment variables dynamically. Designed for use in production-grade systems where clean configuration management and environment setup are essential.

## Features

- **Configurable Environment**: Load configuration from a Python file and set environment variables and attributes automatically.
- **Simple API**: Minimal, easy-to-use interface for integrating environment management into any Python project.
- **Extensible**: Easily extend or customize for additional environment setup needs.
- **No Hardcoded Paths**: Accepts any configuration file path, supporting flexible project structures.

## Usage

### 1. Installation
Copy `EnvManager.py` into your project (e.g., in a `lib/` or `utils/` directory).

### 2. Example Configuration File (`config.py`)
```python
# config.py
API_KEY = "your-api-key"
DEBUG = True
LOG_LEVEL = "INFO"
```

### 3. Basic Usage
```python
from EnvManager import EnvManager

env = EnvManager("config.py")

print(env.API_KEY)      
print(env.DEBUG)
print(env.LOG_LEVEL)
```

### 4. Environment Variable Access
After initialization, configuration values are also available as global variables:
```python
print(API_KEY)  
```

## API Reference

### `EnvManager(config_path: str)`
- **config_path**: Path to the Python configuration file.

#### Methods
- `read_config(file_path: str) -> dict`  
  Reads a Python config file and returns its variables as a dictionary.

- `set_env(config: dict) -> None`  
  Sets environment variables and instance attributes based on the provided configuration dictionary.

## Advanced Details
- **Dynamic Attribute Assignment**: All config keys become attributes of the `EnvManager` instance.
- **Global Scope Option**: All config keys are also set as global variables for easy access throughout your codebase.
- **No External Dependencies**: Pure Python, no third-party requirements.

## License
MIT License

## Author
Gabriel Santini Francisco  
Email: gabrielsantinifrancisco@outlook.com

---

*For questions, suggestions, or contributions, please open an issue or pull request
