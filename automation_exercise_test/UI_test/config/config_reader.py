import yaml
from pathlib import Path

class ConfigReader:
    def __init__(self, config_path):
        self._data = self._load(config_path)
        self.config_path = config_path


    @staticmethod
    def _load(path: str):
        with open(Path(path), "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    @property
    def base_url(self):
        return self._data.get("base_url")

    @property
    def browser(self):
        return self._data.get("browser", "chromium")

    @property
    def headless(self):
        return self._data.get("headless", True)

    @property
    def slow_mo(self):
        return self._data.get("slow_mo", 0)

    @property
    def timeout(self):
        return self._data.get("timeout", 5000)

    @property
    def env(self):
        return self._data.get("env", "local")
