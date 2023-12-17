from tkinter import *
import re
import operator

last_clicked = ""


def num_clicked(n, cur):
    global last_clicked
    if last_clicked == "calculate":
        last_clicked = "num"
        return n

    last_clicked = "num"

    return cur + n


def operator_clicked(op, cur):
    return cur + " " + op + " "


def clear_clicked():
    return ""


def calculate_clicked(eq):

    parsed = re.search(r"^([\d\.]+) ([\+\-\*\/]){1} ([\d\.]+)$", eq)

    if not parsed:
        return

    operator_lookup = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    operand_1 = float(parsed.group(1))
    op = parsed.group(2)
    operand_2 = float(parsed.group(3))

    global last_clicked
    last_clicked = "calculate"

    answer = operator_lookup[op](operand_1, operand_2)

    if answer.is_integer():
        return str(int(answer))

    return answer


def main():
    def num_click(n, output):
        output.configure(text=num_clicked(n, output.cget("text")))

    def operator_click(op, output):
        output.configure(text=operator_clicked(op, output.cget("text")))

    def clear_click():
        output.configure(text=clear_clicked())

    def calculate_click(output):
        output.configure(text=calculate_clicked(output.cget("text")))

    root = Tk()
    root.title("Calculator")

    output = Label(
        root, text="", padx=10, pady=20, borderwidth=5, relief="ridge", anchor=(E)
    )
    output.grid(row=0, column=0, columnspan=4, sticky=(N, E, S, W))

    # Create buttons
    button_1 = Button(
        root, text="1", padx=10, pady=20, command=lambda: num_click("1", output)
    )
    button_2 = Button(
        root, text="2", padx=10, pady=20, command=lambda: num_click("2", output)
    )
    button_3 = Button(
        root, text="3", padx=10, pady=20, command=lambda: num_click("3", output)
    )
    button_4 = Button(
        root, text="4", padx=10, pady=20, command=lambda: num_click("4", output)
    )
    button_5 = Button(
        root, text="5", padx=10, pady=20, command=lambda: num_click("5", output)
    )
    button_6 = Button(
        root, text="6", padx=10, pady=20, command=lambda: num_click("6", output)
    )
    button_7 = Button(
        root, text="7", padx=10, pady=20, command=lambda: num_click("7", output)
    )
    button_8 = Button(
        root, text="8", padx=10, pady=20, command=lambda: num_click("8", output)
    )
    button_9 = Button(
        root, text="9", padx=10, pady=20, command=lambda: num_click("9", output)
    )
    button_0 = Button(
        root, text="0", padx=10, pady=20, command=lambda: num_click("0", output)
    )
    button_dot = Button(
        root, text=".", padx=10, pady=20, command=lambda: num_click(".", output)
    )

    button_add = Button(
        root, text="+", padx=10, pady=20, command=lambda: operator_click("+", output)
    )
    button_subtract = Button(
        root, text="-", padx=10, pady=20, command=lambda: operator_click("-", output)
    )
    button_multiply = Button(
        root, text="*", padx=10, pady=20, command=lambda: operator_click("*", output)
    )
    button_divide = Button(
        root, text="/", padx=10, pady=20, command=lambda: operator_click("/", output)
    )

    button_calculate = Button(
        root, text="=", padx=10, pady=15, command=lambda: calculate_click(output)
    )

    button_clear = Button(
        root, text="C", padx=10, pady=20, command=lambda: clear_click()
    )

    # Place buttons
    button_7.grid(row=1, column=0, sticky=(N, E, S, W))
    button_8.grid(row=1, column=1, sticky=(N, E, S, W))
    button_9.grid(row=1, column=2, sticky=(N, E, S, W))

    button_4.grid(row=2, column=0, sticky=(N, E, S, W))
    button_5.grid(row=2, column=1, sticky=(N, E, S, W))
    button_6.grid(row=2, column=2, sticky=(N, E, S, W))

    button_1.grid(row=3, column=0, sticky=(N, E, S, W))
    button_2.grid(row=3, column=1, sticky=(N, E, S, W))
    button_3.grid(row=3, column=2, sticky=(N, E, S, W))

    button_0.grid(row=4, column=0, sticky=(N, E, S, W))
    button_dot.grid(row=4, column=1, sticky=(N, E, S, W))
    button_clear.grid(row=4, column=2, sticky=(N, E, S, W))

    button_add.grid(row=1, column=3, sticky=(N, E, S, W))
    button_subtract.grid(row=2, column=3, sticky=(N, E, S, W))
    button_multiply.grid(row=3, column=3, sticky=(N, E, S, W))
    button_divide.grid(row=4, column=3, sticky=(N, E, S, W))

    button_calculate.grid(row=5, column=0, columnspan=4, sticky=(N, E, S, W))

    # Experiment with adding expansion info to buttons
    # 4 columns
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)

    # 6 rows

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)

    # Bind keypresses to buttons
    root.bind("1", lambda event: num_click("1", output))
    root.bind("<KP_1>", lambda event: num_click("1", output))

    root.bind("2", lambda event: num_click("2", output))
    root.bind("<KP_2>", lambda event: num_click("2", output))

    root.bind("3", lambda event: num_click("3", output))
    root.bind("<KP_3>", lambda event: num_click("3", output))

    root.bind("4", lambda event: num_click("4", output))
    root.bind("<KP_4>", lambda event: num_click("4", output))

    root.bind("5", lambda event: num_click("5", output))
    root.bind("<KP_5>", lambda event: num_click("5", output))

    root.bind("6", lambda event: num_click("6", output))
    root.bind("<KP_6>", lambda event: num_click("6", output))

    root.bind("7", lambda event: num_click("7", output))
    root.bind("<KP_7>", lambda event: num_click("7", output))

    root.bind("8", lambda event: num_click("8", output))
    root.bind("<KP_8>", lambda event: num_click("8", output))

    root.bind("9", lambda event: num_click("9", output))
    root.bind("<KP_9>", lambda event: num_click("9", output))

    root.bind("0", lambda event: num_click("0", output))
    root.bind("<KP_0>", lambda event: num_click("0", output))

    root.bind("<period>", lambda event: num_click(".", output))
    root.bind("<KP_Decimal>", lambda event: num_click(".", output))

    root.bind("+", lambda event: operator_click("+", output))
    root.bind("<KP_Add>", lambda event: operator_click("+", output))

    root.bind("-", lambda event: operator_click("-", output))
    root.bind("<KP_Subtract>", lambda event: operator_click("-", output))

    root.bind("*", lambda event: operator_click("*", output))
    root.bind("<KP_Multiply>", lambda event: operator_click("*", output))

    root.bind("/", lambda event: operator_click("/", output))
    root.bind("<KP_Divide>", lambda event: operator_click("/", output))

    root.bind("<Return>", lambda event: calculate_click(output))
    root.bind("<KP_Enter>", lambda event: calculate_click(output))
    root.bind("<KP_Equal>", lambda event: calculate_click(output))

    # Start up the main loop
    root.mainloop()


if __name__ == "__main__":
    main()
