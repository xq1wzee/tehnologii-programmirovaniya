from .computer import Computer
class ComputerBuilder:
    def __init__(self):
        self.processor = None
        self.memory = None
        self.storage = None
        self.video_card = "Встроенная"
    def set_processor(self, processor: str):
        self.processor = processor
        return self
    def set_memory(self, memory: int):
        self.memory = memory
        return self
    def set_storage(self, storage: int):
        self.storage = storage
        return self
    def set_video_card(self, video_card: str):
        self.video_card = video_card
        return self
    def build(self) -> Computer:
        if (
            self.processor is None
            or self.memory is None
            or self.storage is None
        ):
            raise ValueError(
                "Необходимо указать процессор, объём ОЗУ и накопитель"
            )
        return Computer(
            processor=self.processor,
            memory=self.memory,
            storage=self.storage,
            video_card=self.video_card
        )