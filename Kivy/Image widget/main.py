from kivy.app import App
from kivy.uix.image import Image

class ImageApp(App):
    def build(self):
        img = Image(source='cat.png')
        return img

if __name__ == '__main__':
    ImageApp().run()
