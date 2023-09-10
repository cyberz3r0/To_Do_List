from tkinter import *
import tkinter as tk

class ToDoItem:
    def __init__(self, name, description):
        self.name = name
        self.description= description

class ToDoListApp:
    def __init__(self,root):
        
        root.title("To Do List")
        
        frame= Frame(root, borderwidth=2, relief="sunken")
        frame.grid(column=1,row=1, sticky=(N,E,S,W))
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)
        
        
        list_label = Label(frame, text="All Items")
        list_label.grid(column=1,row=1,sticky=(S,W))
        self.to_do_items = [
            ToDoItem("iPad", "Apple tablet"), 
            ToDoItem("iPhone", "Apple phone"),
            ToDoItem("iPod", "The OG Apple music player")
            ]
        self.to_do_names = StringVar(value=list(map(lambda item: item.name, self.to_do_items)))
        item_list =Listbox(frame, listvariable=self.to_do_names) 
        item_list.bind("<<ListboxSelect>>", lambda s: self.select_item(item_list.curselection())) 
        item_list.grid(column=1, row=2, sticky=(E, W), rowspan=5)  #rowspan/columnspan is used to have the element span across x number of columns/rows
        
        
        self.selected_description= StringVar()
        selected_description_label = Label(frame,textvariable=self.selected_description,wraplength=200) #word wrap using wraplength which is measured in px
        selected_description_label.grid(column=1,row=7, sticky=(S,E, W))
        
        #Add new item
        new_item_label = Label(frame, text="New Item")
        new_item_label.grid(column=2, row=1, sticky=(S,W))
        
        name_item_label = Label(frame, text="Item name")
        name_item_label.grid(column=2, row=2, sticky=(S,W))
        
        self.item_name = StringVar()
        item_name_entry = Entry(frame, textvariable=self.item_name)
        item_name_entry.grid(column=2, row=3, sticky=(N,E,W))
        
        
        description_label = Label(frame, text="Item description")
        description_label.grid(column=2, row=4, sticky=(S,W))
        
        self.item_description = StringVar()
        description_entry = Entry(frame, textvariable=self.item_description)
        description_entry.grid(column=2, row=5, sticky=(N,E,W))
        
        save_button = Button(frame,text="Save",command=self.save_item)
        save_button.grid(column=2,row=6,sticky=(E))
        
        #for loop to give padding to all children of the frame Object
        for child in frame.winfo_children():
            child.grid_configure(padx=10, pady=5)
        
    def select_item(self, index):
        description_text = self.to_do_items[index[0]].description
        self.selected_description.set(description_text)
        
        
    def save_item(self):
        
        name_variable = self.item_name.get()
        description_variable = self.item_description.get()
        new_item=ToDoItem(name_variable,description_variable)
        self.to_do_items.append(new_item)
        self.to_do_names.set(list(map(lambda item: item.name, self.to_do_items)))
        
        
        # entry = Entry(frame)
        
root = Tk()
ToDoListApp(root)
root.mainloop()
        