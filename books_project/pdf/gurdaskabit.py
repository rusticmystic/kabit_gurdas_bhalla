# Using pyqt for pdf
# -*- coding: utf-8 -*-

from docutils.core import publish_parts
import sys
import json as js

class KabitBook(object):
	"""
	"""	
	gurdasfile = ""
	lang       = [ u"punjabi", u"hindi", u"english", u"roman" ] 
	def __init__(self):
		"""
		"""
		self.gurdasfile   =  open("GurdasKabit.json")
		read              = self.gurdasfile.read()
		#print read
		self.jsondata     = js.loads(read)
		self.language     = self.lang[0]
		pass
	def getKabitText(self,num):
		"""
		"""
		return "\n".join(self.__getKabitList(num))
		pass
	def getKabitHTML(self,num):
		html= self.__generate_html_code_(self.__getKabitList(num),num)
		return html
		pass
	def setLanguage(self, lang=0):
		self.language = self.lang[count]
		pass
	def __getKabitList(self, num):
		if num not in range(1,676):
			return ["Oops","Valid Kabit Numbers : 1 to 675"]
			
		keys=self.jsondata[0][str(num)][0].keys()
		sorted = map(lambda x: int(x),keys)
		sorted.sort()
		list_ = []
		#print sorted
		for i in sorted:
			# check language availabilty in the keys
			languages_available = self.jsondata[0][str(num)][0][str(i)][0].keys()
			if self.language in languages_available :
				text = self.jsondata[0][str(num)][0][str(i)][0][self.language]
			else:
				text = "--"
			list_.append(text)			
		return list_	
		pass
	def __generate_html_code_(self,Plist, kno):
		#print "\n".join(Plist)
		text2=""
		
		sorath = u"ਸੋਰਠਾ"
		chhand = u"ਛੰਦ"
		dohra  = u"ਦੋਹਰਾ"
		kbit   = u"ਕਬਿਤ"  
			
		text2 = text2 + "\n\n" + " " + str(kno)+ "\n\n"
		flag=0
		for line in Plist:
			#print line
			if kbit in line:
				text2 = text2 +  "\n"
				text2 = text2 + ".. raw:: html" 
				text2 = text2 + "\n\n"
				text2 = text2 + "    " + "<font color=blue>" + line + "</font>"
				text2 = text2 + "\n\n::\n\n"
				flag=1
			elif sorath in line:
				text2 = text2 +  "\n"
				text2 = text2 + ".. raw:: html" 
				text2 = text2 + "\n\n"
				text2 = text2 + "    " + "<font color=blue>" + line + "</font>"
				text2 = text2 + "\n\n::\n\n"
				flag=1
			elif chhand in line:
				text2 = text2 + "\n"
				text2 = text2 + ".. raw:: html"
				text2 = text2 + "\n\n"
				text2 = text2 + "    " + "<font color=blue>" + line + "</font>"
				text2 = text2 + "\n\n::\n\n"
				flag=1
			elif dohra in line:
				text2 = text2 + "\n"
				text2 = text2 + ".. raw:: html"
				text2 = text2 + "\n\n"
				text2 = text2 + "    " + "<font color=blue>" + line + "</font>"
				text2 = text2 + "\n\n::\n\n"
				flag=1
			else:
				if flag==0:
					text2 = text2 + "\n\n::\n\n"
				text2 = text2 + "    " + line +  "\n"
		
		headuni="<meta http-equiv=\"Content-Type\" content=\"text\/html; charset=utf-8\">"
	
		myhtmlbody  = publish_parts(text2, writer_name="html")['html_body']
		
	
		myhtml= headuni + "<body>" + "<font size=3>" + "<div align=\"center\">" + myhtmlbody + "</div>"  + "</font>" + "</body>"
	
		# Check if we have to move data to next page
		# Draw the first page removing the pageRect offset due to margins.
		return myhtml
