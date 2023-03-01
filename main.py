import random
import tkinter
from tkinter import *
import DATABASE
import pandas as pd

root = Tk()
root.geometry('650x530+270+300')
#root.resizable(False, False)


#New class for NODE
class Node(Label):



    def specify(self,  conn = []):   #for adding specific atributes of class
        self.id= random.randint(10,99)
        self.connections = []
        self.X = 100
        self.Y=100
        canvas.create_window(self.X, self.Y, window=self)
        self.bind('<Double-ButtonPress-1>', func=self._change_place)
        self.bind('<Button-3>', func=lambda _ : canvas.unbind('<Motion>'))
        self.bind('<Double-ButtonPress-3>',lambda event: create_connection(event,self.X, self.Y))

        return self

    def __download_a_coords(self, mouse):
        self.place(x=mouse.x, y=mouse.y)
        self.X = mouse.x
        self.Y = mouse.y

    def _change_place(self, event):
        canvas.bind('<Motion>', lambda mouse: self.__download_a_coords(mouse))

        self.bind('<Button-1>', lambda _: canvas.unbind('<Motion>'))

def create_connection(event, x1, y1): #to_this_node,
    canvas.bind('<Motion>', lambda event: canvas.create_line(x1, y1, event.x,event.y,fill='blue', width=1))


def add_new_node(): #создание класса сопряжено с его визуализацией
    unit = Node(canvas, text=square.get('1.0','end-1c')).specify()
    unit.place(x=200, y=200)
    print(DATABASE.DATA)


if __name__ == "__main__":

    # Frame
    square = Text(root,height= 6,width=63,bg='Pink', cursor='plus', highlightbackground='red', highlightthickness=2)
    square.pack(expand=1, fill=X)
    square.place(x=130, y=0)

    # Buttons
    button_add = Button(root, width=15,height=3, text='Добавить\nузел',command=add_new_node)
    button_add.pack(side=LEFT)
    button_add.place(x=0,y=0)

    # Canvas
    canvas = Canvas(root, width=690, height=800, bg='#A98E94' )
    canvas.pack()
    canvas.place(x=0, y=108)
    a=Node(text="Hi")
    print(a.cget("text"))

    root.mainloop()

