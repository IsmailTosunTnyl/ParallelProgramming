import time
import random


class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


class FindE:

    def __init__(self):
        self.counter = 0

    def throw_points(self, nn):

        for _ in range(nn):

            sum = 0
            while True:
                sum = sum + random.uniform(0, 1)
                self.counter += 1
                if sum >= 1:
                    break

        return self.counter/nn
