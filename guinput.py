import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Anime Recommender')
label1.config(font=('robotto', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Input your Anime:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)
    
button1 = tk.Button(text='Get your Anime', bg='green', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()