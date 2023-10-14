# encoding: utf-8

###########################################################################################################
#
#
# 	General Plugin
#
# 	Read the docs:
# 	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/General%20Plugin
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *


class MyPluginWithPanelInspector(GeneralPlugin):
    @objc.python_method
    def settings(self):
        self.name = Glyphs.localize(
            {
                "en": "Plugin With Panel Inspector",
                "de": "Plug-in mit Panel Inspector",
            }
        )

    @objc.python_method
    def start(self):
        print("started Plugin with Panel Inspector")

        # newMenuItem = NSMenuItem(self.name, self.showWindow_)
        # Glyphs.menu[EDIT_MENU].append(newMenuItem)

    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
