import tkinter as tk
from datetime import datetime


class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.is_24_hour = True
        self.is_running = True
        self.update_job = None

        self.root.title("Digital Clock")
        self.root.geometry("620x330")
        self.root.resizable(False, False)
        self.root.configure(bg="#111827")

        self.clock_label = tk.Label(
            root,
            text="00:00:00",
            font=("Consolas", 64, "bold"),
            bg="#111827",
            fg="#38bdf8",
        )
        self.clock_label.pack(pady=(30, 5))

        self.date_label = tk.Label(
            root,
            text="",
            font=("Segoe UI", 18),
            bg="#111827",
            fg="#d1d5db",
        )
        self.date_label.pack()

        self.format_button = tk.Button(
            root,
            text="Switch to 12-hour",
            command=self.toggle_format,
            font=("Segoe UI", 11, "bold"),
            bg="#1f2937",
            fg="#ffffff",
            activebackground="#374151",
            activeforeground="#ffffff",
            relief="flat",
            padx=15,
            pady=6,
            cursor="hand2",
        )
        self.format_button.pack(pady=(15, 8))

        self.control_button = tk.Button(
            root,
            text="Pause",
            command=self.toggle_clock,
            font=("Segoe UI", 11, "bold"),
            bg="#1f2937",
            fg="#ffffff",
            activebackground="#374151",
            activeforeground="#ffffff",
            relief="flat",
            padx=20,
            pady=6,
            cursor="hand2",
        )
        self.control_button.pack()

        self.update_clock()

    def toggle_format(self):
        self.is_24_hour = not self.is_24_hour

        if self.is_24_hour:
            self.format_button.config(text="Switch to 12-hour")
        else:
            self.format_button.config(text="Switch to 24-hour")

        self.update_display()

    def toggle_clock(self):
        if self.is_running:
            self.is_running = False
            self.control_button.config(text="Resume")

            if self.update_job is not None:
                self.root.after_cancel(self.update_job)
                self.update_job = None
        else:
            self.is_running = True
            self.control_button.config(text="Pause")
            self.update_clock()

    def update_display(self):
        current_time = datetime.now()

        if self.is_24_hour:
            time_format = "%H:%M:%S"
        else:
            time_format = "%I:%M:%S %p"

        self.clock_label.config(
            text=current_time.strftime(time_format)
        )

        self.date_label.config(
            text=current_time.strftime("%A, %d %B %Y")
        )

    def update_clock(self):
        if not self.is_running:
            return

        self.update_display()
        self.update_job = self.root.after(1000, self.update_clock)


def main():
    root = tk.Tk()
    DigitalClock(root)
    root.mainloop()


if __name__ == "__main__":
    main()