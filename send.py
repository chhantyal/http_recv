import logging

from logging.handlers import HTTPHandler

logger = logging.getLogger(__name__)

server = 'https://log-recv.herokuapp.com:80'

http_handler = HTTPHandler(server, '/', method='POST')

logger.addHandler(http_handler)
logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
    logger.debug("Debug message logged to remote server")
    print("Logs sent to {}:)".format(server))
