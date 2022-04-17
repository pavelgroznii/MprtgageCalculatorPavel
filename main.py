from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MorgageCalculatorApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Morgage Calculator", halign="center")


MorgageCalculatorApp().run()