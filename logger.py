import logging

def get_logger(level=logging.WARNING, filter=None):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        logger.addHandler(get_handler(level, filter))
    return logger

def get_handler(level, filter):
    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s')
    handler.setFormatter(formatter)
    if filter is not None:
        handler.addFilter(filter)
    return handler

def main():
    filter = logging.Filter()
    filter.filter = lambda record: record.levelno == logging.CRITICAL
    logger = get_logger()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

if __name__ == '__main__':
    main()
