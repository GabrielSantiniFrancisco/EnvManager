# Author : Gabriel Santini Francisco
# Email  : gabrielsantinifrancisco@outlook.com
# Utility class for loading config from a Python file and setting environment variables.

class EnvManager:
    """
    Simple utility class for loading Python configuration files and setting attributes.
    
    Loads a Python config file using exec() and sets all variables as instance attributes.
    Designed for internal use with trusted configuration files.
    """
    def __init__(self, config_path: str):
        """Initialize EnvManager by loading config and setting environment variables."""
        self.config = self.read_config(config_path)
        self.set_env(self.config)

    @staticmethod
    def read_config(file_path: str) -> dict:
        """Read a Python config file and return its variables as a dict."""
        try:
            with open(file_path, 'r') as file: config_content = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error reading configuration file: {e}")
        
        config = {}
        try:
            exec(config_content, config)
        except RuntimeError as e:
            raise RuntimeError(f"Error executing configuration file: {e}")
        except Exception as e:
            raise Exception(f"Unexpected error executing configuration file: {e}")
        
        config.pop('__builtins__', None)
        return config

    def set_env(self, config: dict) -> None:
        """Set environment variables and initialize logger from config."""
        for key, value in config.items(): setattr(self, key, value)
