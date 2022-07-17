import tkinter
import snake


class Grid():
    size = {
        "x": 25,
        "y": 25,
    }
    canvas = None
    snakePlacement = []
    foodPosition = None

    def __init__(self, canvas: tkinter.Canvas, size: dict, snake: snake.Snake, foodPosition: dict):
        self.size = size
        self.canvas = canvas
        self.snake = snake
        self.foodPosition = foodPosition

        self.drawGrid()
        self.drawSnake()
        self.drawFood(foodPosition)

    def drawGrid(self):
        for x in range(0, self.size["x"]):
            for y in range(0, self.size["y"]):
                xStart = x * 25
                yStart = y * 25
                xEnd = xStart + 25
                yEnd = yStart + 25
                self.canvas.create_rectangle(
                    xStart,
                    yStart,
                    xEnd,
                    yEnd,
                    fill="black"
                )

    def drawSnake(self, snake=None):
        while not len(self.snakePlacement) == 0:
            popped = self.snakePlacement.pop()
            self.canvas.delete(popped)

        if snake is not None:
            self.snake = snake

        snakeSquares = self.snake.travelled
        for squarePosition in snakeSquares:
            x = squarePosition["x"]
            y = squarePosition["y"]
            xStart = x * 25
            yStart = y * 25
            xEnd = xStart + 25
            yEnd = yStart + 25
            currentSnakeSquare = self.canvas.create_rectangle(
                xStart,
                yStart,
                xEnd,
                yEnd,
                fill="green"
            )
            self.snakePlacement.append(currentSnakeSquare)

    def drawFood(self, foodPosition: dict):
        if self.foodPosition is not None:
            self.canvas.delete(self.foodPosition)

        x = foodPosition["x"]
        y = foodPosition["y"]
        xStart = x * 25
        yStart = y * 25
        xEnd = xStart + 25
        yEnd = yStart + 25
        self.foodPosition = self.canvas.create_rectangle(
            xStart,
            yStart,
            xEnd,
            yEnd,
            fill="red"
        )
