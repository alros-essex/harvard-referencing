import sys,os
import curses

from enum import Enum
from .collection import Collection
from .reference import BookReference, Reference, ReferenceType
from .storage import Storage

class Color(Enum):
  MENU_SELECT = 1
  MENU_NORMAL = 2
  WINDOW = 3
  WINDOW_INPUT = 4
  WINDOW_TITLE = 5
  WINDOW_ITALIC = 6

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
    self.__loop()

  def __loop(self):
    key_pressed = 0
    self.__setup_colors()
    while (key_pressed != ord(Shortcut.QUIT.value)):
      self.__reset_screen()

      if(self.state == State.NO_ACTIVE_COLLECTION):
        if(key_pressed == ord(Shortcut.NEW_COLLECTION.value)):
          collection = self.__create_new_collection()
          self.storage.insert_collection(collection)
          self.__set_active_collection(collection)
          self.__reset_screen()
        elif(key_pressed == ord(Shortcut.OPEN_COLLECTION.value)):
          #TODO
          pass
        
      elif(self.state == State.ACTIVE_COLLECTION):
        self.__show_active_collection()
        if(key_pressed == ord(Shortcut.ADD_NEW_REFERENCE.value)):
          reference = self.__create_new_reference()
          self.__add_reference(reference)
          self.__reset_screen()
      key_pressed = self.stdscr.getch()

    curses.endwin()

  # menu functions

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

  # end menu functions

  # windows

  def __create_new_collection(self) -> Collection:
    input_size = 30
    window_max_x = 49
    # header
    j, i = self.__print("", (3, 2), Color.WINDOW, min_width = window_max_x)
    j, i = self.__print(" New collection", (j+1, 2), Color.WINDOW_TITLE, min_width = window_max_x)
    j, i = self.__print("", (j+1, 2), Color.WINDOW, min_width = window_max_x)
    # name
    j, i = self.__print(" Name       : ", (j+1, 2), Color.WINDOW)
    coords_input_name = j, i
    j, i = self.__print(" "*(input_size+1), (j, i), Color.WINDOW_INPUT)
    j, i = self.__print("", (j, i), Color.WINDOW, min_width = window_max_x)
    # description
    j, i =  self.__print("", (j+1, 2), Color.WINDOW, min_width = window_max_x)
    j, i = self.__print(" Description: ", (j+1, 2), Color.WINDOW)
    coords_input_description = j, i
    j, i = self.__print(" "*(input_size+1), (j, i), Color.WINDOW_INPUT)
    j, i = self.__print("", (j, i), Color.WINDOW, min_width = window_max_x)
    # footer
    _, _ = self.__print("", (j+1, 2), Color.WINDOW, min_width = window_max_x)
    # get input
    name = self.__get_input(coords_input_name, input_size, Color.WINDOW_INPUT)
    description = self.__get_input(coords_input_description, input_size, Color.WINDOW_INPUT)
    return Collection(name = name, description = description)

  def __show_active_collection(self) -> None:
    window_size = 77
    j, i = self.__print("", (3, 2), Color.WINDOW, min_width = window_size)
    j, i = self.__print(" "+self.active_collection.name, (j+1, 2), Color.WINDOW_TITLE, min_width = window_size)
    j, i = self.__print("", (j+1, 2), Color.WINDOW, min_width = window_size)
    for reference in self.active_references:
      first_part, title, second_part = reference.format_console().split("_")
      j, i = self.__print(" "+first_part, (j+1, 2), Color.WINDOW, max_width=window_size-1)
      j, i = self.__print(" "+title, (j, i), Color.WINDOW_ITALIC, max_width=window_size-1)
      j, i = self.__print(" "+second_part, (j, i), Color.WINDOW, max_width=window_size-1, min_width = window_size)
      j, i = self.__print("", (j+1, 2), Color.WINDOW, min_width = window_size)

  def __create_new_reference(self) -> None:
    window_size = 77
    input_size = 30
    oriz_offset = 2
    vert_offset = 3
    self.__hide_cursor()
    # header
    j, i = self.__print("", (vert_offset, oriz_offset), Color.WINDOW, min_width = window_size)
    j, i = self.__print(" New reference", (vert_offset+1, oriz_offset), Color.WINDOW_TITLE, min_width = window_size)
    j, i = self.__print("", (vert_offset+1, i), Color.WINDOW, min_width = window_size)
    j, i = self.__print("", (vert_offset+2, oriz_offset), Color.WINDOW, min_width = window_size)
    # fields
    coord_input_type        = self.__add_line_with_input("Type       ", (vert_offset+ 3, oriz_offset), input_size, window_size)
    coord_input_authors     = self.__add_line_with_input("Authors    ", (vert_offset+ 4, oriz_offset), input_size, window_size)
    coord_input_year        = self.__add_line_with_input("Year       ", (vert_offset+ 5, oriz_offset), input_size, window_size)
    coord_input_title       = self.__add_line_with_input("Title      ", (vert_offset+ 6, oriz_offset), input_size, window_size)
    coord_input_volume      = self.__add_line_with_input("Volume     ", (vert_offset+ 7, oriz_offset), input_size, window_size)
    coord_input_edition     = self.__add_line_with_input("Edition    ", (vert_offset+ 8, oriz_offset), input_size, window_size)
    coord_input_place       = self.__add_line_with_input("Place      ", (vert_offset+ 9, oriz_offset), input_size, window_size)
    coord_input_publisher   = self.__add_line_with_input("Publisher  ", (vert_offset+10, oriz_offset), input_size, window_size)
    coord_input_url         = self.__add_line_with_input("Url        ", (vert_offset+11, oriz_offset), input_size, window_size)
    coord_input_last_access = self.__add_line_with_input("Last Access", (vert_offset+12, oriz_offset), input_size, window_size)
    # footer
    j, i = self.__print("", (vert_offset+12, oriz_offset), Color.WINDOW, min_width = window_size)
    # get imputs
    type = self.__get_multiple_choice_input(coord_input_type, input_size, Color.WINDOW_INPUT, ReferenceType.list())
    authors = self.__get_input(coord_input_authors, input_size, Color.WINDOW_INPUT)
    year = self.__get_input(coord_input_year, input_size, Color.WINDOW_INPUT)
    title = self.__get_input(coord_input_title, input_size, Color.WINDOW_INPUT)
    volume = self.__get_input(coord_input_volume, input_size, Color.WINDOW_INPUT)
    edition = self.__get_input(coord_input_edition, input_size, Color.WINDOW_INPUT)
    place = self.__get_input(coord_input_place, input_size, Color.WINDOW_INPUT)
    publisher = self.__get_input(coord_input_publisher, input_size, Color.WINDOW_INPUT)
    url = self.__get_input(coord_input_url, input_size, Color.WINDOW_INPUT)
    last_access = self.__get_input(coord_input_last_access, input_size, Color.WINDOW_INPUT)
    return BookReference(authors,year,title,place,publisher,volume,edition)

  # end

  def __add_line_with_input(self, label: str, position: tuple, input_size: int, expected_width: int) -> tuple:
    j, i = self.__print(" {label}: ".format(label=label), (position[0], position[1]), Color.WINDOW)
    coords = j, i
    j, i = self.__print(" "*(input_size+1), (j, i), Color.WINDOW_INPUT)
    j, i = self.__print("", (j, i), Color.WINDOW, min_width = expected_width)
    return coords

  # utility functions

  def __set_active_collection(self, collection: Collection) -> None:
    self.active_collection = collection
    self.state = State.NO_ACTIVE_COLLECTION if collection is None else State.ACTIVE_COLLECTION
    tmp = self.storage.select_references_by_collection(collection)
    self.active_references = tmp

  def __add_reference(self, reference: Reference) -> None:
    self.storage.insert_reference(self.active_collection,reference)
    self.__set_active_collection(self.storage.select_collection_by_name(self.active_collection.name))

  def __setup_colors(self):
    curses.start_color()
    curses.init_pair(Color.MENU_SELECT.value, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(Color.MENU_NORMAL.value, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(Color.WINDOW.value, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(Color.WINDOW_INPUT.value, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(Color.WINDOW_TITLE.value, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(Color.WINDOW_ITALIC.value, curses.COLOR_GREEN, curses.COLOR_WHITE)

  def __reset_screen(self):
    self.stdscr.clear()
    self.stdscr.refresh()
    self.__render_top_menu()
    self.__hide_cursor()
    self.stdscr.refresh()
    if(self.state==State.ACTIVE_COLLECTION):
      self.__show_active_collection()

  def __get_input(self, position: tuple, max_len:int, color: Color) -> str:
    input = ""
    key_pressed = 0
    while(not self.__is_return_key(key_pressed)):
      if(len(input)<max_len and key_pressed != 0):
        tmp = input + chr(key_pressed)
        if(tmp.isprintable()):
          input=tmp
      j, i = self.__print(input, position , color)
      self.__show_cursor((position[0],position[1]+len(input)))
      self.stdscr.refresh()
      key_pressed = self.stdscr.getch()
    return input

  def __get_multiple_choice_input(self, position: tuple, max_len:int, color: Color, types) -> str:
    key_pressed = 0
    selected = 0
    while(not self.__is_return_key(key_pressed)):
      if(key_pressed == curses.KEY_UP and selected > 0):
        selected-=1
      elif(key_pressed == curses.KEY_DOWN and selected < len(types)-1):
        selected+=1
      self.__print(types[selected], position, color, min_width = position[0]+max_len)
      self.__hide_cursor()
      self.stdscr.refresh()
      key_pressed = self.stdscr.getch()
    return types[selected]
    
  def __print(self, text: str, position: tuple, color: Color, options: int = 0, max_width: int = None, min_width: int = None) -> tuple:
    settings = self.__color(color) | options
    self.stdscr.attron(settings)
    if(max_width is not None):
      gap = position[1]+len(text)+1-max_width
      if(gap > 0):
        text = text[0:len(text)-gap-3]+"..."
    if(min_width is not None and len(text)<min_width):
      text = text + " "*(min_width-len(text)-position[1])
    
    try:
      self.stdscr.addstr(position[0], position[1], text)
    except curses.error:
      pass

    self.stdscr.attroff(settings)
    return position[0], position[1] + len(text)

  def __color(self, color: Color) -> int:
    return curses.color_pair(color.value)

  def __is_return_key(self, key_pressed: int) -> bool:
    return key_pressed == curses.KEY_ENTER or key_pressed == 10 or key_pressed == 13

  def __hide_cursor(self) -> None:
    curses.curs_set(0)

  def __show_cursor(self, position: tuple) -> None:
    curses.curs_set(1)
    self.stdscr.move(position[0], position[1])

def main():
    curses.wrapper(GUI().draw)