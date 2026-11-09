from dataclasses import dataclass
@dataclass(frozen=True)
class Computer:
    processor: str
    memory: int
    storage: int
    video_card: str
    def describe(self) -> str:
        return (
            f"Процессор: {self.processor}; "
            f"ОЗУ: {self.memory} ГБ; "
            f"Накопитель: {self.storage} ГБ; "
            f"Видеокарта: {self.video_card}"
        )