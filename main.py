from logger import setup_logging
import logging

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Attendance tracker started...")

if __name__ == "__main__":
    main()