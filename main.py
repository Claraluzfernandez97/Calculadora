from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ecuacion = ''

        with self.canvas:
            Color(0.6, 0.6, 0.6, 0.9)
            self.rect = Rectangle(size=(self.size[0], 0.15 * self.size[1]), pos=(0, 0.85 * self.height))

        self.muestra = MDLabel(text="0", bold=True, halign='center', pos_hint={'center_y': 0.925})
        self.add_widget(self.muestra)

        self.botones = GridLayout(cols=4, size_hint=(1, 0.7), spacing=5, padding=10, pos_hint={'center_x': 0.5, 'top': 0.82})

        # Lista de botones para agregarlos limpiamente sin errores de sintaxis
        lista_botones = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            '.', '0', '=', '/'
        ]

        for texto in lista_botones:
            if texto == '=':
                btn = Button(text=texto, bold=True, size_hint=(0.25, 0.18), background_color='lightblue')
                btn.bind(on_press=lambda x: self.resultado())
            else:
                btn = Button(text=texto, bold=True, size_hint=(0.25, 0.18), background_color='lightblue')
                btn.bind(on_press=lambda x, t=texto: self.presionar(t))
            self.botones.add_widget(btn)

        self.add_widget(self.botones)

        # Botón Borrar corregido en una sola línea para evitar fallos de Python
        btn_borrar = Button(text='Borrar', bold=True, size_hint=(0.25, 0.12), background_color='red', pos_hint={'center_x': 0.5, 'top': 0.12})
        btn_borrar.bind(on_press=lambda x: self.borrar())
        self.add_widget(btn_borrar)

    def on_size(self, *args):
        self.rect.size = (self.size[0], 0.15 * self.size[1])
        self.rect.pos = (0, 0.85 * self.height)

    def presionar(self, valor):
        self.ecuacion = self.ecuacion + valor
        self.muestra.text = self.ecuacion

    def resultado(self):
        try:
            self.ecuacion = str(eval(self.ecuacion))
            self.muestra.text = self.ecuacion
        except:
            self.ecuacion = ''
            self.muestra.text = 'Error'

    def borrar(self):
        self.ecuacion = ''
        self.muestra.text = '0'

class Miapp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        SC = ScreenManager()
        SC.add_widget(Principal(name='principal'))
        return SC

if __name__ == '__main__':
    Miapp().run()
