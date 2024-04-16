import tkinter as tk
from tkinter import ttk


def say_hello():
    print("Hello, Tkinter!")


def main():
    root = tk.Tk()
    root.title("Buttons Example")

    hello_button = tk.Button(root, text="Say Hello", command=say_hello)
    hello_button.pack()
    root.geometry("500x500")

    root.mainloop()


if __name__ == "__main__":
    main()
