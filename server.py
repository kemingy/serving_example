from mosec import Server

from demo.main import Inference


if __name__ == "__main__":
    server = Server()
    server.append_worker(Inference, max_batch_size=8, num=2)
    server.run()
