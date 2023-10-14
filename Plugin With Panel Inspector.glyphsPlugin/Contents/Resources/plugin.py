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
from vanilla import (
    Window,
    Group,
    TextBox,
)


# Our own patched Vanilla Group class
class PatchedGroup(Group):
    nsViewClass = objc.lookUpClass("GSInspectorView")


class MyPluginWithPanelInspector(GeneralPlugin):
    @objc.python_method
    def settings(self):
        self.name = Glyphs.localize(
            {
                "en": "Plugin With Panel Inspector",
                "de": "Plug-in mit Panel Inspector",
            }
        )

        self.width = 150
        self.height = 180
        self.paletteView = Window((self.width, self.height))
        self.paletteView.group = PatchedGroup(
            (0, 0, self.width, self.height)
        )  # Using PatchedGroup() here instead of Group() (for the inspecotr view)
        self.paletteView.group.label = TextBox(("auto"), "Hello Panel Inspector")

        rules = [
            "H:|-10-[label]-10-|",
            "V:|-5-[label]-5-|",
        ]
        self.paletteView.group.addAutoPosSizeRules(rules)

        # GSCallbackHandler.addCallback_forOperation_(
        #     self, "GSInspectorViewControllersCallback"
        # )
        GSCallbackHandler.addCallback_forOperation_(
            self,
            "GSPanelInspectorsViewControllersCallbackName",
        )

    @objc.python_method
    def start(self):
        pass

    # def inspectorViewControllersForLayer_(self, layer):
    def panelInspectorsForLayer_(self, layer):
        try:
            self.paletteView.group.label.set(layer.name)
        except:
            pass
        if layer and layer.selection:
            self.paletteView.group.label.set(
                [s.__class__.__name__ for s in layer.selection]
            )
            return [self]
        return [self]

    def view(self):
        return self.paletteView.group.getNSView()

    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
