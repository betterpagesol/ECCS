#!/usr/bin/python3
import os
import math
import datetime
import subprocess
import traceback
import npyscreen
import curses
from gencodes import *
from cryptomodule import *
from xorotp import *
from otp import *

class MainMenuForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.TitleText, name="Main Menu", editable=False)
        self.menu = self.add(npyscreen.MultiLineAction,
                             values=["Option 1", "Option 2", "Option 3"],
                             max_height=5,
                             scroll_exit=True)
        self.menu.actionHighlighted = self.on_select

    def on_select(self, *args, **keywords):
        index = self.menu.cursor_line
        if index == 0:
            self.parentApp.setNextForm("MENU1")
        elif index == 1:
            self.parentApp.setNextForm("MENU2")
        elif index == 2:
            self.parentApp.setNextForm("MENU3")
        self.parentApp.switchFormNow()

class SubMenuForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.TitleText, name="Sub Menu", editable=False)
        self.menu = self.add(npyscreen.MultiLineAction,
                             values=["Sub Option 1", "Sub Option 2", "Sub Option 3"],
                             max_height=5,
                             scroll_exit=True)
        self.menu.actionHighlighted = self.on_select

    def on_select(self, *args, **keywords):
        npyscreen.notify_confirm("You selected: " + self.menu.get_selected_objects()[0])

class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainMenuForm, name="Main Menu")
        self.addForm("MENU1", SubMenuForm, name="Sub Menu 1")
        self.addForm("MENU2", SubMenuForm, name="Sub Menu 2")
        self.addForm("MENU3", SubMenuForm, name="Sub Menu 3")

if __name__ == '__main__':
    app = MyApplication()
    app.run()

