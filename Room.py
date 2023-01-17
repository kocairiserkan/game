from PIL import ImageTk, Image 

"""
    Create a room described "description". Initially, it has
    no exits. The 'description' is something like 'kitchen' or
    'an open court yard'.
"""

class Room:

    def __init__(self, description):

        """
            Constructor method.
        :param description: Text description for this room
        """

        self.description = description
        self.exits = {}  # Dictionary
        self.all_items = [] #List
        self.all_locks = [] #List
        self.all_images = [] #List

    def set_exit(self, direction, neighbour):
        
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room).
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """

        self.exits[direction] = neighbour
    

    def get_long_description(self):

        """
            Fetch a longer description including available exits.
        :return: text description
        """

        return f'Location: {self.description} \n \
               Exits: {self.get_exits()}'

    def get_last(self):

        """
            Fetch a string saying the game is over.
        :return: last
        """

        last =  'CONGRATULATIONS! \n' \
            'You  found all the necessary items to study! \n' \
                   'GAME IS OVER' 
        return last

    def get_exits(self):

        """
            Fetch all available exits as a list.
        :return: all_exits
        """

        exit = list(self.exits.keys())
        
        all_exits = [i.upper() for i in exit]
        return all_exits

    def get_exit(self, direction):

        """
            Fetch an exit in a specified direction.
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """

        if direction in self.exits:
            return self.exits[direction]
        else:
            return None


    def set_item(self,objects):

        """
            Adds an item for a room. The item is stored as a 
            tuple entry (name, weight) of the list.
        :param objects: The object created in Item.
        :return: None
        """

        self.all_items.append(objects)

    def show_items(self):

        """
            Shows names and weights of item in room.
        :return: strings
        """

        item_ = []
        if not self.all_items:
            return f'There is no item here!'
        else:
            for i in self.all_items:
                item_.append((i.name, i.weight))
            return f"Items here:{item_}"
            

    def set_lock(self,lock=False):

        """
            Define a lock for a room. The lock is stored as a 
            boolean variable.
        :param lock: By default it is false, if it is true, then there is a lock.
        :return: None
        """

        self.all_locks.append(lock)

    def set_image(self,file_path):
        
        """
            Define an image for a room and save it in a list.
        :param file_path: to set an image, it must be typed the path of the image file
        :return: None
        """
        
        self.img = Image.open(file_path)
        self.img = self.img.resize((400,200),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.all_images.append(self.img)
        
    

    