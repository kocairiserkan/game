import logging
"""
    Create a Backpack class with items that can show them and check their weight.
"""
class Backpack:

    def __init__(self):

        """
            Constructor method.
        """

        self.added_items = []
        self.limit = 2800

    def add_item(self,item):
        
        """
            Add item to the backpack.
        :param item: the item that is added
        :return: None
        """

        self.added_items.append(item)

    def check_weight(self):

        """
            Check weight of the backpack.
        :return: total weight
        """

        total = 0 
        for i in self.added_items:
            total += i.weight
        return total 


    def show_backpack_items(self):
        """
            Shows names and weights of items in backpack.
        :return: b_item_
        """
        logging.info('The player has clicked open bag button') #for logging file

        b_item_ = []
        for i in self.added_items:
            b_item_.append([i.name, i.weight])
        if len(b_item_) == 0:
            return f'There is no item in your backpack!'
        else: 
            logging.info('The player has opened the backpack')
            return b_item_