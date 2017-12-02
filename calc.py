from tkinter import *


def main():
    root = Tk()
    root.title("Calc")
    str_result = ""

    def obj(string):
        global str_result
        str_result += string
        Label(text=str_result).grid(row=0, column=0, columnspan=3)

    def clean():
        Label(text="                          ", anchor="w").grid(row=0, column=0, columnspan=3)

    # operation buttons
    def operation(operations):
        if operations is "+" or operations is "-" or operations is "*" or operations is "/":
            global str_result
            str_result += str(operations)
            Label(text=str_result).grid(row=0, column=0, columnspan=3)

        if operations is "=":
            try:
                clean()
                Label(text=str(eval(str_result))).grid(row=0, column=0, columnspan=3)
            except ZeroDivisionError:
                Label(text="Zero division!").grid(row=0, column=0, columnspan=3)
            except SyntaxError:
                Label(text="Syntax?!").grid(row=0, column=0, columnspan=3)

        if operations is "clear":
            str_result = ""
            clean()  # TODO: Place good cleaning.

    # result label
    label = Label(text="", anchor="w").grid(row=0, column=0, columnspan=3)

    # number buttons
    one = Button(text="1", command=lambda: obj("1")).grid(row=1, column=0)
    two = Button(text="2", command=lambda: obj("2")).grid(row=1, column=1)
    three = Button(text="3", command=lambda: obj("3")).grid(row=1, column=2)
    four = Button(text="4", command=lambda: obj("4")).grid(row=2, column=0)
    five = Button(text="5", command=lambda: obj("5")).grid(row=2, column=1)
    six = Button(text="6", command=lambda: obj("6")).grid(row=2, column=2)
    seven = Button(text="7", command=lambda: obj("7")).grid(row=3, column=0)
    eight = Button(text="8", command=lambda: obj("8")).grid(row=3, column=1)
    nine = Button(text="9", command=lambda: obj("9")).grid(row=3, column=2)
    zero = Button(text="0", command=lambda: obj("0")).grid(row=4, column=1)
    dot = Button(text=".", command=lambda: obj(".")).grid(row=4, column=0)

    plus = Button(text="+", command=lambda: operation("+")).grid(row=1, column=3)
    minus = Button(text="-", command=lambda: operation("-")).grid(row=2, column=3)
    div = Button(text="/", command=lambda: operation("/")).grid(row=3, column=3)
    multiplicity = Button(text="*", command=lambda: operation("*")).grid(row=4, column=3)
    equal = Button(text="=", command=lambda: operation("=")).grid(row=4, column=2)

    # system
    clear = Button(text="C", command=lambda: operation("clear")).grid(row=5, column=0, columnspan=3)

    # TODO: Keyboard support
    # TODO: Switch to Text input + focus

    root.mainloop()


if __name__ == '__main__':
    main()



