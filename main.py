import tkinter
import game

root = tkinter.Tk()
root.title("Snake Game")
root.geometry("500x580")
root.grid()

gameCanvas = tkinter.Canvas(
    root,
    width=498,
    height=498,
    bg="white"
)
gameCanvas.grid(
    row=0,
    column=0
)

game = game.SnakeGame(root, gameCanvas)

root.after(300, game.gameloop)
root.mainloop()
