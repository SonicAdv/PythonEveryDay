import logging
import logging.handlers
LOG_FILE = "./log/get_ios_info.log"
LOG_FILE1 = "./log/image_size.log"


def log_config(logger, log_path):
    hdlr = logging.handlers.TimedRotatingFileHandler(log_path, when='H', interval=1, backupCount=40)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(hdlr)


def debug_log(msg):
    log = logging.getLogger('debug')
    log_config(log, LOG_FILE)
    log.info(msg)


def imagesize_log(msg):
    logger = logging.getLogger('imagesize')
    log_config(logger, LOG_FILE1)
    logger.info(msg)


def main():
    debug_log('456')
    imagesize_log('123')


if __name__ == "__main__":
    main()
