# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 21:48:55 2022

@author: shant
"""

#This code is just for Demo Purpose
#No copyright

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
 
root= tk.Tk()
  
canvas1 = tk.Canvas(root, width = 800, height = 300)
canvas1.pack()

label1 = tk.Label(root, text='Chart Drawer')
label1.config(font=('Arial', 25))
canvas1.create_window(400, 50, window=label1)
   

entry1 = tk.Entry (root)
canvas1.create_window(400, 100, window=entry1)

label2 = tk.Label(root, text='Initial_data_1')
label2.config(font=('Arial', 10))
canvas1.create_window(300, 100, window=label2) 
  

entry2 = tk.Entry (root)
canvas1.create_window(400, 120, window=entry2) 
label3 = tk.Label(root, text='Initial_data_2')
label3.config(font=('Arial', 10))
canvas1.create_window(300, 120, window=label3)
   
      
entry3 = tk.Entry (root)
canvas1.create_window(400, 140, window=entry3) 
label4 = tk.Label(root, text='Final')
label4.config(font=('Arial', 10))
canvas1.create_window(300, 140, window=label4) 
  
def create_charts():
    global x1
    global x2
    global x3
    global bar1
    global pie2
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    x3 = float(entry3.get())

    figure1 = Figure(figsize=(4,3), dpi=100) 
    subplot1 = figure1.add_subplot(111) 
    xAxis = [float(x1),float(x2),float(x3)] 
    yAxis = [float(x1),float(x2),float(x3)] 
    subplot1.bar(xAxis,yAxis, color = 'green') 
    bar1 = FigureCanvasTkAgg(figure1, root) 
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=0)
      
    figure2 = Figure(figsize=(4,3), dpi=100) 
    subplot2 = figure2.add_subplot(111) 
    labels2 = 'Label1', 'Label2', 'Label3' 
    pieSizes = [float(x1),float(x2),float(x3)]
    my_colors2 = ['green','tomato','cyan']
    explode2 = (0, 0.1, 0)  
    subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90) 
    subplot2.axis('equal')  
    pie2 = FigureCanvasTkAgg(figure2, root)
    pie2.get_tk_widget().pack()

def clear_charts():
    bar1.get_tk_widget().pack_forget()
    pie2.get_tk_widget().pack_forget()
            
button1 = tk.Button (root, text=' Create',command=create_charts, bg='palegreen', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 180, window=button1)

button2 = tk.Button (root, text='  Clear', command=clear_charts, bg='lightskyblue', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 220, window=button2)

button3 = tk.Button (root, text='Exit', command=root.destroy, bg='lightsteelblue', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 260, window=button3)
 
root.mainloop()