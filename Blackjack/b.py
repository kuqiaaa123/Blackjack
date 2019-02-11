from tkinter import *


class Frames(object):

    def __init__(self):
        pass

    def main_frame(self):
        main = Tk()
        main.title('WeatherMe')
        main.geometry('300x100')

        query = StringVar()

        Label(main, text='Enter a city below').pack()
        Entry(main, textvariable=query).pack()
        Button(main, text="Submit", command=self.result_frame).pack()

        main.mainloop()

    def result_frame(self):

        result = Tk()
        result.title('City')
        result.geometry('600x125')

        Button(result, text="OK", command=result.destroy).pack()


        result.mainloop()
