# logger.py
import logging
from flask import Flask

def setup_logger(app: Flask):
    """
    Set up logging configuration for the Flask app.
    This will log to both console and a file.
    """
    # Set up basic logging configuration
    logging.basicConfig(
        level=logging.DEBUG,  # Set to the desired level: DEBUG, INFO, WARNING, ERROR, CRITICAL
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )

    # Set the Flask app logger level
    app.logger.setLevel(logging.DEBUG)

    # Optionally, log to a file
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(file_handler)

    return app
