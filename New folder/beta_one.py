# no_class_21 - beta june 28, 2018 - 4:20
# black-jack - 21 - tkinter - 
# d.howe - kingston - Canada - June - 2018

# my imports
from tkinter import *
from tkinter import messagebox
import random
import csv   

# My variables
count = 0
col_count = 0
house_col = 0
player_score = 0
house_score = 0

#  functions hit and stay - stay is hit for house
def hit():
    global count
    global col_count
    global player_score
  
    photo=PhotoImage(file=card_names[count])
    show = Button(Main_win,image = photo,)
    show.image = photo
    show.grid(row=0,column=col_count)
    col_count = col_count + 1
    
    if int(card_values[count]) == 1:
        print('Ace, Ace, Ace, yiphee Ace!!')
        answer = messagebox.askyesno("Question","Value Ace as 1 (one)?")
        if answer == False:
            player_score = player_score + 10
            
    player_score = (player_score + int(card_values[count]))
    score.set(str(player_score))
    count = count + 1
    print (player_score)
    
def stay():
    global count
    global house_col
    photo=PhotoImage(file=card_names[count])
    show = Button(Main_win,image = photo)
    show.image = photo
    show.grid(row=1,column=house_col)
    count=count+1
    house_col = house_col + 1

# main tkinter frame
root = Tk()
Main_win = Frame(root).grid(row=0,column=0)


# read in my card file names and values
with open('newfull.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    card_names = []
    card_values = []
    for row in readCSV:
        card_name = row[0]
        card_value = row[1]
        card_names.append(card_name)
        card_values.append(card_value)

# shuffle my deck
deck = list(zip(card_names, card_values))
random.shuffle(deck)
card_names, card_values =zip(*deck)

# label string variable to allow score update in label
score = StringVar()

# start the game with 2 player cards and a 1 house card showing
hit()
hit()
stay()

# house face down card
photo=PhotoImage(file='./back.png')
show = Button(Main_win,image = photo)
show.image = photo
show.grid(row=1,column=1)

# now we need to check scores for 21 and over -
# and play out house cards
# also need betting for game 

# my buttons and labels
HitButt=Button(Main_win, text="Hit", command=hit).grid(column=0, row=3)
Stand=Button(Main_win, text="Stay", command=stay).grid(column=1, row=3)
QuitBut=Button(Main_win, text="Quit", command=root.destroy).grid(column=2, row=3)
Label(Main_win,text="No Class 21" , font=32).grid(row=4,column=2)
Label(Main_win,textvariable=score, font=32).grid(row=5,column=0)

# mainloop
root.mainloop()
