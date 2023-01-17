"""
    Create an Item class which has the name and the weight of the item.
"""
class Item:

    def __init__(self,name,weight):

        """
            Get the name of the item and the weight of the item.
        :param : name (name of the item)
        :param : weight (weight of the item)
        :return : None
        """

        self.name = name
        self.weight = weight
