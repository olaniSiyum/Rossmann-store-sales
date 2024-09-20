import logging

def setup_logger():
    logging.basicConfig(
        filename='../notebooks/logs/project_log.log', 
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger()
    return logger