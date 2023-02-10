class Inference:
    def __init__(self) -> None:
        print("init")

    def forward(self, data):
        print("receive request: %s", data)
        return data
