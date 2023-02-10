from time import sleep

from mosec import Worker


class Inference(Worker):
    def __init__(self) -> None:
        print("init")

    def forward(self, data):
        print("receive request:", data)
        sleep(sum(float(req.get("time", 0)) for req in data))
        return data
