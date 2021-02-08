import logging
import os

if not os.path.isdir("logs"):
    os.mkdir("logs")


def get_named_logger(logger_name):
    in_logger = logging.getLogger(logger_name)
    in_logger.setLevel(logging.DEBUG)

    default_fm = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    debug_ch = logging.StreamHandler()
    debug_ch.setLevel(logging.DEBUG)
    debug_ch.setFormatter(default_fm)

    debug_fh = logging.FileHandler(f"logs/{logger_name}_debug.log")
    debug_fh.setLevel(logging.DEBUG)
    debug_fh.setFormatter(default_fm)

    info_fh = logging.FileHandler(f"logs/{logger_name}_info.log")
    info_fh.setLevel(logging.INFO)
    info_fh.setFormatter(default_fm)

    error_fh = logging.FileHandler(f"logs/{logger_name}_error.log")
    error_fh.setLevel(logging.ERROR)
    error_fh.setFormatter(default_fm)

    in_logger.addHandler(debug_fh)
    in_logger.addHandler(error_fh)
    in_logger.addHandler(info_fh)
    in_logger.addHandler(debug_ch)

    # global f_logger
    # f_logger = in_logger

    return in_logger