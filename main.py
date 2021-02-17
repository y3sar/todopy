import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.task_list = [];
        self.master = master
        self.pack()
        for i in range(5):
            self.create_task(str(i))

    def create_task(self, task_text):
        self.task_list.append(Task(task_text, master=self));

    def add_task(self):
        pass


class Task(tk.Frame):
    def __init__(self, task_text, master=None):
        super().__init__(master);
        self.master = master;
        self.pack();
        self.task_text = task_text;
        self.task = tk.Label(self, text=self.task_text);
        self.task.pack();
        self.create_widgets();

    def create_widgets(self):
        self.remove = tk.Button(self, text="remove", command=lambda: self.destroy());
        self.remove.pack(side="right");
        self.done = tk.Button(self, text="done", command=self.change_bg);
        self.done.pack(side="left");

    def change_bg(self):
        self.config(bg="green");
        self.task.config(bg="green");




root = tk.Tk()
root.geometry("500x200");
app = Application(master=root)
app.mainloop()
