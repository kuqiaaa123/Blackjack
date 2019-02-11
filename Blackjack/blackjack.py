import tkinter as tk
from tkinter import messagebox
import random
import sys

LARGE_FONT= ("Verdana", 12)
START_FUNDS=1000
funds=1000
win=0
loss=0

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.geometry("330x350")
        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        titleLabel=tk.Label(self,text="Blackjack",bg='green',font=("Arial",12),width=25,height=2)
        titleLabel.place(x=50, y=0)

        playBtn=tk.Button(self,text="1. Play the Game",font=("Arial",12),width=25,height=2,command=lambda: controller.show_frame(PageOne))
        playBtn.place(x=50, y=70)

        displayBtn=tk.Button(self,text="2. Display Availabel Founds",font=("Arial",12),width=25,height=2,command=lambda:self.checkFunds())
        displayBtn.place(x=50, y=125)

        resetBtn=tk.Button(self,text="3. Reset Funds to Zero",font=("Arial",12),width=25,height=2,command=lambda:self.reset())
        resetBtn.place(x=50, y=180)

        quitBtn=tk.Button(self,text="4. Quit",font=("Arial",12),width=25,height=2,command=lambda:quit())
        quitBtn.place(x=50, y=235)

    def checkFunds(self):
        global funds
        tk.messagebox.showinfo(title="Funds",message='Your Funds: ' + str(funds))

    def reset(self):
        global funds
        global win
        global loss
        result = tk.messagebox.askquestion(title="Hi",message='Are you sure?(Y/N)')
        if result=='yes':
            funds=1000
            win=0
            loss=0
            tk.messagebox.showinfo(title="Hi",message='You winnings is reset to zero!')

