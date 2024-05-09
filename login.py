from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

class Login(App):
    def build(self):
      layout_float = FloatLayout()
      
      imagem = Image(source='/Users/aluno.sesipaulista/Downloads/ola.png', pos_hint={'x': 0, 'y': 0.2})
      
      email = TextInput(text='Email', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.4})
      senha = TextInput(text='Senha', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.3})
      
      btn1 = Button(text='Login', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.2}, background_color=get_color_from_hex('#D1D1D1'))
      btn2 = Button(text='Registrar', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.1}, background_color=get_color_from_hex('#D1D1D1'))
      
      layout_float.add_widget(email)
      layout_float.add_widget(senha)
      layout_float.add_widget(imagem)
      layout_float.add_widget(btn1)
      layout_float.add_widget(btn2)
      
      Window.clearcolor = (1, 1, 1, 1)
      
      return layout_float
      
if __name__ == "__main__":
    Login().run()