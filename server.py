import logging

from mosec import Server, Worker

from demo.main import Inference

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s - %(process)d - %(levelname)s - %(filename)s:%(lineno)s - %(message)s"
)
sh = logging.StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)


class Demo(Inference, Worker):
    pass


if __name__ == "__main__":
    # klass = type(Inference.__name__, (Inference, Worker), {})
    server = Server()
    server.append_worker(Demo, max_batch_size=8)
    server.run()
