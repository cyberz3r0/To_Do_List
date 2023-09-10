from tkinter import *
import tkinter as tk
#there are widgets from the ttk library. Online resources may use that
class MyApp:
    def __init__(self,root):
        root.title("My app")
        root.geometry("500x400") # setting up window size
        # root.maxsize(800,600) #max size for width and height respectively 
        frame = Frame(root, width=200, height=100, relief="groove", borderwidth=2) #relief is a border style and borderwidth is straightforward measures in pixel without the px. 
        frame.place(x=0,y=0)

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
        
        #########################################Positioning and Sizing Part 1
        ##import tkinter as tk so we can access tk module
        # label4 = Label(root, text="some text")
        # label5 = Label(root, text="some text")
        # label6 = Label(root, text="some text")
        # label7 = Label(root, text="some text")
        # label4.pack(side=tk.TOP) # if all items are set to TOP they will stack from top to bottom
        # label5.pack(side=tk.BOTTOM) #if all items are set to BOTTOM they will stack from bottom to top
        # label6.pack(side=tk.RIGHT)#if all items are set to RIGHT they will stack from right to left
        # label7.pack(side=tk.LEFT) #if all items are set to LEFT they will stack from left to right
        # # you can add padding(like HTML) in pack() by using padx, for x-axis, and pady, for the y-axis and the measure is in pixels
        # label8 = Label(root, text="some text")
        # label8.pack(side=tk.TOP, padx=10, pady=10)
        
        #####################Part2
        #using place()
        #using place we can use x= and y= to move the widget around in pixel measurement with x=0,y=0 being the top left corner widget_variable.place(x=0, y=0)
        
        ######################Part3
        #using grid() which is the recommended way
        #cells (rows/columns) will take up as much space as the largest widget in it's row
        #elements are automatically centered so we can use sticky which takes a tuple with compass coordinates (ie.N,E,S,W).Diagonals exist too (NE,NW,SE,SW)
        # label9 = Label(root, text="Looooooooooooooooooooong Label")
        # label9["font"] = ("Courier", 48)
        # textbox = Entry(root)
        # button1 = Button(root, text="Press me")
        # label9.grid(column=1, row=1) #top left cell
        # # textbox.grid(column=2, row=1) 
        # button1.grid(column=1,row=2,pady=15,padx=15, sticky=(NE))
        # #if we want the element to take up the entire width we give the tuple 3 parameters, first being the position, and the next two are the width directions(they need to be opposites such as E, W or N, S) 
        # textbox.grid(column=2, row=1, sticky=(N,N,S))
        ####################################### PART4
        # button2 = Button(root, text="Press me", font=('Courier', 24))
        # button2.place(x=0, y=0)
        # button2.configure(width=10,height=1) #width is based on character size plus the width value and height goes up by number of lines
        
        
        ##############################################Part5
        #Frame Widget
        #Frames used to group widget in a structure(divs?) see __init__ for use of Frame
        
        
root = Tk()
MyApp(root)
root.mainloop()