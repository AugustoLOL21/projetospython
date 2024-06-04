import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")

        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Iniciar", command=self.start, width=15)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Parar", command=self.stop, width=15)
        self.stop_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Resetar", command=self.reset, width=15)
        self.reset_button.pack(pady=5)

    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1

            time_str = f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
            self.time_label.config(text=time_str)
            self.root.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        if not self.running:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            self.time_label.config(text="00:00:00")
if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")

        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Iniciar", command=self.start, width=15)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Parar", command=self.stop, width=15)
        self.stop_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Resetar", command=self.reset, width=15)
        self.reset_button.pack(pady=5)

    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1

            time_str = f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
            self.time_label.config(text=time_str)
            self.root.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        if not self.running:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            self.time_label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
