import tkinter as tk

class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Timer")

        self.time_left = 60

        self.timer_label = tk.Label(master, text="")
        self.timer_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.stop_button.pack()

    def start_timer(self):
        self.update_timer()

    def stop_timer(self):
        self.time_left = 0
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text="Time Left: {}".format(self.time_left))
            self.time_left -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's Up!")

def main():
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
