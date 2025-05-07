import logging
import os
from datetime import datetime

def setup_logger():
    """
    Sets up and returns a logger instance configured to write to both file and console.
    Creates a new log file for each test run with timestamp in the filename.
    """
    try:
        # Logs directory path relative to framework root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_dir = os.path.join(base_dir, "logs")
        
        # Create logs directory if it doesn't exist
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            print(f"Created logs directory at: {log_dir}")

        # Create log filename with date and time
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = os.path.join(log_dir, f"test_run_{current_time}.log")

        # Set up logger with a unique name
        logger = logging.getLogger('selenium_framework')
        logger.setLevel(logging.INFO)
        logger.propagate = True  # Allow logs to propagate to parent loggers

        # Clear old handlers if any
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

        # File handler with detailed formatting
        file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
        file_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Log the start of a new test run
        logger.info("="*50)
        logger.info("Starting new test run")
        logger.info("="*50)

        return logger
        
    except Exception as e:
        print(f"Error setting up logger: {str(e)}")
        raise
