import tkinter as tk
from Game import Game
from PIL import ImageTk, Image 
import tkinter.messagebox as messagebox
import logging

class App():

    # Creates a Frame for the application and populates the GUI...
    def __init__(self, root):
        
        #for logging
        logging.basicConfig(level=logging.INFO, filename='game.log', filemode='w', 
        format='%(asctime)s - %(levelname)s - %(message)s')

        self.game = Game()

        logging.info('The game has started')

        # Create two frames owned by the window root.
        # In order to use multiple layout managers, the frames
        # cannot share a parent frame. Here both frames are owned
        # by a top level instance root.


        self.frame0 = tk.Frame(root, width=500, height=200, bg='WHITE', borderwidth=2)
        self.frame0.pack_propagate(0)  # Prevents resizing
        self.frame1 = tk.Frame(root, width=500, height=300, bg='WHITE', borderwidth=2)
        self.frame1.pack_propagate(0)  # Prevents resizing
        self.frame2 = tk.Frame(root, width=500, height=100, bg='LIGHT GREY', borderwidth=2)
        self.frame2.grid_propagate(0)  # Prevents resizing

        # This packs both frames into the root window...
        self.frame0.pack()
        self.frame1.pack()
        self.frame2.pack()

        # Now add some useful widgets...
        self.image_area = tk.Label(self.frame0, image=self.game.show_images())
        self.text_area1 = tk.Label(self.frame1, text='',wraplength=420)
        self.text_area1.pack()
        self.cmd_area = tk.Entry(self.frame2, text='')
        self.cmd_area.pack()
        self.text_area2 = tk.Label(self.frame2, text='')
        self.text_area2.pack()

        #Create a menubar and three label 
        self.menubar = tk.Menu(root)
        self.menubar.add_command(label="Help",command=lambda: self.text_area1.config(text = self.help_messagebox()))
        self.menubar.add_command(label="Map",command=self.open_map_popup)
        self.menubar.add_command(label="Quit", command=root.destroy)
        root.config(menu=self.menubar)

        self.name_surname()
        self.build_GUI()

    
    def open_map_popup(self):

        """
            It creates a pop-up to display the map of the game in a pop-up
        :return: None
        """

        logging.info('The player has clicked map pop-up') #for log file

        # Create the pop-up window
        self.popup = tk.Toplevel()
        self.popup.title("Map")
        self.popup.resizable(False, False)

        # Create a label widget to display the map in the pop-up window
        self.img = Image.open("map.png")
        self.img = self.img.resize((400,400),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        label = tk.Label(self.popup, image=self.img)
        label.pack()
        
        # Create a button widget to close the pop-up window
        button = tk.Button(self.popup, text='Close', command=self.popup.destroy)
        button.pack()
        


    def help_messagebox(self):

        """
            It creates a messagebox to display help text in there
        :return: None
        """

        logging.info('The player has clicked help button') #for log file
        messagebox.showinfo("Help", self.game.print_help())


    def name_surname(self):
        
        """
            It creates a button to be clicked after typing the player's name and surname and displays a welcome message!
        :return: None
        """
        self.ns_button = tk.Button(self.frame2, text='Start', fg='black', bg='cyan', command=self.do_name)
        self.ns_button.pack()
        self.text_area1.configure(text=self.game.player_welcome())
        
    
    def build_GUI(self):

        """
            It creates buttons that are used by players to play the game.
        :return: None
        """
        
        self.cmd_button = tk.Button(self.frame2, text='Run command', fg='black', bg='blue', command=lambda: (self.do_command(),self.image_area.config(image=self.game.show_images())))
        self.take_button = tk.Button(self.frame1, text='Take Item', fg='black', bg='yellow',command=lambda: self.text_area1.config(text = self.game.take_command()))
        self.leave_button = tk.Button(self.frame1, text='Leave Item', fg='black', bg='yellow',command=lambda: self.text_area1.config(text = self.game.leave_command()))
        self.open_bag_btn = tk.Button(self.frame1, text='Open Bag', fg='black', bg='yellow',command=lambda: (self.toggle_button(),self.text_area1.config(text = f'Items in your backpack: {self.game.backpack.show_backpack_items()}')))
        self.close_bag_btn = tk.Button(self.frame1, text='Close Bag', state='disabled', fg='black', bg='yellow',command=lambda: (self.toggle_button(),self.text_area1.config(text = self.game.close_bag())))      
        

    

    def toggle_button(self):
        
        """
            This function changes the state of the close bag button.
        :return: None
        """
        if self.close_bag_btn['state'] == 'normal':
            self.close_bag_btn.configure(state='disabled')
        else:
            self.close_bag_btn.configure(state='normal')


    def name_command(self,command):
        """
            Process a command.
        :param command: a 2-tuple of the form (name, surname)
        """
        name, surname = self.get_command_string(command)
        if name != None and surname != None:
            name = name.upper()
            surname = surname.upper()
            self.text_area1.configure(text=self.game.print_welcome(name,surname))
            self.ns_button.pack_forget()
            self.cmd_button.pack()
            self.image_area.pack()
            self.take_button.pack()
            self.leave_button.pack()
            self.open_bag_btn.pack()
            self.close_bag_btn.pack()
            self.take_button.place(x=5, y= 270)
            self.leave_button.place(x=75, y= 270)
            self.open_bag_btn.place(x=350, y= 270)
            self.close_bag_btn.place(x=420, y= 270) 
            self.cmd_area.delete(0,'end')
            self.text_area2.pack_forget()

            return (name,surname)
        elif name == None and surname == None:
            self.text_area2.configure(text="Please, enter your both name and surname!")
        else:
            self.text_area2.configure(text="Please, enter your name and surname with using space!")
    
    
    def do_command(self):
        logging.info('The player has cliked run command button')
        command = self.cmd_area.get()  # Returns a 2-tuple
        logging.info('The player has entered:'+ command)
        self.process_command(command)
        
        
    def do_name(self):
        logging.info('The player has cliked start button')
        name_surname = self.cmd_area.get()
        logging.info('The player has entered:'+ name_surname)
        self.name_command(name_surname)
        return name_surname
        
    
    

    def get_command_string(self, input_line):
        """
            Fetches a command (borrowed from old TextUI).
        :return: a 2-tuple of the form (command_word, second_word)
        """
        word1 = None
        word2 = None
        if input_line != "":
            all_words = input_line.split()
            word1 = all_words[0]
            if len(all_words) > 1:
                word2 = all_words[1]
            else:
                word2 = None
            # Just ignore any other words
        return (word1, word2)


    def process_command(self, command):
        """
            Process a command.
        :param command: a 2-tuple of the form (command_word, second_word)
        """

        command_word, second_word = self.get_command_string(command)
        if command_word != None:
            command_word = command_word.upper()
            second_word = second_word.upper()

            if command_word == "GO":
                self.text_area1.configure(text=self.game.do_go_command(second_word))
            else:
                # Unknown command...
                self.text_area1.configure(text="Don't know what you mean.")
        
    def create_player(self):
        
        """
            Save player's name and surname
        :return:
        """
        self.game.player.add_player(self.do_name())


    

def main():
    win = tk.Tk()                           # Create a window
    win.title("Study at campus with GUI")   # Set window title
    win.geometry("500x600")                 # Set window size
    win.resizable(False, False)             # Both x and y dimensions...
    
    # Create the GUI as a Frame and attach it to the window...
    myApp = App(win)
    

    # Call the GUI mainloop...
    win.mainloop()

    #myApp.destroy(win)

if __name__ == "__main__":
    main()
