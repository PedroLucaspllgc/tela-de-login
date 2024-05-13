from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.utils import get_color_from_hex
from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class RegistroScreen(Screen):
    def __init__(self, **kwargs):
      super(RegistroScreen, self).__init__(**kwargs)

      layout_float = FloatLayout()
      
      imagem = AsyncImage(source='https://pt.pngtree.com/freepng/avatar-icon-profile-icon-member-login-vector-isolated_5247852.html', pos_hint={'x': 0, 'y': 0.2})
      
      email = TextInput(text='Email', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.4})
      senha = TextInput(text='Senha', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.3})
      
      btn2 = Button(text='Registrar', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.2}, background_color=get_color_from_hex('#D1D1D1'))
      
      layout_float.add_widget(email)
      layout_float.add_widget(senha)
      layout_float.add_widget(imagem)
      layout_float.add_widget(btn2)
      
      Window.clearcolor = (1, 1, 1, 1)

      self.add_widget(layout_float)
