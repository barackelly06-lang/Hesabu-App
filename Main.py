from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class HesabuLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        self.input = TextInput(hint_text='Weka mauzo ya leo', multiline=False, font_size=24)
        self.add_widget(self.input)

        btn = Button(text='Hifadhi Mau
