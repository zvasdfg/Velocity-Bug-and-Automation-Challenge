import os
import yaml
from dotenv import load_dotenv


load_dotenv() 

class Settings:
    UI_BASE_URL = os.getenv("UI_BASE_URL")
    API_BASE_URL = os.getenv("API_BASE_URL")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

class Environment:
    _config = None

    @classmethod
    def load_config(cls, env: str = None):
        """
        Loads configuration from config.yaml and .env
        Priority:
        1. System environment variables
        2. .env file
        3. config.yaml
        """

        load_dotenv()

        if cls._config is None:
            with open("src/config/config.yaml", "r") as file:
                cls._config = yaml.safe_load(file)

        if env:
            cls._config["active_env"] = env

        return cls._config
        
        

    @classmethod
    def get(cls, key: str, default=None):
        """
        Access config values using dot notation
        Example:
            Environment.get("ui.base_url")
        """
        # Environment variable override
        env_value = os.getenv(key.upper().replace(".", "_"))
        BASE_URL = os.getenv("BASE_URL")
        API_BASE_URL = os.getenv("API_BASE_URL")
        USERNAME = os.getenv("USERNAME")
        PASSWORD = os.getenv("PASSWORD")

        if env_value:
            return env_value

        keys = key.split(".")
        value = cls._config

        for k in keys:
            value = value.get(k)
            if value is None:
                return default

        return value