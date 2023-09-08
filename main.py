from tkinter import *
import tkinter as tk
#there are widgets from the ttk library. Online resources may use that
class MyApp:
    def __init__(self,root):
        root.title("My app")
        root.geometry("500x400") # setting up window size
        root.maxsize(800,600) #max size for width and height respectively 

        

        # label = Label(root,text="Label Text", bg="red") #bg is background
        # label1 = Label(root,text="Label Text 1")
        # label.pack() # pack just adds widgets from top to bottom by default
        # label1.pack()
        
        ######################################Dictionary method - useful if you want to change 1-2 things
        # label['text'] = "new label text" # you can change values of label via square bracket notation like dictionaries (because it's a dictionary)
        # label["font"] = ("Courier", 40) #Font and size 
        ######################################Configure method - useful if you want to change many things at once       
        # label.configure(text="New label text", font=("Courier", 30)) 
        
        #Entry is a input box
        # entry_text= StringVar() #going about it this way allows us to have drier code because we can bind this to multiple widgets. We change the value in one location for multiple widgets 
        # entry = Entry(root, textvariable=entry_text)
        # label2 = Label(root)
        # # label2.configure(textvariable=entry_text) #when we type into the input box the label text also has the same text
        # label2.pack()
        # entry.pack()
        # entry_text.get() # get the value
        # entry_text.set("some other string") # changes the value 
        
        ######################################Button      
        
        #####Copied from above to complete challenge of changing a label text when button is clicked
            # #By declaring self to a variable you make it globally accessible usually used in function/method 
        
    #     self.entry_text1= StringVar() 
    #     entry1 = Entry(root, textvariable=self.entry_text1)
    #     self.label_text = StringVar()
    #     label3 = Label(root, textvariable=self.label_text)
    #     button = Button(root,text="Press me!", command= self.press_button) # we call the function via dot notation starting with self without () if no parameters
    #     label3.pack()
    #     entry1.pack()
    #     button.pack()
    # def press_button(self):
    #     text = self.entry_text1.get()
    #     self.label_text.set(text)
            
        ########################################################Listbox
        #Default size of list box is 10 rows of items after that it becomes scrollable but you can set height
        
    #     self.list_item_strings = ["Hello","I","am","Sam"]
    #     list_items = StringVar(value=self.list_item_strings)
    #     listbox =Listbox(root, listvariable=list_items) # We can't provide a list into listvariable only a string that is a list. The above code does this
    #     listbox['height'] = 3 # 3 here means 3 rows
    #     listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection())) #curselection returns a tuple with the index in the 0th index and blank in the 1st index
    #     listbox.pack()
        
        
    # def select_item(self, index):
    #     selected_item = self.list_item_strings[index[0]]
    #     print(selected_item)
        
        #########################################Positioning and Sizing
        ##import tkinter as tk so we can access tk module
        label4 = Label(root, text="some text")
        label5 = Label(root, text="some text")
        label6 = Label(root, text="some text")
        label7 = Label(root, text="some text")
        label4.pack(side=tk.TOP) # if all items are set to TOP they will stack from top to bottom
        label5.pack(side=tk.BOTTOM) #if all items are set to BOTTOM they will stack from bottom to top
        label6.pack(side=tk.RIGHT)#if all items are set to RIGHT they will stack from right to left
        label7.pack(side=tk.LEFT) #if all items are set to LEFT they will stack from left to right
        
root = Tk()
MyApp(root)
root.mainloop()