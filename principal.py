from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from login import LoginScreen
from Registrar import RegistroScreen

class MinhaApp(App):
    def build(self):

        sm = ScreenManager()

        sm.add_widget(LoginScreen(name='Login'))
        sm.add_widget(RegistroScreen(name='Registrar'))

        return sm
    
if __name__ == "__main__":
    MinhaApp().run()
