import tkinter as tk
from datetime import datetime


class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("620x240")
        self.root.resizable(False, False)
        self.root.configure(bg="#111827")

        self.clock_label = tk.Label(
            root,
            text="00:00:00",
            font=("Consolas", 64, "bold"),
            bg="#111827",
            fg="#38bdf8",
        )
        self.clock_label.pack(pady=(35, 5))

        self.date_label = tk.Label(
            root,
            text="",
            font=("Segoe UI", 18),
            bg="#111827",
            fg="#d1d5db",
        )
        self.date_label.pack()

        self.update_clock()

    def update_clock(self):
        current_time = datetime.now()

        self.clock_label.config(
            text=current_time.strftime("%H:%M:%S")
        )

        self.date_label.config(
            text=current_time.strftime("%A, %d %B %Y")
        )

        self.root.after(1000, self.update_clock)


def main():
    root = tk.Tk()
    DigitalClock(root)
    root.mainloop()


if __name__ == "__main__":
    main()
    