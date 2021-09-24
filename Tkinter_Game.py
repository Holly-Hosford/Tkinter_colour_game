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




def game1(event):
    global score
    global time1
    lose = Label(game, text="You Lose", bg="deep sky blue", fg="white", font="Times 16")
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    canvas.delete(ALL)
    colour1 = ["red", "orange", "yellow", "light green", "green", "light blue", "blue", "purple"]
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
    time1 = time()

def loss():
    lose.pack()
    canvas.delete(ALL)



game.mainloop()