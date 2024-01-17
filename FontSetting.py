# poppins 10 bold italic
poppinseBold7 = str('poppins 7 bold')
poppinseBold8 = str('poppins 8 bold')
poppinseBold9 = str('poppins 9 bold')
poppinseBold10 = str('poppins 10 bold')
poppinseBold11 = str('poppins 11 bold')
poppinseBold12 = str('poppins 12 bold')
poppinseBold13 = str('poppins 13 bold')
poppinseBold14 = str('poppins 14 bold')
poppinseBold15 = str('poppins 15 bold')
poppinseBold16 = str('poppins 16 bold')
poppinseBold17 = str('poppins 17 bold')
poppinseBold18 = str('poppins 18 bold')

poppinseItalic7 = str('poppins 7 italic')
poppinseItalic8 = str('poppins 8 italic')
poppinseItalic9 = str('poppins 9 italic')
poppinseItalic10 = str('poppins 10 italic')
poppinseItalic11 = str('poppins 11 italic')
poppinseItalic12 = str('poppins 12 italic')

# standers 
HEADING = int(16)
SUBHEADING = int(14)
DEFAULT = int(12)
SMALLTEXT = int(8)
LARGETEXT = int(20)

class SetFontFamily: # main class
    def __init__(self,_fontfamily): #constructor which takes the font name
        self.name = _fontfamily 
    def setFont_size_style(self,_size,_style):
        return str(self.name + " " + str(_size) + " " + _style)
    def setFont_size(self,_size):
        return str(self.name + " " + str(_size))
    def setFont_default(self):
        return str(self.name + " " + str(DEFAULT))
    def setFont_heading(self):
        return str(self.name + " " + str(HEADING) + ' bold')
    def setFont_subheading(self):
        return str(self.name + " " + str(SUBHEADING))
    def setFont_smallText(self):
        return str(self.name + " " + str(SMALLTEXT))
    def setFont_largeText(self):
        return str(self.name + " " + str(LARGETEXT))