# -*- coding: utf-8 -*-

import     sys
from       PyQt4      import    QtGui,QtCore
from       ui_class   import    Ui_MainWindow
import     json       as        js

#
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
#

class MyUI(Ui_MainWindow):
    def __init__(self):
		super(MyUI, self).__init__()



class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        #self.ui = Ui_MainWindow()
        self.ui                                = MyUI()
        self.ui.setupUi(self)
        
        # Variables to handle state
        self.kabitNo                           = 1
        self.lang                              = u"punjabi"                 
        self.text                              = u"Welcome"
		
        gurdasfile                             = open("GurdasKabit.json")
        read                                   = gurdasfile.read()
        self.jsondata                          = js.loads(read)
        
        # This is a good place to connect signals
        # go on setting up your handlers like:
        # self.ui.okButton.clicked.connect(function_name)
        # etc...

        self.ui.horizontalSlider.setRange(1,675) 
        QtCore.QObject.connect(self.ui.pun_button,       QtCore.SIGNAL(_fromUtf8("clicked()")),            self.pun_button_clicked)
        QtCore.QObject.connect(self.ui.hin_button,       QtCore.SIGNAL(_fromUtf8("clicked()")),            self.hin_button_clicked)
        QtCore.QObject.connect(self.ui.eng_button,       QtCore.SIGNAL(_fromUtf8("clicked()")),            self.eng_button_clicked)
        QtCore.QObject.connect(self.ui.ok_button,        QtCore.SIGNAL(_fromUtf8("clicked()")),            self.ok_button_clicked)
        QtCore.QObject.connect(self.ui.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),    self.slider_updated)
        QtCore.QObject.connect(self.ui.lineEdit,         QtCore.SIGNAL(_fromUtf8("returnPressed()")),      self.update_slider)
        
    def update_slider(self):
		
		self.ui.horizontalSlider.setValue(int(self.ui.lineEdit.text()))
		
		
		self.update()
		pass   
        
    def slider_updated(self,intt):
		
		self.kabitNo = intt
		
		self.ui.lineEdit.setText(unicode(self.kabitNo))
		self.update()
		pass

    def pun_button_clicked(self):
		self.lang = u"punjabi"
		self.update()
		
    def hin_button_clicked(self):
		
		self.lang = u"hindi"
		self.update()
		pass

    def ok_button_clicked(self):
		self.update()
  
    def eng_button_clicked(self):
		self.lang = u"english"
		self.update()
  
    def update(self):
		self.kabitNo = self.ui.lineEdit.text()
		#print "Update Me %s" % self.kabitNo
		Plist=self.GetKabitTextList(self.kabitNo,self.lang)
		#self.textEdit.setWordWrap(true)
		
		if self.lang in ("punjabi","hindi") :
				self.ui.textEdit.setFontPointSize(15)
		# Do something for the word wrap
		self.ui.textEdit.setText(unicode("\n".join(Plist)))
	
    def GetKabitText(self,Number , Language):
        # The line numbers are in a dict so they are not sorted
        # Get then in order
        keys=self.jsondata[0][Number][0].keys()
        sorted = map(lambda x: int(x),keys)
        sorted.sort()
        list = []
        for i in sorted:
             list.append(self.jsondata[0][str(Number)][0][str(i)][0][Language])
        return "\n".join(list)

    def GetKabitTextList(self,Number , Language):
        # The line numbers are in a dict so they are not sorted
        # Get then in order
        keys=self.jsondata[0][unicode(Number)][0].keys()
        sorted = map(lambda x: int(x),keys)
        sorted.sort()
        list = []
        #print sorted
        for i in sorted:
             # check language availabilty in the keys
             languages_available = self.jsondata[0][unicode(Number)][0][unicode(i)][0].keys()
             if Language in languages_available :
                 text = self.jsondata[0][unicode(Number)][0][str(i)][0][Language]
             else:
                 text = "--"
             list.append(text)
      
        return list


# Main Application Code
def main():
    app = QtGui.QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()





