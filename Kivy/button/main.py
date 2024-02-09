from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):

        button = Button(text='Click Me!', 
                        size_hint=(None, None), 
                        size=(200, 100),          
                        pos=(300, 200),           
                        on_press=self.on_button_press)  

        return button

    def on_button_press(self, instance):
        print("Button Pressed!")

if __name__ == '__main__':
    ButtonApp().run()
