from .singleton.demo import run as run_singleton
from .factory_method.demo import run as run_factory_method
from .abstract_factory.demo import run as run_abstract_factory
from .builder.demo import run as run_builder
def main():
    print("=== Singleton ===")
    run_singleton()
    print("\n=== Factory Method ===")
    run_factory_method()
    print("\n=== Abstract Factory ===")
    run_abstract_factory()
    print("\n=== Builder ===")
    run_builder()
if __name__ == "__main__":
    main()