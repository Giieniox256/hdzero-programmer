import logging
import os


def setup_logger(log_file_name="app.log", log_dir="logs", log_level=logging.DEBUG):
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # remove old handlers
    while logger.hasHandlers():
        logger.removeHandler(logger.handlers[0])

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # path to base folder
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    log_folder_path = os.path.join(base_path, log_dir)

    # create folder if not exist
    if not os.path.exists(log_folder_path):
        os.makedirs(log_folder_path)

    log_file_path = os.path.join(log_folder_path, log_file_name)

    file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

# # Przykład użycia:
# logger = setup_logger()
# logger.info("Logger zapisuje do folderu logs w głównym katalogu")
