from random import randint


class Brain:
    def __init__(self, body):
        self.body = body

    def act(self):
        _act = randint(0, 4)
        if _act == 0:
            self.body.move_in_x(randint(-6, 6))
        elif _act == 1:
            self.body.move_in_y(randint(-6, 6))
        elif _act == 2:
            self.body.eat()
        elif _act == 3:
            self.body.idle()
