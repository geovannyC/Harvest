import kivy 
kivy.require('1.9.1') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

# add the following 2 lines to solve OpenGL 2.0 bug
from kivy.config import Config
Config.set('graphics', 'multisamples', '0')

class MyGrid(Widget):
    pass
class MyApp():
    def build(self):
        return MyGrid

if __name__ == '__main__':
    MyApp().run ()
