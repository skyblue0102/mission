#ch10 ex2
import tkinter as tk

size = 1000

x = 10
y = 10
l = 800
window = tk.Tk()
window.title("삼각형 프랙탈")
canvas = tk.Canvas(window, height = size, width=size, bg='white')



canvas.create_polygon(x,y,x+l,y,x*l/2,y-size*(3**1/2)//2, fill='red', outline="red")



canvas.pack()
window.mainloop()




