from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox

class CheckBoxApp(App):
    def build(self):
        # Create a BoxLayout to hold the widgets vertically
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create a Label widget
        label = Label(text='This is a Label')

        # Create two CheckBox widgets
        checkbox1 = CheckBox(active=False, on_active=self.on_checkbox_active)
        checkbox2 = CheckBox(active=True, on_active=self.on_checkbox_active)

        # Add the widgets to the layout
        layout.add_widget(label)
        layout.add_widget(checkbox1)
        layout.add_widget(checkbox2)

        return layout

    def on_checkbox_active(self, instance, value):
        checkbox_text = "Checkbox 1" if instance == checkbox1 else "Checkbox 2"
        checkbox_state = "activated" if value else "deactivated"
        print(f"{checkbox_text} is {checkbox_state}")

if __name__ == '__main__':
    CheckBoxApp().run()
