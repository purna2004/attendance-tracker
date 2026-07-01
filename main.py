import logging
import logging.config
import os
import yaml

def setup_logging():
    config_path = "logging.yaml"

    if os.path.exists(config_path):
        with open(config_path, "rt") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(
            filename='app.log',
            filemode='a',
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.INFO
        )
        logging.warning("logging.yaml not found. Using basic configuration.")

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Attendance tracker started...")

if __name__ == "__main__":
    main()