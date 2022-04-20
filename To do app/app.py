from tkinter import * 
root = Tk()
root.title("TO - Do Lists")
# root.geometry("600x400")
list = []
r_index = 4 # Row index begins with 4 for list of tasks
def addTask():   # r_index -> row index
    task = e.get()
    global list
    global r_index
    print("This is " + str(r_index))
    # list = []
    list.append(task)
    e.delete(0, END)
    myLabel = Label(root, text = f"- {task}")
    myLabel.grid(row = r_index, column = 0)
    print(list)
    r_index += 1
    pass
e = Entry(root, width= 100)
e.grid(row = 1, column = 0)
addButton = Button(root,text = "Add Task", command= addTask) 
addButton.grid(row = 2, column = 0)
# clearButton = Button(root,text = "Clear all Tasks", command= clearTask) 
# clearButton.grid(row = 2, column = 0)
myLabel = Label(root, text = "Pending Tasks")
myLabel.grid(row = 3, column = 0)
print(list)
root.mainloop()