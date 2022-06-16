import os
import logging
import logging.handlers

from os.path import exists, normpath, join


def set_logger(name='CxConsolidatedReports', level=logging.DEBUG, format_string=None, log_folder=None, when="D",
               backup_count=5):
    """

    Args:
        name (str): Log name
        level (int):  Logging level, e.g. ``logging.INFO``
        format_string (str):  Log message format
        log_folder (str):
        when (str):
            S - Seconds
            M - Minutes
            H - Hours
            D - Days
            midnight - roll over at midnight
            W{0-6} - roll over on a certain day; 0 - Monday
        backup_count (int):

    Returns:

    """
    log_file_name = "cxreporting.log"

    if format_string is None:
        format_string = "%(asctime)s %(name)s [%(levelname)s] %(message)s"

    if log_folder is None or not exists(log_folder):
        log_folder = normpath(join(os.getcwd(), "logs"))
        if not exists(log_folder):
            os.mkdir(log_folder)
    filename = normpath(join(log_folder, log_file_name))
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.handlers.TimedRotatingFileHandler(
        filename=filename, when=when, backupCount=backup_count, encoding="utf-8"
    )
    handler.setLevel(level)
    formatter = logging.Formatter(format_string)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
