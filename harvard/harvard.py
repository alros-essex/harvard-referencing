from harvard.reference import BookReference, EbookReference, VitalsourceReference
from tkinter import Radiobutton
import PySimpleGUI as sg

from typing import List
from enum import Enum

from PySimpleGUI.PySimpleGUI import Button, Col

from .collection import Collection
from .storage import Storage


class GUI():

  def __init__(self):
    self.storage = Storage()

  def draw(self) -> None:

    layout = [
      [sg.Text("Harvard references")],
      [
        sg.Combo(values=self.__load_collections(),size=(80,10), key='combo-collections'), 
        sg.Button('Load selected', key='load_collection'),
        sg.Button("New collection", key="create_new_collection")]
      ]
    window = sg.Window('Harvard references', layout)

    while True:
      event, values = window.read()
      
      if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

      if event == "create_new_collection":
        self.__create_new_collection()
        window['combo-collections'].update(value='',values=self.storage.select_all_collections())
      elif event == 'load_collection':
        self.__load_collection(values['combo-collections'])

    window.close()

  # windows

  def __create_new_collection(self):
    layout = [
      [sg.Text('Name'), sg.Input(key="new_collection_name")],
      [sg.Text('Description'), sg.Input(key="new_collection_description")],
      [sg.Button('Save', key="save_new_collection")]
    ]
    window = sg.Window('Harvard references - New collection', layout)
    while True:
      event, values = window.read()
      if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
      if event == "save_new_collection":
        self.__save_new_collection(name=values['new_collection_name'], description=values['new_collection_description'])
        window.close()

  def __load_collection(self, collection_name):
    if collection_name == '':
      return
    collection = self.storage.select_collection_by_name(collection_name)
    window = self.__load_collection_window(collection)
    while True:
      event, values = window.read()
      if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
      if event == "add_new_reference":
        self.__add_new_reference(collection)
        window.close()
        window = self.__load_collection_window(collection)

  def __load_collection_window(self, collection: Collection):
    layout = [
      [sg.Text("Collection: "+collection.name)],
      [sg.Text(collection.description)],
      [sg.Button('Add new reference', key="add_new_reference")]
    ]
    references = self.storage.select_references_by_collection(collection)
    for reference in references:
      layout.append([sg.Input(reference.format_console(),disabled=True)])
    return sg.Window('Harvard references - {name}'.format(name=collection.name), layout)

  def __add_new_reference(self, collection: Collection):
    layout = [
      [
        sg.Text('Type'),
        sg.Radio(text='Book', group_id='new_reference_type',key="new_reference_book"),
        sg.Radio(text='Ebook', group_id='new_reference_type',key="new_reference_ebook"),
        sg.Radio(text='Vitalsource', group_id='new_reference_type',key="new_reference_vitalsource")
      ],
      [sg.Text('Authors'),sg.Input(key="new_reference_authors")],
      [sg.Text('Year'),sg.Input(key="new_reference_year")],
      [sg.Text('Title'),sg.Input(key="new_reference_title")],
      [sg.Text('Volume'),sg.Input(key="new_reference_volume")],
      [sg.Text('Edition'),sg.Input(key="new_reference_edition")],
      [sg.Text('Place'),sg.Input(key="new_reference_place")],
      [sg.Text('Publisher'),sg.Input(key="new_reference_publisher")],
      [sg.Text('Url'),sg.Input(key="new_reference_url")],
      [sg.Text('Last access'),sg.Input(key="new_reference_last_access")],
      [sg.Button('Save', key='save_new_reference')]
    ]
    window = sg.Window('Harvar references - New reference', layout)
    while True:
      event, values = window.read()
      if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
      if event == "save_new_reference":
        if values['new_reference_book']:
          reference = BookReference(
            authors=values['new_reference_authors'],
            year = values['new_reference_year'],
            title= values['new_reference_title'],
            place = values['new_reference_place'],
            publisher = values['new_reference_publisher'],
            volume = values['new_reference_volume'],
            edition = values['new_reference_edition']
          )
        elif values['new_reference_ebook']:
          reference = EbookReference(
            authors=values['new_reference_authors'],
            year = values['new_reference_year'],
            title= values['new_reference_title'],
            place = values['new_reference_place'],
            publisher = values['new_reference_publisher'],
            url = values['new_reference_url'],
            last_access = values['new_reference_last_access']
          )
        elif values['new_reference_vitalsource']:
          reference = VitalsourceReference(
            authors=values['new_reference_authors'],
            year = values['new_reference_year'],
            title= values['new_reference_title'],
            place = values['new_reference_place'],
            publisher = values['new_reference_publisher'],
            last_access = values['new_reference_last_access'],
            edition = values['new_reference_edition']
          )
        self.storage.insert_reference(collection,reference)
        return
  # utilities

  def __load_collections(self) -> List[Collection]:
    return self.storage.select_all_collections()

  def __save_new_collection(self, name, description):
    self.storage.insert_collection(Collection(name, description))


def main():
  GUI().draw()