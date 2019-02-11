import tkinter as tk

def main():
    root=tk.Tk()
    root.title("Blackjack")
    root.geometry("330x350")

    titleLabel=tk.Label(root,text="Blackjack",bg='green',font=("Arial",12),width=25,height=2)
    titleLabel.place(x=50, y=0)

    playBtn=tk.Button(root,text="1. Play the Game",font=("Arial",12),width=25,height=2)
    playBtn.place(x=50, y=70)

    displayBtn=tk.Button(root,text="2. Display Availabel Founds",font=("Arial",12),width=25,height=2)
    displayBtn.place(x=50, y=125)

    resetBtn=tk.Button(root,text="3. Reset Funds to Zero",font=("Arial",12),width=25,height=2)
    resetBtn.place(x=50, y=180)

    quitBtn=tk.Button(root,text="4. Quit",font=("Arial",12),width=25,height=2)
    quitBtn.place(x=50, y=235)
    

def play(self):
    window_play=tk.Toplevel(self)
    window_play.title("Blackjack")
    window_play.geometry("330x350")

    firstCard=tk.StringVar()
    secondCard=tk.StringVar()
    thirdCard=tk.StringVar()

    firstCardLabel = tk.Label(window_play, text="1.  " + firstCard.get())
    firstCardLabel.pack(pady=10,padx=10)

root.mainloop()

if __name__ == "__main__":
    main()
