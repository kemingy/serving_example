from time import sleep

from mosec import Worker, get_logger

logger = get_logger()


class Inference(Worker):
    def __init__(self) -> None:
        logger.info("init")

    def forward(self, data):
        logger.info("receive request: %s", data)
        sleep(max(float(req.get("time", 0)) for req in data))
        return data
