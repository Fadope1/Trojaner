from Server.config import logger, TIMEOUT_TIME

import time


def dont_accept_keyboard_interrupt(func):
    def inner():
        try:
            func()
        except KeyboardInterrupt:
            logger.warn(" [PRIVILAGE] Only admins can stop the server, type @help for help")
    return inner


@dont_accept_keyboard_interrupt
def timeout():
    time.sleep(TIMEOUT_TIME)
