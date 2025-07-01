#1
import calendar

c = calendar.TextCalendar()
m = c.formatmonth(2021,2)

print(m)

#2
import tkinter as tk

s = "Life is short\nUse Python"

# root = tk.Tk()
# t = tk.Text(root, height=2, width=13)
# t.insert(tk.END, s)
# t.pack()
# tk.mainloop()

#3
root2 = tk.Tk()
t2 = tk.Text(root2, height=6, width=20)
t2.insert(tk.END, m)
t2.pack()
tk.mainloop()