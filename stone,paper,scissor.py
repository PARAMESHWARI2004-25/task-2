import random 
import tkinter

root = tkinter.Tk()  
root.geometry("400x400") 
root.title("TASK-5")
 
computer_dict = { 
"0":"Rock", 
"1":"Paper", 
"2":"Scissors" 
}
def reset_game(): 
 b1["state"] = "active" 
 b2["state"] = "active" 
 b3["state"] = "active" 
 l1.config(text = "USER") 
 l3.config(text = "DEVICE") 
 l4.config(text = "")

def button_disable(): 
 b1["state"] = "disable" 
 b2["state"] = "disable" 
 b3["state"] = "disable"

def player_rock(): 
    c_v = computer_dict[str(random.randint(0,2))] 
    if c_v == "Rock": 
        match_result = "Tie!" 
    elif c_v=="Scissors": 
        match_result = "USER Wins" 
    else: 
        match_result = "DEVICE Wins" 
    l4.config(text = match_result) 
    l1.config(text = "Rock") 
    l3.config(text = c_v) 
    button_disable() 
 
def player_paper(): 
    c_v = computer_dict[str(random.randint(0, 2))] 
    if c_v == "Paper": 
        match_result = "Tie!" 
    elif c_v=="Scissors": 
        match_result = "DEVICE Wins" 
    else: 
        match_result = "USER Wins" 
    l4.config(text = match_result) 
    l1.config(text = "Paper") 
    l3.config(text = c_v) 
    button_disable() 
 
def player_scissors(): 
    c_v = computer_dict[str(random.randint(0,2))] 
    if c_v == "Rock": 
        match_result = "DEVICE Wins" 
    elif c_v == "Scissors": 
        match_result = "Tie!" 
    else: 
        match_result = "USER Wins" 
    l4.config(text = match_result) 
    l1.config(text = "Scissors") 
    l3.config(text = c_v) 
    button_disable()
tkinter.Label(root, text = 'Choose any one: Rock, Paper, Scissors', font = "Consolas",  fg = "blue").pack(pady = 20)  


frame = tkinter.Frame(root) 
frame.pack() 

l1 = tkinter.Label(frame,  text = "Player", font = 10) 

l2 = tkinter.Label(frame, text = "VS", font = "Consolas") 

l3 = tkinter.Label(frame, text = "Computer", font = 10) 

l1.pack(side = 'left') 
l2.pack(side = 'left') 
l3.pack() 

l4 = tkinter.Label(root, text = "", font = "Consolas", bg = "blue", width = 15 , borderwidth = 2, relief = "solid") 
l4.pack(pady = 20) 

frame1 = tkinter.Frame(root) 
frame1.pack() 

b1 = tkinter.Button(frame1, text = "Rock", font = 8, width = 7, bg = "light blue", command = player_rock) 

b2 = tkinter.Button(frame1, text = "Paper ", font = 8, width = 7, bg = "light blue", command = player_paper) 

b3 = tkinter.Button(frame1, text = "Scissors", font = 8, width = 7, bg = "light blue", command = player_scissors) 

b1.pack(side = 'left', padx = 10) 
b2.pack(side = 'left', padx = 10) 
b3.pack(padx = 10) 

tkinter.Button(root, text = "Reset Game", font = 10, fg = "red", bg = "light grey", command = reset_game).pack(pady = 20) 

root.mainloop()
