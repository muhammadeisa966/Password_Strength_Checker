import logging

def main():
    print("Main function started")
    # ...existing code...
def setup_logger():
    logger = logging.getLogger("PasswordLogger")
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler("password_checker.log")
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(fh)

    return logger