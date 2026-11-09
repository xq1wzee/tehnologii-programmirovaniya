from .settings import AppSettings
def run():
    first_settings = AppSettings()
    second_settings = AppSettings()
    first_settings.theme = "dark"
    print("Первый объект:", first_settings.show())
    print("Второй объект:", second_settings.show())
    print("Это один объект:", first_settings is second_settings)
if __name__ == "__main__":
            run()