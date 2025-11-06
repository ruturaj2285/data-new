import logging


def configure_logger(event_id: str) -> logging.Logger:
    
    event_uniqe_id = event_id.split('-')[-1][-4:]
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # Remove existing handlers to avoid duplicate logs in Lambda
    if logger.handlers:
        for h in list(logger.handlers):
            logger.removeHandler(h)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        fmt=f"%(levelname)s: %(asctime)s: {event_uniqe_id}: [Online Data Collection Controller]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


