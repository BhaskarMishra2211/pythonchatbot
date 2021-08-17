from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *


mybot = ChatBot(name="First",read_only = True)

small_talks = [
    "how are you?",
    "I'm great",
    "where are you ?",
    "I'm on the internet",
    "What is your name?",
    "My name is First",
    "Tell me your name?",
    "which is your fav.movie?",
    "My fav.movie is Mission Impossible",
    "Do you watch anime?",
    "yes I do, demon slayer is my favourite"
]


list_trainer = ListTrainer(mybot)
list_trainer.train(small_talks)



main = Tk()


def ask_here():
    query = textF.get()
    reply_from_bot = mybot.get_response(query)
    msgs.insert(END,"you:"+query)
    msgs.insert(END,"First:"+str(reply_from_bot))
    textF.delete(0,END)

main.geometry("500x500")
main.title("task2")

frame = Frame(main)
sb = Scrollbar(frame)
msgs = Listbox(frame,width=100,height=20)

sb.pack(side=RIGHT,fill = Y)
msgs.pack(side=LEFT,fill=BOTH,pady = 20)
frame.pack()


# creating a textfield
textF = Entry(main,font = ("monospace",12))
textF.pack(fill = X,pady=20)

btn = Button(main,text="your msg to bot",font=('monospace',12),command = ask_here)
btn.pack()

main.mainloop()
