from Room import Room
from Backpack import Backpack
from Item import Item
from Player import Player
import logging

"""
    This class is the main class of the "Adventure World" application. 
    'Adventure World' is a very simple, text based adventure game. Users 
    can walk around some scenery. That's all. It should really be extended 
    to make it more interesting!
    
    To play this game, use the main() method in the AdventureWorldGUI class.

    This main class creates and initialises all the others: it creates all
    rooms, creates the parser and starts the game. It also evaluates and
    executes the commands that the parser returns.
    
    This game is adapted from the 'World of Zuul' by Michael Kolling
    and David J. Barnes. The original was written in Java and has been
    simplified and converted to Python by Kingsley Sage.
    
    This version adds the beginnings of a GUI using Tkinter.
"""

class Game:

    def __init__(self):

        """
            Initialises the game.
        """

        self.create_rooms()
        self.create_items()
        self.current_room = self.corridor
        self.backpack = Backpack()
        self.player = Player()
        
        

    def create_rooms(self):

        """
            Sets up all room assets.
        :return: True
        """

        self.corridor = Room("in the Corridor!")
        self.library = Room("in the Library!")
        self.lab = Room("in the Lab!")
        self.toilet = Room("in the Toilet!")
        self.canteen = Room("in the Canteen!")
        self.common_area = Room("in the Common Area!")
        self.nlp_room = Room("in the Nlp Room!")
        self.python_room = Room("in the Python Room!")
        self.ads_room = Room("in the Ads Room!")
        self.math_room = Room("in the Math Room!")


        self.corridor.set_exit("NORTH", self.common_area)

        self.common_area.set_exit("NORTH", self.library)
        self.common_area.set_exit("SOUTH", self.corridor)
        self.common_area.set_exit("EAST", self.toilet)
        self.common_area.set_exit("WEST", self.canteen)
        
        self.canteen.set_exit("NORTH", self.math_room)
        self.canteen.set_exit("EAST", self.common_area)

        self.math_room.set_exit("NORTH", self.lab)
        self.math_room.set_exit("SOUTH", self.canteen)
        self.math_room.set_exit("EAST", self.library)

        self.lab.set_exit("SOUTH", self.math_room)
        self.lab.set_exit("EAST", self.python_room)

        self.python_room.set_exit("SOUTH", self.library)
        self.python_room.set_exit("EAST", self.ads_room)
        self.python_room.set_exit("WEST", self.lab)

        self.library.set_exit("NORTH",self.python_room)
        self.library.set_exit("SOUTH",self.common_area)
        self.library.set_exit("EAST",self.nlp_room)
        self.library.set_exit("WEST",self.math_room)
        self.library.set_lock(lock=True)

        self.nlp_room.set_exit("NORTH",self.ads_room)
        self.nlp_room.set_exit("SOUTH",self.toilet)
        self.nlp_room.set_exit("WEST",self.library)

        self.ads_room.set_exit("SOUTH",self.nlp_room)
        self.ads_room.set_exit("WEST",self.python_room)

        self.toilet.set_exit("NORTH",self.nlp_room)
        self.toilet.set_exit("WEST",self.common_area)

        self.ads_room.set_image("ads.jpg")
        self.canteen.set_image("canteen.jpg")
        self.common_area.set_image("common_area.jpg")
        self.corridor.set_image("corridor.jpg")
        self.lab.set_image("lab.jpg")
        self.library.set_image("library.jpg")
        self.math_room.set_image("math.jpg")
        self.nlp_room.set_image("nlp.jpg")
        self.python_room.set_image("python.jpg")
        self.toilet.set_image("toilet.jpg")
        self.ads_room.set_image("ads.jpg")

        return True

    def create_items(self):

        """
            Sets up all item assets.
        :return: True
        """

        self.pc = Item("Personal Computer",2000)
        self.oop_notes = Item("OOP Notes", 150)
        self.tc_notes = Item("Time Complexity Notes",100)
        self.matrix_notes = Item("Matrix Notes", 50)
        self.nb_notes = Item("Naive Bayes Notes",150)
        self.snacks = Item("Snacks",250)
        self.library_key = Item("Library Key",25)
        
        self.lab.set_item(self.pc)
        self.python_room.set_item(self.oop_notes)
        self.nlp_room.set_item(self.nb_notes)
        self.ads_room.set_item(self.tc_notes)
        self.math_room.set_item(self.matrix_notes)
        self.canteen.set_item(self.snacks)
        self.common_area.set_item(self.library_key)

        return True

    def player_welcome(self):

        """
            Return the welcome message as a string.
        :return: string
        """

        self.welcome = \
        f'WELCOME! \n \
Please enter your name and surname to start playing!'

        return self.welcome

    def print_welcome(self,name,surname):

        """
            Return the welcome message as a string.
        :param name: the name typed by the user
        :param surname: the surname typed by the user
        :return: message
        """

        self.name = name
        self.surname = surname
        self.message = \
        f'WELCOME! {self.name} {self.surname} \n You are at your campus. You are alone. You have to \n \
        find related  notes to study your exams. \n\n \
        Your {self.current_room.get_long_description()} \n\n \
        Your command word is: {self.show_command_words()}'

        return self.message

    def show_command_words(self):

        """
            Show a list of available commands.
        :return: the command as a string
        """

        return  'GO'

    def print_help(self):

        """
            Display some useful help text.
        :return: msg
        """

        self.msg = \
        f'     NEED A HELP! \n \
    You are at your campus. You are all alone. You have to \n \
    find related  notes to study your exams. \n\n \
    Your command word is -> {self.show_command_words()}'

        return self.msg

    def opposite(self, second_word):

        """
            Performs the GO command.
        :param second_word: the direction the player wishes to travel in
        :return: opposite of the param
        """

        if second_word == "NORTH":
            second_word = "SOUTH"
        elif second_word == "SOUTH":
            second_word = "NORTH"
        elif second_word == "WEST":
            second_word = "EAST"
        else:
            second_word = "WEST"
        return second_word   
    
    
    
    
    def do_go_command(self, second_word):

        """
            Performs the GO command.
        :param second_word: the direction the player wishes to travel in
        :return: text output
        """

        if second_word == None:
            # Missing second word...
            return 'Go where?(north,south,east,west)'
        
        if second_word == 'SOUTH' or second_word == 'NORTH' or second_word == 'WEST' or second_word == 'EAST':
            next_room = self.current_room.get_exit(second_word)
            if next_room == None:
                return 'There is no door!'
            else:
                self.current_room = next_room
                if self.show_locks() == True: #checks whether the door is locked or not
                    if self.library_key in self.show_backpack_objects() and self.matrix_notes in self.show_backpack_objects() and self.oop_notes in self.show_backpack_objects() and self.tc_notes in self.show_backpack_objects() and self.nb_notes in self.show_backpack_objects() and self.pc in self.show_backpack_objects(): #if the player has all of these items in his/her backpack, the game is over
                        return f'{self.current_room.get_last()} ' 
                    if self.library_key in self.show_backpack_objects(): #the player can enter the library, if librar_key is in backpack
                        return f'{self.current_room.get_long_description()} \n {self.current_room.show_items()}'
                    else: #otherwise he stays where he is
                        self.current_room = self.current_room.get_exit(self.opposite(second_word)) 
                        lock = f"The room you try to enter has a key so, you can't enter the room without the key\n" \
                        f'{self.current_room.get_long_description()} \n {self.current_room.show_items()}'
                    
                        return lock  
                else:
                    return f'{self.current_room.get_long_description()} \n {self.current_room.show_items()}'
        else:
            return f'You should type one of these words correctly after go ->(north,south,east,west)'

        
    def show_weights(self):

        """
            Shows weight of item in classroom.
        :return item_weight:
        """
        item_weight = 0 
        for i in self.current_room.all_items:
            if not self.current_room.all_items:
                return item_weight
            else:
                item_weight = i.weight
        return item_weight

    def show_objects(self):

        """
            Shows object of item in classrooms.
        :return objects:
        """

        objects = ""
        if not self.current_room.all_items:
            return f'There is no item to be taken!'
        else:
            for i in self.current_room.all_items:
                objects = i
            return objects

    def take_command(self):

        """
            Takes items when it is called.
        :return strings:
        """

        logging.info('The player has clicked take item button') #for log file
        if self.show_weights() == 0:
                return f'There is no item to be taken!'
        else:
            if self.backpack.check_weight() < self.backpack.limit and self.backpack.check_weight() + self.show_weights() <= self.backpack.limit:
                self.backpack.add_item(self.show_objects())
                a = self.current_room.show_items()
                self.current_room.all_items.remove(self.show_objects())

                return f'The first element of {a} taken and added your backpack!'
            else:
                return f'You can"t add this item to your backpack because it"s too heavy to carry.'
        

    def leave_command(self):

        """
            Leaves items when it called
        :return strings:
        """

        logging.info('The player has clicked leave item button') #for log file
        if len(self.backpack.added_items) == 0:
            return f'There is nothing to leave in your backpack!'
               
        else:
            if self.current_room == self.library and self.library_key == self.backpack.added_items[0]:
                return f'You cannot leave the library key here!'
            else:
                self.current_room.set_item(self.backpack.added_items[0])
                x = self.backpack.show_backpack_items()[0] 
                del self.backpack.added_items[0]

                return f'{x} is deleted:Your current items are:{self.backpack.show_backpack_items()}'

            

    
    def show_backpack_objects(self):

        """
            Shows objects of items in backpack.
        :return b_objects:
        """

        b_objects = []
        if not self.backpack.added_items:
            return b_objects
        else:
            for i in self.backpack.added_items:
                b_objects.append(i)
            return b_objects

    def close_bag(self):

        """
            Closes the bag when it is called
        :return strings:
        """

        logging.info('The player has clicked close bag button')
        return f'{self.current_room.get_long_description()} \n \
        {self.current_room.show_items()}'

    
    def show_locks(self):

        """
            Shows locks of classrooms.
        :return True/False:
        """

        for i in self.current_room.all_locks:
            if i == False:
                return False
            else:
                return True

    def show_images(self):

        """
            Shows images when it is called
        :return image:
        """

        for image in self.current_room.all_images:
            return image