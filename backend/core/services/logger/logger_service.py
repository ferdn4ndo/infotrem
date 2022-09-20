import logging
import inspect
import os

from datetime import datetime

from api.settings import BASE_DIR


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    log_level = logging.DEBUG if os.environ['ENV_MODE'] == 'dev' else logging.WARNING
    logger.setLevel(log_level)

    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_code

    logger_handler = logging.FileHandler(filename=get_log_filename(name))
    logger_handler.setLevel(log_level)
    logger_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - {} ({}:{}) - %(message)s'.format(
            func.co_name,
            func.co_filename,
            func.co_firstlineno
        )
    )
    logger_handler.setFormatter(logger_formatter)
    logger.addHandler(logger_handler)

    return logger


def get_log_filename(name: str) -> str:
    today = datetime.today()
    date = datetime(today.year, today.month, today.day)

    log_filename = os.path.join(BASE_DIR, "logs", "{}_{:04d}-{:02d}-{:02d}.log".format(
        name,
        date.year,
        date.month,
        date.day
    ))

    return log_filename
