from random import randint


class Brain:
    def __init__(self, body):
        self.body = body

    def act(self):
        self.body.dx += randint(-6, 6)
        self.body.dy += randint(-6, 6)
