import logging

from mosec import Server

from demo.main import Inference

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s - %(process)d - %(levelname)s - %(filename)s:%(lineno)s - %(message)s"
)
sh = logging.StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)


if __name__ == "__main__":
    server = Server()
    server.append_worker(Inference, max_batch_size=8, num=2)
    server.run()
