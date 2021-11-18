
# Импортируем нужные модули
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

# Создаём окно и называем его
root = Tk()
root.title("Калькулятор")

# Создаём список с именами будущих кнопок
bttn_list = [
    "7", "8", "9", "+", "*",
    "4", "5", "6", "-", "/",
    "1", "2", "3", "=", "xⁿ",
    "0", ".", "±",  "C",
    "Exit", "π", "sin", "cos",
    "(", ")","n!","√2", ]

# Создаём кнопки
r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

# Создаём поле ввода калькулятора
calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)

# Логика калькулятора
def calc(key):
    global memory
    if key == "=":
# Исключение написания слов или букв
        str1 = "-+0123456789.*/)(" # Только эти символы можно вводить
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "Первый символ не число!")
            messagebox.showerror("Ошибка!", "Вы ввели не число!")
# Исчисления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Ошибка!")
            messagebox.showerror("Ошибка!", "Проверьте корректность введённых данных")

# Очищение поля вводы
    elif key == "C":
        calc_entry.delete(0, END)

# Изменение минуса на плюс и наоборот
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass

# Число пи
    elif key == "π":
        calc_entry.insert(END, math.pi)

# Выход из программы
    elif key == "Exit":
        root.after(1, root.destroy)
        sys.exit

# Возведение в степень
    elif key == "xⁿ":
        calc_entry.insert(END, "**")

# sin и cos
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))

    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))

# Скобки
    elif key == "(":
        calc_entry.insert(END, "(")

    elif key == ")":
        calc_entry.insert(END, ")")

# Вычисление факториала
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))

# Извлечение квадратного корня из числа
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))

# Очищение поля ввода при нажатии на кнопку "="
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

# Закрытие окна tkinter
root.mainloop()
