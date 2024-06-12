import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.shape = None

    def draw(self, event):
        if self.shape:
            self.canvas.delete(self.shape)
        self.end_x = event.x
        self.end_y = event.y
        self.shape = self.canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y, outline="black")

root = tk.Tk()
app = DrawingApp(root)
root.mainloop()
