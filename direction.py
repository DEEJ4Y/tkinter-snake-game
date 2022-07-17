def moveRight(currentDirection):
    if currentDirection == "left":
        return "bottom"
    elif currentDirection == "top":
        return "left"
    elif currentDirection == "right":
        return "top"
    else:
        return "right"


def moveLeft(currentDirection):
    if currentDirection == "left":
        return "top"
    elif currentDirection == "top":
        return "right"
    elif currentDirection == "right":
        return "bottom"
    else:
        return "left"
