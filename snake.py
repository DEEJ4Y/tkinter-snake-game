import direction


class Snake:
    size = 5
    travelled = []
    position = None
    direction = None

    def __init__(self, startPosition, startDirection):
        self.position = startPosition
        self.direction = startDirection

        for i in range(self.size):
            self.travelled.append(
                {"x": startPosition["x"]-self.size+i+1, "y": startPosition["y"]})

    def eat(self):
        self.size = self.size + 1

    def nextPosition(self):
        travelled = self.travelled
        last = travelled[-1]
        next = {}
        if(self.direction == "top"):
            next["y"] = last["y"] + 1
            next["x"] = last["x"]
        elif(self.direction == "right"):
            next["y"] = last["y"]
            next["x"] = last["x"] + 1
        elif(self.direction == "bottom"):
            next["y"] = last["y"] - 1
            next["x"] = last["x"]
        elif(self.direction == "left"):
            next["y"] = last["y"]
            next["x"] = last["x"] - 1

        self.travelled.append(next)
        if len(travelled) > self.size:
            self.travelled.pop(0)

    def goLeft(self):
        self.direction = direction.moveLeft(self.direction)
        self.nextPosition()

    def goRight(self):
        self.direction = direction.moveRight(self.direction)
        self.nextPosition()

    def goStraight(self):
        self.nextPosition()
