# Using pyqt for pdf
# -*- coding: utf-8 -*-

from PyQt4.QtGui import QTextDocument, QPrinter, QApplication, QPainter
from PyQt4.QtCore import QSizeF
from docutils.core import publish_parts
from gurdaskabit import KabitBook as kb
import sys

def main():
	app = QApplication(sys.argv)
	
	# Preparing the pdf
	doc = QTextDocument()
	printer = QPrinter()
	printer.setOutputFileName("KabitGurdas.pdf")
	printer.setOutputFormat(QPrinter.PdfFormat)
	
	# Setting page size as A5
	printer.setPaperSize(QPrinter.A5);
	# page margin
	
	printer.setPageMargins(12, 16, 12, 20, QPrinter.Millimeter)
	doc.setPageSize(QSizeF(printer.pageRect().size()))
	
	painter = QPainter()
	painter.begin( printer )	
	
	# Set poem book and get each poem in pdf
	book = kb()
	
	for KabitNumber in range(1,676):		
		# Add text in html to page
		doc.setHtml(book.getKabitHTML(KabitNumber))
		doc.defaultFont().setPointSize(20)
	
		# A new page
		printer.newPage()
		# Create a QPainter to draw our content    
		doc.drawContents(painter)#,printer.pageRect().translated( -printer.pageRect().x(), -printer.pageRect().y() ))
		#QTextDocument.drawContents(QPainter, QRectF rect=QRectF())
		doc.print_(printer)
	
	# Done.
	painter.end()

main()
