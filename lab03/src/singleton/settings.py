class AppSettings:
    """Хранит единственный экземпляр настроек приложения."""
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        if not hasattr(self, "_initialized"):
            self.theme = "light"
            self.language = "ru"
            self._initialized = True
    def show(self):
        return f"Тема: {self.theme}, язык: {self.language}"