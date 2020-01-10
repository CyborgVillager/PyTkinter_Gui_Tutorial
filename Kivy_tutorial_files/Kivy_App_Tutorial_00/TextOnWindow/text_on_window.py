from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

BoxLayout:
    #orientation:'vertical'
    orientation:'horizontal'
    Label:
        canvas.before:
            Color:
                rgba: 1,0,0,.22
            Rectangle:
                pos:self.pos
                size:self.size
        text:'Top'
        size_hint_y:None
        height:sp(70)
        font_size:sp(50)
    Label:
        canvas.before:
            Color:
                rgba: 2,1,1,.35
            Rectangle:
                pos:self.pos
                size:self.size
        text:'Center'
        size_hint_y:None
        size_hint_x:None
        width:sp(85)
        height:sp(65)
        font_size:sp(25)
        
        
    Label:
        canvas.before:
            Color:
                rgba: 4,103,32,.25
            Rectangle:
                pos:self.pos
                size:self.size
        text:'Bottom'
        size_hint_y:None
        height:sp(35)
        font_size:sp(25)
    
                
    

'''))