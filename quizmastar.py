import tkinter
from tkinter import *
import random


questions = [
    "Who is hailed as the father of plastic surgery?",
    "Who is the only person in history to win 2 Nobel prizes?",
    "According to Mahabharat, who among the following was the grandson Bheem ?",
    "Who was fearfully called 'Shershah' by Pakistani Army in 1999 Kargil War ?",
    "How many bones are present in an avg adult human body?",
    "The append Method adds value to the list at the  ?",
    "Who is regarded as the inventor of Television?",
    "Which of the following has lowest energy?",
    "Which of the following keyword is used to create a function in Python ?",
    "CH3-CH2-Cl+AgCN=?",
]

answers_choice = [
    ["Dr James lynn","Shushrut","Harry Parker","Saraka",],
    ["Neils Bohr","Richard Feyman","Marie Curie","Pierre Curie",],
    ["Barbarik","Parikshit","Ghatothkach","Babruvahan",],
    ["Capt. Sourabh Kalia","PVC Subedar Yogendra Yadav","PVC Capt.Vikram batra","General Bipin Rawat",],
    ["234","216","312","206",],
    ["custom location","end","center","beginning",],
    ["James Groggins","Sameul Colt","Derek Mueller","Philo Farnsworth",],
    ["Pn band","Conduction band","Valence band","Pn junction",],
    ["function","void","fun","def",],
    ["CH3-CH2-COOH","CH3-CH2-CHO","CH3-CH2-CN","CH3-CH2-NC",],
] 

answers = [1,2,0,2,3,1,3,2,3,3] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Are Excellent !!")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better !!")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Should Work Hard !!")


def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()
    




def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title("Quizmaster")
root.geometry("800x1000")
root.config(background="#ffffff")
root.resizable(0,0)


img1 = PhotoImage(file="t.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Quizmaster",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

lblRules = Label(
    root,
    text = "This quiz contains 10 questions\nOnce you select a radio button that will be a final choice\nhence think before you select",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()

root.mainloop()
