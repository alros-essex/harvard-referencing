import sys,os
import curses

from enum import Enum
from .collection import Collection
from .storage import Storage

class Color(Enum):
  MENU_SELECT = 1
  MENU_NORMAL = 2
  WINDOW = 3
  WINDOW_INPUT = 4
  WINDOW_TITLE = 5

class Shortcut(Enum):
  QUIT = 'q'
  OPEN_COLLECTION = 'o'
  NEW_COLLECTION = 'n'
  CLOSE_COLLECTION = 'c'
  ADD_NEW_REFERENCE = 'a'

class State(Enum):
  NO_ACTIVE_COLLECTION = 1
  CREATING_COLLECTION = 2
  ACTIVE_COLLECTION = 3
  CREATING_REFERENCE = 4

class GUI():

  def draw(self, stdscr):
    self.storage = Storage()
    self.__set_active_collection(None)
    self.stdscr = stdscr
    self.__draw_menu()

  def __draw_menu(self):
    key_pressed = 0
    self.__setup_colors()
    while (key_pressed != ord(Shortcut.QUIT.value)):
      self.__reset_screen()
      self.__render_top_menu()

      if(key_pressed == ord(Shortcut.NEW_COLLECTION.value)):
        collection = self.__create_new_collection()
        self.storage.insert_collection(collection)
        self.__set_active_collection(collection)

      self.stdscr.move(0, 0)
      self.stdscr.refresh()
      key_pressed = self.stdscr.getch()

    curses.endwin()

  def __reset_screen(self):
    self.stdscr.clear()
    self.stdscr.refresh()

  def __setup_colors(self):
    curses.start_color()
    curses.init_pair(Color.MENU_SELECT.value, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(Color.MENU_NORMAL.value, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(Color.WINDOW.value, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(Color.WINDOW_INPUT.value, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(Color.WINDOW_TITLE.value, curses.COLOR_BLUE, curses.COLOR_WHITE)

  def __render_top_menu(self):
    GUI.top_menu_functions[self.state](self)
  
  def __render_top_menu_no_active_collection(self):
    _, width = self.stdscr.getmaxyx()
    _, i = self.__print(Shortcut.QUIT.value.capitalize(), (0, 1), Color.MENU_SELECT)
    _, i = self.__print("uit | ", (0, i), Color.MENU_NORMAL)
    _, i = self.__print(Shortcut.NEW_COLLECTION.value.capitalize(), (0, i), Color.MENU_SELECT)
    _, i = self.__print("ew collection | ", (0, i), Color.MENU_NORMAL)
    _, i = self.__print(Shortcut.OPEN_COLLECTION.value.capitalize(), (0, i), Color.MENU_SELECT)
    _, i = self.__print("pen collection", (0, i), Color.MENU_NORMAL)
    _, i = self.__print(" " * (width - i), (0, i), Color.MENU_NORMAL)

  def __render_top_menu_active_collection(self):
    _, width = self.stdscr.getmaxyx()
    _, i = self.__print(Shortcut.QUIT.value.capitalize(), (0, 1), Color.MENU_SELECT)
    _, i = self.__print("uit | ", (0, i), Color.MENU_NORMAL)
    _, i = self.__print(Shortcut.CLOSE_COLLECTION.value.capitalize(), (0, i), Color.MENU_SELECT)
    _, i = self.__print("lose collection | ", (0, i), Color.MENU_NORMAL)
    _, i = self.__print(Shortcut.ADD_NEW_REFERENCE.value.capitalize(), (0, i), Color.MENU_SELECT)
    _, i = self.__print("dd new reference", (0, i), Color.MENU_NORMAL)
    _, i = self.__print(" " * (width - i), (0, i), Color.MENU_NORMAL)

  top_menu_functions = {
    State.NO_ACTIVE_COLLECTION: __render_top_menu_no_active_collection,
    State.ACTIVE_COLLECTION: __render_top_menu_active_collection
  }

  def __set_active_collection(self, collection) -> None:
    self.active_collection = collection
    self.state = State.NO_ACTIVE_COLLECTION if collection is None else State.ACTIVE_COLLECTION

  def __create_new_collection(self) -> Collection:
    input_size = 30
    window_size = 46
    j, i = self.__print(" "*window_size, (3, 2), Color.WINDOW)
    j, i = self.__print(" New collection"+" "*30, (j+1, 2), Color.WINDOW_TITLE)
    j, i = self.__print(" "*window_size, (j+1, 2), Color.WINDOW)
    j, i = self.__print(" Name       : ", (j+1, 2), Color.WINDOW)
    coords_input_name = j, i
    j, i = self.__print(" "*(input_size+1), (j, i), Color.WINDOW_INPUT)
    j, i = self.__print(" ", (j, i), Color.WINDOW)
    j, i = self.__print(" "*window_size, (j+1, 2), Color.WINDOW)
    j, i = self.__print(" Description: ", (j+1, 2), Color.WINDOW)
    coords_input_description = j, i
    j, i = self.__print(" "*(input_size+1), (j, i), Color.WINDOW_INPUT)
    j, i = self.__print(" ", (j, i), Color.WINDOW)
    _, _ = self.__print(" "*window_size, (j+1, 2), Color.WINDOW)
    name = self.__get_input(coords_input_name, input_size, Color.WINDOW_INPUT)
    description = self.__get_input(coords_input_description, input_size, Color.WINDOW_INPUT)
    return Collection(name = name, description = description)

  def __get_input(self, position: tuple[int, int], max_len:int, color: Color):
    input = ""
    key_pressed = 0
    while(not self.__is_return_key(key_pressed)):
      if(len(input)<max_len and key_pressed != 0):
        tmp = input + chr(key_pressed)
        if(tmp.isprintable()):
          input=tmp
      j, i = self.__print(input, position , color)
      self.stdscr.move(position[0], position[1]+len(input))
      self.stdscr.refresh()
      key_pressed = self.stdscr.getch()
    return input
    
  def __print(self, text: str, position: tuple[int,int], color: Color, options: int = 0) -> tuple[int, int]:
    settings = self.__color(color) | options
    self.stdscr.attron(settings)
    self.stdscr.addstr(position[0], position[1], text)
    self.stdscr.attroff(settings)
    return position[0], position[1] + len(text)

  def __color(self, color: Color) -> int:
    return curses.color_pair(color.value)

  def __is_return_key(self, key_pressed: int) -> bool:
    return key_pressed == curses.KEY_ENTER or key_pressed == 10 or key_pressed == 13

def main():
    curses.wrapper(GUI().draw)