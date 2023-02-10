from mosec import Worker


class Inference(Worker):
    def __init__(self) -> None:
        print("init")

    def forward(self, data):
        print("receive request:", data)
        return data
