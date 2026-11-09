from .computer_builder import ComputerBuilder
def run():
    computer = (
        ComputerBuilder()
        .set_processor("Intel Core i5")
        .set_memory(16)
        .set_storage(512)
        .set_video_card("NVIDIA GeForce RTX 4060")
        .build()
    )
    print("Собран компьютер:")
    print(computer.describe())
if __name__ == "__main__":
            run()