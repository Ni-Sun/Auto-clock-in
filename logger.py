import logging
from logging.handlers import TimedRotatingFileHandler


def get_logger(log_file='clock_in.log'):
    """创建隔离的自定义日志器"""
    # 创建专属日志器（非 root）
    logger = logging.getLogger("MyLogger")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False  # 关键：禁止日志传播

    # 避免重复初始化
    if logger.handlers:
        return logger

    # 文件处理器（仅记录自定义日志）
    file_handler = TimedRotatingFileHandler(
        filename=log_file,
        when='midnight',
        backupCount=30,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)-8s - %(message)s'
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # 控制台处理器配置（在 root logger）
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)-8s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)

    # 配置 root logger 仅用于控制台输出
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    if not root_logger.handlers:
        root_logger.addHandler(console_handler)

    # 抑制第三方库日志传播
    logging.getLogger("selenium").propagate = False
    logging.getLogger("urllib3").propagate = False

    return logger
def main():
    # 创建过滤器：只允许 CRITICAL 级别
    class CriticalFilter(logging.Filter):
        def filter(self, record):
            return record.levelno == logging.CRITICAL

    # 初始化日志器（控制台输出 WARNING 及以上，文件记录所有级别）
    logger = get_logger(
        log_file='clock_in.log'  # 日志文件名
    )

    # 测试日志输出
    logger.debug("Debug 消息（不会显示）")
    logger.info("Info 消息（不会显示）")
    logger.warning("Warning 消息（不会显示）")
    logger.critical("Critical 消息（显示并记录）")


if __name__ == '__main__':
    main()
