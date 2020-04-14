from tkinter import *
from tkinter import font as tkFont
import math


def input_num(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def equals():
    global operator
    try:
        evaluate = str(eval(operator))
        operator = evaluate
    except:
        evaluate = "error"
    text_input.set(evaluate)


def clear():
    global operator
    operator = ""
    text_input.set("")


def sqroot():
    global operator
    evaluate = str(math.sqrt(eval(operator)))
    text_input.set(evaluate)
    operator = evaluate


def big():
    global fontSize
    fontSize.configure(size = fontSize.cget('size') + 1)


def small():
    global fontSize
    fontSize.configure(size = fontSize.cget('size') - 1)


if __name__ == "__main__":
    global operator, text_input, fontSize
    calcu = Tk()
    calcu.title("Calculator")
    operator = ""
    text_input = StringVar()
    fontSize = tkFont.Font(size=12)
    
    txtDisplay = Entry(calcu, font=fontSize,
                       textvariable=text_input,
                       bd=10, insertwidth=3, bg="white",
                       justify='right').grid(columnspan=5)
    
    # 7, 8 ,9 1st row
    btn7 = Button(calcu, font=fontSize, padx=16, pady=12,
                  bd=6, fg="black", text="7",
                  command=lambda: input_num(7)).grid(row=1, column=0)
    
    btn8 = Button(calcu, font=fontSize, padx=16, pady=12,
                  bd=6, fg="black", text="8",
                  command=lambda: input_num(8)).grid(row=1, column=1)
    
    btn9 = Button(calcu, font=fontSize, padx=16, pady=12,
                  bd=6, fg="black", text="9",
                  command=lambda: input_num(9)).grid(row=1, column=2)
    
    # 4, 5, 6, 2nd row
    btn4 = Button(calcu, font=fontSize, padx=16, pady=12,
                  bd=6, fg="black", text="4",
                  command=lambda: input_num(4)).grid(row=2, column=0)
    
    btn5 = Button(calcu, font=fontSize, padx=16, pady=12,
                  bd=6, fg="black", text="5",
                  command=lambda: input_num(5)).grid(row=2, column=1)
    
    btn6 = Button(calcu, font=fontSize, padx=16, pady=12,
                  bd=6, fg="black", text="6",
                  command=lambda: input_num(6)).grid(row=2, column=2)
    
    # 1, 2, 3, 3rd row
    btn1 = Button(calcu, font=fontSize, padx=16, pady=12,
                  bd=6, fg="black", text="1",
                  command=lambda: input_num(1)).grid(row=3, column=0)
    
    btn2 = Button(calcu, font=fontSize, padx=16, pady=12,
                  bd=6, fg="black", text="2",
                  command=lambda: input_num(2)).grid(row=3, column=1)
    
    btn3 = Button(calcu, font=fontSize, padx=16, pady=12,
                  bd=6, fg="black", text="3",
                  command=lambda: input_num(3)).grid(row=3, column=2)
    
    # clear, zero, and equals, 4th row
    btn1Clear = Button(calcu, font=fontSize, padx=16, pady=12,
                       bd=6, fg="black", text="C",
                       command=clear).grid(row=4, column=0)
    
    btn0 = Button(calcu, font=fontSize, padx=16, pady=12,
                  bd=6, fg="black", text="0",
                  command=lambda: input_num(0)).grid(row=4, column=1)
    
    btnEquals = Button(calcu, font=fontSize, padx=16, pady=12,
                       bd=6, fg="black", text="=",
                       command=equals).grid(row=4, column=2)
    
    # add, subtract, multiply, divide 3rd column
    btnAdd = Button(calcu, font=fontSize, padx=12, pady=12,
                    bd=6, fg="black", text="+",
                    command=lambda: input_num("+")).grid(row=4, column=3)
    
    btnSub = Button(calcu, font=fontSize, padx=12, pady=12,
                    bd=6, fg="black", text="-",
                    command=lambda: input_num("-")).grid(row=3, column=3)
    
    btnMul = Button(calcu, font=fontSize, padx=12, pady=12,
                    bd=6, fg="black", text="*",
                    command=lambda: input_num("*")).grid(row=2, column=3)
    
    btnDiv = Button(calcu, font=fontSize, padx=12, pady=12,
                    bd=6, fg="black", text="/",
                    command=lambda: input_num("/")).grid(row=1, column=3)

    # increase&decrease size, sqrt
    btnSqrt = Button(calcu, font=fontSize, padx=16, pady=12,
                     bd=6, fg="black", text="√",
                     command=sqroot).grid(row=5, column=0)
    
    btnEnlarge = Button(calcu, font=fontSize, padx=12,pady=12,
                        bd=6, fg="black", text="BIG",
                        command=big).grid(row=5, column=3, columnspan = 1)
    
    btnShrink = Button(calcu, font=fontSize, padx=12, pady=12,
                       bd=6, fg="black", text="SMALL",
                       command=small).grid(row=5, column=1, columnspan = 2)
    calcu.mainloop()
