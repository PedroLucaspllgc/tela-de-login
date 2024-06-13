from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

class Login(Screen):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        layout_float = FloatLayout()
        
        imagem = AsyncImage(source='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4SdvpxJlSY1IUWJJ2oFlipGY9dqmV7BCiYQ&s', pos_hint={'x': 0, 'y': 0.2})
        
        email = TextInput(hint_text='Email', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.4})
        senha = TextInput(hint_text='Senha', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.3})
        
        btn1 = Button(text='Login', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.2}, background_color=get_color_from_hex('#D1D1D1'))
        btn2 = Button(text='Registrar', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.1}, background_color=get_color_from_hex('#D1D1D1'), on_press=self.ir_para_registro)
        
        layout_float.add_widget(email)
        layout_float.add_widget(senha)
        layout_float.add_widget(imagem)
        layout_float.add_widget(btn1)
        layout_float.add_widget(btn2)
        
        Window.clearcolor = (1, 1, 1, 1)
        
        self.add_widget(layout_float)
        
    def ir_para_registro(self, instance):
        self.manager.current = 'Registro'

class Registro(Screen):
    def __init__(self, **kwargs):
        super(Registro, self).__init__(**kwargs)
        layout_float = FloatLayout()
        
        imagem = AsyncImage(source='/Users/aluno.sesipaulista/Downloads/oie.png', pos_hint={'x': 0, 'y': 0.2})
        
        email = TextInput(hint_text='Email', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.4})
        senha = TextInput(hint_text='Senha', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.3})
        
        btn2 = Button(text='Registrar', size_hint=(None, None), size=(450, 50), pos_hint={'x': 0.27, 'y': 0.2}, background_color=get_color_from_hex('#D1D1D1'), on_press=self.ir_para_login)
        
        layout_float.add_widget(email)
        layout_float.add_widget(senha)
        layout_float.add_widget(imagem)
        layout_float.add_widget(btn2)
        
        Window.clearcolor = (1, 1, 1, 1)
        
        self.add_widget(layout_float)
    
    def ir_para_login(self, instance):
        self.manager.current = 'Login'


class GerenciadorTelas(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        gerenciador = GerenciadorTelas()
        gerenciador.add_widget(Login(name='Login'))
        gerenciador.add_widget(Registro(name='Registro'))
        return gerenciador


if __name__ == "__main__":
    MyApp().run()
