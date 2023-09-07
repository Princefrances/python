from tkinter import *
from tkinter import messagebox
from tkinter import ttk

f = ('Times', 14)


def calculate_payroll():
    hours_worked = float(tHours.get())
    position = comboPosition.get()

    positions = {
        "Clerk": 250,
        "Supervisor": 450,
        "Manager": 650
    }

    if position in positions:
        rate_per_hour = positions[position]
        pay = hours_worked * rate_per_hour
        tax = pay * 0.12
        final_pay = pay - tax

        messagebox.showinfo('Payroll Result', f'Final Pay = {final_pay}')
    else:
        messagebox.showerror('Invalid Position', 'Invalid position selected.')


ws = Tk()
ws.title('Payroll Calculator')
ws.geometry('400x300')
ws.config(bg='#5A5A5A')

frame = Frame(
    ws,
    bd=2,
    bg='#e8e4c9',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    frame,
    text="Hours Worked",
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    frame,
    text="Position",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, pady=10)

tHours = Entry(
    frame,
    font=f
)

comboPosition = ttk.Combobox(
    frame,
    values=["Clerk", "Supervisor", "Manager"],
    font=f
)

bCalculate = Button(
    frame,
    width=15,
    text='Calculate Payroll',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=calculate_payroll
)

tHours.grid(row=0, column=1, pady=10, padx=20)
comboPosition.grid(row=1, column=1, pady=10, padx=20)
bCalculate.grid(row=2, column=1, pady=10, padx=20)
frame.place(x=50, y=50)

ws.mainloop()
