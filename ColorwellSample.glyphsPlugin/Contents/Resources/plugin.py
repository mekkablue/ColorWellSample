# encoding: utf-8
from __future__ import division, print_function, unicode_literals

###########################################################################################################
#
#
#	General Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/General%20Plugin
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
from AppKit import NSColorWell

class ColorWellSample(GeneralPlugin):
		
	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({
			'en': 'My Colors',
			'de': 'Meine Farben',
			'fr': 'Mes couleurs',
			'es': 'Mis colores',
			})
	
	@objc.python_method
	def start(self):
		newMenuItem = NSMenuItem(self.name, self.showWindow_)
		Glyphs.menu[EDIT_MENU].append(newMenuItem)

	def showWindow_(self, sender):
		self.colorWell = NSColorWell.alloc().init()
		self.colorWell.activate_(True)
		self.colorWell.addObserver_forKeyPath_options_context_(self, "color", 0, 0)
		# now, whenever self.colorWell.color is changed, the observer will try to call a method
		# called observeValueForKeyPath_ofObject_change_context_() in self (=this ColorWellSample object)

	@objc.python_method
	def __del__(self):
		# bad example, I think this is never called in this sample:
		self.colorWell.deactivate()
		self.colorWell.removeObserver_forKeyPath_(self, "color")
	
	# the method the observer will call:
	def observeValueForKeyPath_ofObject_change_context_(self, keyPath, obj, change, context):
		# brings macro window to front and clears its log:
		Glyphs.clearLog()
		Glyphs.showMacroWindow()
		
		# print all the received data:
		print("COLORWELL\nkeyPath:", keyPath, "\nobject:", obj, "\nchange:", change, "\ncontext:", context)
		# access the color either through the object passed to it:
		print(obj.color())
		# or by accessing the object itself, if it is available to you:
		print(self.colorWell.color())

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	