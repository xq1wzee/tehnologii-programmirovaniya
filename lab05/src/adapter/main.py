from adapter import ExternalLogger, LoggerAdapter

def main():
    external_logger = ExternalLogger()
    logger = LoggerAdapter(external_logger)
    logger.log("This is a test message.")

if __name__ == "__main__":
    main()