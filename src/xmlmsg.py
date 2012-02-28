import datetime

s_date = datetime.date.today()
aboutmsg="""
<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n
p, li { white-space: pre-wrap; }\n
</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n
<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Gnome-BAXC</span></p>\n
<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"></p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"baxc50.png\" />Version 1.01</p>\n
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Gnome-BAXC </span><span style=\" font-size:11pt;\">(Gnome -</span><span style=\" font-size:11pt; font-weight:600;\">Ba</span><span style=\" font-size:11pt;\">ckground </span><span style=\" font-size:11pt; font-weight:600;\">X</span><span style=\" font-size:11pt;\">ML </span><span style=\" font-size:11pt; font-weight:600;\">C</span><span style=\" font-size:11pt;\">reator) generates xml code for background slide show of gnome.</span></p>\n
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"></p>\n
<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"></p></body></html>
"""
def finalmsg(outfile,count):
	msg = '\n Added '+str(count)+'image(s).\nOutput file:'+outfile+'\n'
	return msg

class xml:
	def __init__(self,path,time):
		self.start="""
<background>
  <starttime>
    <year>"""+str(s_date.year)+"""</year>
    <month>"""+str(s_date.month)+"""</month>
    <day>"""+str(s_date.day)+"""</day>
    <hour>00</hour>
    <minute>00</minute>
    <second>00</second>
  </starttime>
<!--this will start at midnight-->
"""
		self.s1="""<static>
    <duration>"""+str(time)+"""</duration>
    <file>"""+path
		self.s2="""</file>
  </static>
  <transition>
    <duration>5.0</duration>
    <from>"""+path
		self.s3='</from>'
		self.end="""</to>\n</transition>\n</background>
<!--Created by BAckground Xml Creater -->\n"""


