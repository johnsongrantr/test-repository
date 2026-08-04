import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Hello World")
    root.geometry("300x120")
    root.resizable(False, False)

    label = tk.Label(root, text="Hello, World!", font=("Arial", 14))
    label.pack(pady=15)

    ok_button = tk.Button(root, text="OK", width=10, command=root.destroy)
    ok_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
