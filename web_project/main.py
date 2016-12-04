# Using pyqt for pdf
# -*- coding: utf-8 -*-

import sys

from docutils.core import publish_parts
import cherrypy as c
from gurdaskabit import KabitBook as kb

class webinterface(object):
	@c.expose
	def __init__(self):
		self.kb = kb()
	def index(self):
		return self.kb.getKabitHTML(1)
	index.exposed = True
	
	@c.expose
	def page(self,count=1):
		#return "Oh"
		return self.kb.getKabitHTML(int(count))
	
c.quickstart(webinterface())
