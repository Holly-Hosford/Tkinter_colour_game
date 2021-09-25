from tkinter import *
import random
from time import *
game = Tk()
game.config(bg="deep sky blue")
canvas = Canvas(game, width=500, height=500)
canvas.configure(bg="sky blue")
canvas.pack()

score = 0
colour1 = ["red", "orange", "yellow", "light green", "green", "light blue", "blue","purple"]
game_2_colours = ["red", "orange", "yellow", "green"]

timing = 0


def begin():
    global time1
    colour1 = ["red", "orange", "yellow", "light green", "green", "light blue", "blue", "purple"]
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    square = canvas.create_rectangle(x, y,x+100,y+100, fill="blue")
    canvas.tag_bind(square, "<Button-1>", game1)
    start.config(state="disabled")
    if time1 != time():
        time1 = time()

def end(event):
    game.destroy()

def reset():
    global score
    global timing
    canvas.delete(ALL)
    score = 0
    score_label["text"] = ("Score", (score))
    timing = 0
    time_label["text"] = ("Time", timing)
    start.config(state="normal")
    lose.pack_forget()


score_label = Label(game, text=("Score",score), bg="deep sky blue", fg="white", font="Times 12")
score_label.pack()
time_label = Label(game, text=("Time", timing), bg="deep sky blue", fg="white", font="Times 12")
time_label.pack()
game.bind("<Control-c>", end)
time1 = time()
start = Button(game, text = "Start", width=70, height=2, bg="green", fg="white", activebackground="light green", activeforeground="white", relief="ridge",command=begin)
start.pack()
reset = Button(game, text="Reset", width=70, height=2, bg="red3", fg="white", activebackground="brown1", activeforeground="white", relief="ridge", command=reset)
reset.pack()
lose = Label(game, text="You Lose", bg="deep sky blue", fg="white", font="Times 16")

def loss():
    if score >= 20:
        game2.colour_label.pack_forget()
    lose.pack()
    canvas.delete(ALL)


def game1(event):
    global score
    global time1
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    canvas.delete(ALL)
    square = canvas.create_rectangle(x, y, x + 100, y + 100, fill=colour1[random.randint(0, 7)])
    canvas.tag_bind(square, "<Button-1>", game1)
    time2 = time()
    timing = (time2 - time1)
    if timing > 2:
        loss()
    if timing < 2:
        if timing < 0.4:
            score += 5
        else:
            score += 1
    score_label["text"] = ("Score", (score))
    time_label["text"] = ("Time", ("%.3f" % (timing)))
    if score >= 20:
        canvas.delete(ALL)
        game2("<Button-1>")
        time1 = time()
    time1 = time()
    
def game2(event):
    global score
    global time1
    global num
    canvas.delete(ALL)
    square2 = canvas.create_rectangle(75, 75, 175, 175, fill="red")
    square3 = canvas.create_rectangle(325, 75, 425, 175, fill="orange")
    square4 = canvas.create_rectangle(75, 325, 175, 425, fill="yellow")
    square5 = canvas.create_rectangle(325, 325, 425, 425, fill="green")
    num = random.randint(0, 3)
    game2.colour_label = Label(text=game_2_colours[num], bg=game_2_colours[num])
    game2.colour_label.pack()
    list_squares = [square2, square3, square4, square5]
    canvas.tag_bind(list_squares[num], "<Button-1>", clicked)
    time2 = time()
    timing = (time2 - time1)
    if timing > 2:
        loss()
    if timing < 2:
        if timing < 0.75:
            score += 5
        else:
            score += 1
    score_label["text"] = ("Score", (score))
    time_label["text"] = ("Time", ("%.3f" % (timing)))
    time1 = time()

def clicked(event):
    game2.colour_label.pack_forget()
    game2("<Button-1>")





game.mainloop()