def quit():
    result = tk.messagebox.askquestion(title="Quit",message='Are you sure?(Y/N)')
    if result=='yes':
        app.destroy()
        

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
 
        self.controller=controller
        self.play()

    def play(self):
        self.firstCardNum=random.randint(1,12)
        self.firstCardSuit=random.randint(1,4)
        self.firstCard=findCard(self.firstCardNum,self.firstCardSuit)

        self.secondCardNum=random.randint(1,12)
        self.secondCardSuit=random.randint(1,4)
        self.secondCard=findCard(self.secondCardNum,self.secondCardSuit)

        self.thirdCardNum=0
        self.thirdCardSuit=0
        self.thirdCard=""

        result=self.checkCard()
        while True:
            if self.firstCard==self.secondCard:
                self.secondCardNum=random.randint(1,12)
                self.secondCardSuit=random.randint(1,4)
                self.secondCard=findCard(self.secondCardNum,self.secondCardSuit)
            else:
                break

            
        
        self.firstCardLabel=tk.Label(self,text="1.  " + self.firstCard,font=("Arial",12),width=25,height=2,)
        self.secondCardLabel=tk.Label(self,text="2.  " + self.secondCard,font=("Arial",12),width=25,height=2,)
        self.thirdCardLabel=tk.Label(self,text="",font=("Arial",12),width=25,height=2,)
        self.playBtn=tk.Button(self,text="Third Card",font=("Arial",12),width=25,height=2,command=self.drawCard)
        self.redrawBtn=tk.Button(self,text="Redraw",font=("Arial",12),width=25,height=2,command=self.reDraw)
        
        self.firstCardLabel.pack()
        self.secondCardLabel.pack()
        self.thirdCardLabel.pack()
        self.playBtn.pack()
        self.redrawBtn.pack()

        self.button1 = tk.Button(self, text="Back to Home",font=("Arial",12),width=25,height=2,
                            command=lambda: controller.show_frame(StartPage))
        self.button1.pack()

    def checkCard(self):
        if self.firstCardNum==self.secondCardNum:
            if(self.fristCardSuit==self.secondCardSuit):
                self.secondCardNum=random.randint(1,12)
                self.secondCardSuit=random.randint(1,4)
                return False
        if self.firstCardNum==self.thirdCardNum:
            if(self.fristCardSuit==self.thirdCardSuit):
                self.thirdCardNum=random.randint(1,12)
                self.thirdCardSuit=random.randint(1,4)
                return False
        if self.secondCardNum==self.thirdCardNum:
            if(self.secondCardNum==self.thirdCardSuit):
                self.thirdCardNum=random.randint(1,12)
                self.thirdCardSuit=random.randint(1,4)
                return False
        return True

    def drawCard(self):
        self.thirdCardNum=random.randint(1,12)
        self.thirdCardSuit=random.randint(1,4)
        self.thirdCard=findCard(self.thirdCardNum,self.thirdCardSuit)
        self.thirdCardLabel.config(text=self.thirdCard)

        while True:
            if self.firstCard==self.thirdCard:
                self.secondCardNum=random.randint(1,12)
                self.secondCardSuit=random.randint(1,4)
                self.thirdCard=findCard(self.thirdCardNum,self.thirdCardSuit)
            else:
                break
            if self.thirdCard==self.secondCard:
                self.thirdCardNum=random.randint(1,12)
                self.thirdCardSuit=random.randint(1,4)
                self.thirdCard=findCard(self.thirdCardNum,self.thirdCardSuit)
            else:
                break
        print(self.firstCardNum)
        print(self.secondCardNum)
        self.checkWin()

    def checkWin(self):
        global funds
        global win
        global loss
        total=0

        if self.firstCardNum>10:
            total=total+10
        else:
            total=total+self.firstCardNum
        if self.secondCardNum>10:
            total=total+10
        else:
            total=total+self.firstCardNum
        if self.thirdCardNum>10:
            total=total+10
        else:
            total=total+self.firstCardNum

        if(self.firstCardNum==1 or self.secondCardNum==1 or self.thirdCardNum==1) and total!=21:
            if total+10==21:
                total=21

        if total==21:
            funds=funds+100
            win=win+1
            tk.messagebox.showinfo(title="Win",message='You Win!')
        else:
            funds=funds-50
            loss=loss+1
            tk.messagebox.showinfo(title="Loss",message='You Loss!')
        print(funds)

        if funds<=0:
            tk.messagebox.showinfo(title="GameOVer",message='GAME OVER--YOU ARE OUT OF FUNDS!')
            self.controller.show_frame(StartPage)
        else:
            self.playAgain()

    def playAgain(self):
        result = tk.messagebox.askquestion(title="Hi",message='Do you want to play again?')
        if result=='yes':
            self.firstCardNum=random.randint(1,12)
            self.firstCardSuit=random.randint(1,4)
            self.firstCard=findCard(self.firstCardNum,self.firstCardSuit)
            self.secondCardNum=random.randint(1,12)
            self.secondCardSuit=random.randint(1,4)
            self.secondCard=findCard(self.secondCardNum,self.secondCardSuit)
            self.firstCardLabel.config(text="1.  " + self.firstCard)
            self.secondCardLabel.config(text="2.  " + self.secondCard)
            self.thirdCardLabel.config(text="")
        else:
            self.firstCardNum=random.randint(1,12)
            self.firstCardSuit=random.randint(1,4)
            self.firstCard=findCard(self.firstCardNum,self.firstCardSuit)
            self.secondCardNum=random.randint(1,12)
            self.secondCardSuit=random.randint(1,4)
            self.secondCard=findCard(self.secondCardNum,self.secondCardSuit)
            self.firstCardLabel.config(text="1.  " + self.firstCard)
            self.secondCardLabel.config(text="2.  " + self.secondCard)
            self.thirdCardLabel.config(text="")
            self.controller.show_frame(StartPage)

    def reDraw(self):
        self.firstCardNum=random.randint(1,12)
        self.firstCardSuit=random.randint(1,4)
        self.firstCard=findCard(self.firstCardNum,self.firstCardSuit)
        self.secondCardNum=random.randint(1,12)
        self.secondCardSuit=random.randint(1,4)
        self.secondCard=findCard(self.secondCardNum,self.secondCardSuit)
        self.firstCardLabel.config(text="1.  " + self.firstCard)
        self.secondCardLabel.config(text="2.  " + self.secondCard)
        self.thirdCardLabel.config(text="")
        
  
        
        
def findCard(num,suits):
         card=""    
         if num==1:
             card="Ace"
         elif num==2:
             card="Two"
         elif num==3:
             card="Three"
         elif num==4:
             card="Four"
         elif num==5:
             card="Five"
         elif num==6:
             card="Six"
         elif num==7:
             card="Seven"
         elif num==8:
             card="Eight"
         elif num==9:
             card="Nine"
         elif num==10:
             card="Ten"
         elif num==11:
             card="Eleven"
         elif num==12:
             card="Twelve"
         elif num==13:
             ard="Thirteen"
         card=card+" of "
         if suits==1:
             card=card+"Spades"
         elif suits==2:
             card=card+"Hearts"
         elif suits==3:
             card=card+"Diamonds"
         elif suits==4:
             card=card+"Clubs"
         return card

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global funds
        global win
        global loss
        fundsString=str(funds)
        label = tk.Label(self, text="Funds: " + fundsString, font=LARGE_FONT)
        label.pack(pady=100,padx=100)

        button1 = tk.Button(self, text="Back to Home",font=("Arial",12),width=25,height=2,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        


app = SeaofBTCapp()

app.mainloop()
