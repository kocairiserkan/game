from Game import Game
from Room import Room
from Item import Item
from Backpack import Backpack
from Player import Player
import unittest


class TestItem(unittest.TestCase):
    def setUp(self):
        self.item1 = Item("Item1",10)
    
    def test_item(self):
        self.assertTrue(self.item1)
        

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("in the room1")
        self.room2 = Room("in the room2")
        self.item2 = Item("Mouse and Keyboard",150)
    
    def test_room(self):
        self.room1.set_exit("north",self.room2)
        self.assertEqual(self.room1.exits, {"north": self.room2})

        self.assertEqual(self.room1.get_exits(),['NORTH'])
        self.assertEqual(self.room1.get_exit('north'),self.room2)

        test_var = f'Location: {self.room1.description} \n \
               Exits: {self.room1.get_exits()}'
        self.assertEqual(self.room1.get_long_description(), test_var)

        self.room1.set_item(self.item2)
        test_var_1 = f"Items here:{[('Mouse and Keyboard',150)]}"
        self.assertEqual(self.room1.show_items(),test_var_1)

class TestBackpack(unittest.TestCase):

    def setUp(self):
        self.backpack1 = Backpack()
        self.item = Item("Item",4)
        
    def test_backpack(self):
        self.backpack1.add_item(self.item)
        self.assertEqual(self.backpack1.show_backpack_items(),([["Item", 4]]))

        self.assertEqual(self.backpack1.check_weight(),4)

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_player(self):
        self.player.add_player("serkan kocairi")
        self.assertTrue(self.player)


class TestGame(unittest.TestCase):
    
    def setUp(self):
        import tkinter

        win = tkinter.Tk()
        win.geometry("500x600")
        self.game = Game()
    
    def test_game(self):
        self.assertTrue(self.game.create_rooms())
        self.assertTrue(self.game.create_items())

        player_welcome = f'WELCOME! \n \
Please enter your name and surname to start playing!'
        self.assertEqual(self.game.player_welcome(),player_welcome)
        
        print_help = f'     NEED A HELP! \n \
    You are at your campus. You are all alone. You have to \n \
    find related  notes to study your exams. \n\n \
    Your command word is -> {self.game.show_command_words()}'
        self.assertEqual(self.game.print_help(),print_help)

        self.assertEqual(self.game.opposite("NORTH"),"SOUTH")
        self.assertEqual(self.game.do_go_command(None),'Go where?(north,south,east,west)')
        self.assertTrue(self.game.show_images)
        self.assertTrue(self.game.show_locks)
