import tkinter as tk
import sys

class Menu():
    def __init__(self,master):

        self.master=master
        self.master.geometry("330x350")
        self.master.title("Blackjack")

        self.titleLabel=self.Label(self,text="Blackjack",bg='green',font=("Arial",12),width=25,height=2)
        self.titleLabel.place(x=50, y=0)

        self.playBtn=tk.Button(self,text="1. Play the Game",font=("Arial",12),width=25,height=2,command=play(root))
        self.playBtn.place(x=50, y=70)

        self.displayBtn=tk.Button(self,text="2. Display Availabel Founds",font=("Arial",12),width=25,height=2)
        self.displayBtn.place(x=50, y=125)
    
        self.resetBtn=tk.Button(self,text="3. Reset Funds to Zero",font=("Arial",12),width=25,height=2)
        self.resetBtn.place(x=50, y=180)

        self.quitBtn=tk.Button(self,text="4. Quit",font=("Arial",12),width=25,height=2)
        self.quitBtn.place(x=50, y=235)

    def playPage(self):
        root2=Toplevel(self.master)
        myPlay=PlayPage(root2)

class PlayPage():
    def __init__(self,master):
        self.master=master
        self.master.geometry("330x350")
        self.master.title("Blackjack")

def main():
    root=tk.Tk()
    myMenu=Menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
