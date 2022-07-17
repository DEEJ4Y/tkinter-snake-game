import tkinter
import grid
import snake
import random


class SnakeGame:
    # Last keypress direction
    lastDirection = "up"
    foodPosition = None

    def __init__(self, root: tkinter.Tk, canvas: tkinter.Canvas):
        self.root = root
        self.snake = snake.Snake(
            {
                "x": 5,
                "y": 5
            },
            "right"
        )
        self.makeValidFood()
        self.canvas = canvas
        self.grid = grid.Grid(
            canvas=self.canvas,
            size={
                "x": 20,
                "y": 20
            },
            snake=self.snake,
            foodPosition=self.foodPosition
        )

        self.gameStatus = tkinter.StringVar(self.root, value="Playing...")
        tkinter.Label(self.root, textvariable=self.gameStatus).grid(
            row=1,
            column=0
        )

        self.gameScore = tkinter.StringVar(self.root, value="Score: 0")
        tkinter.Label(self.root, textvariable=self.gameScore).grid(
            row=2,
            column=0
        )

        tkinter.Button(self.root, text="Restart",
                       command=self.reset).grid(row=3, column=0)

        self.root.bind("<Left>", lambda _: self.setLastDirection("left"))
        self.root.bind("<Right>", lambda _: self.setLastDirection("right"))

    def makeValidFood(self):
        isValidFood = False
        while not isValidFood:
            randX = random.randint(0, 19)
            randY = random.randint(0, 19)

            matching = False
            for position in self.snake.travelled:
                if position["x"] == randX and position["y"] == randY:
                    matching = True

            if not matching:
                isValidFood = True
                self.foodPosition = {
                    "x": randX,
                    "y": randY
                }

    def setLastDirection(self, lastDirection: str):
        self.lastDirection = lastDirection

    def gameOver(self):
        # Hits wall
        snakeLastPosition = self.snake.travelled[-1]
        if snakeLastPosition["x"] < 0 or snakeLastPosition["x"] >= 20 or snakeLastPosition["y"] < 0 or snakeLastPosition["y"] >= 20:
            return True

        # Hits self
        for snakePosition in self.snake.travelled[0:-2]:
            if snakeLastPosition["x"] == snakePosition["x"] and snakeLastPosition["y"] == snakePosition["y"]:
                return True

        return False

    def reset(self):
        self.canvas.delete("all")

        randDir = ["right", "top", "bottom"][random.randint(0, 2)]

        self.snake = snake.Snake(
            {
                "x": random.randint(5, 15),
                "y": random.randint(5, 15)
            },
            randDir
        )
        self.snake.travelled = self.snake.travelled[-5:-1]
        self.snake.size = 5

        self.makeValidFood()
        self.grid = grid.Grid(
            canvas=self.canvas,
            size={
                "x": 20,
                "y": 20
            },
            snake=self.snake,
            foodPosition=self.foodPosition
        )

        self.gameStatus.set("Playing...")
        self.gameScore.set("Score: 0")

    def gameloop(self):
        if not self.gameOver():
            lastPosition = self.snake.travelled[-1]
            if lastPosition["x"] == self.foodPosition["x"] and lastPosition["y"] == self.foodPosition["y"]:
                currentScore = int(self.gameScore.get().split(" ")[1])
                currentScore = currentScore + 1
                self.gameScore.set(f'Score: {currentScore}')

                self.snake.eat()

                self.makeValidFood()
                self.grid.drawFood(self.foodPosition)

            if self.lastDirection == "left":
                self.snake.goLeft()
            elif self.lastDirection == "right":
                self.snake.goRight()
            else:
                self.snake.goStraight()

            self.grid.drawSnake(self.snake)
            self.setLastDirection("up")
            self.root.after(300, self.gameloop)
        else:
            if not self.gameStatus.get() == "Oops! Game Over":
                self.gameStatus.set("Oops! Game Over")
            self.root.after(300, self.gameloop)
