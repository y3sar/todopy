import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.task_list = [];
        self.master = master
        self.pack()
        self.create_widgets();

    def create_task(self):
        self.task_list.append(Task(self.task_text.get(), master=self));
        self.task_text.delete(0, len(self.task_text.get()));

    def create_widgets(self):
        self.task_text = tk.Entry(self);
        self.task_text.pack(side="top");
        self.task_button = tk.Button(self, text="create task", command=lambda: self.create_task());
        self.task_button.pack(side="top");




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
