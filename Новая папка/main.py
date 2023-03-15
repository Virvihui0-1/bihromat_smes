from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.config import Config
Config.set('kivy','keyboard_mode','systemanddock')
from kivymd.theming import ThemeManager
#Window.size=(540,1170)
Builder.load_string("""
<Itemlabel@MDTextField>:
    font_size:'30sp'
    #size_hint:.1,.26
    halign:'center'
    valign:'middle'
    input_type:'number'
    input_filter:'int'
<Godv>:
    rows:6
    padding:80
    label1:label_1
    label2:label_2
    input1:input_1
    input2:input_2
    input3:input_3

    Itemlabel:
        id:input_1
        multiline:False
        hint_text:'4/1 Cr2O3'

    Itemlabel:
        id:input_2
        multiline:False
        hint_text:'5/1 Cr2O3'

    Itemlabel:
        id:input_3
        multiline:False
        hint_text:'кубы'
    Label:
        id:label_1
        #text:'Бихромат 2,4(cm)'
        font_size:55
    Label:
        id:label_2
        #text:'Вода 3,6(cm)'
        font_size:55

    MDRectangleFlatButton:
        text:'Расчет'
        font_size:55
        size_hint:.1,.4
        on_press:
            root.Ras()""")

class Godv(GridLayout):
    def Ras(self):
        self.a=(int(self.input1.text)/(int(self.input2.text)))
        self.v=int(self.input3.text)/(self.a)
        self.voda=int(self.input3.text)-self.v

        self.label1.text = f'Бихромат {str(round(int(self.input3.text)/self.a,2))} ({round(int(self.input3.text)/self.a/0.061)}cm) '
        self.label2.text = f'Вода {str(round(self.voda,2))} ({round(self.voda/0.061)}cm) '

class MainApp(MDApp):

    theme_cls=ThemeManager()
    title = 'bih'

    def build(self):
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette = "Orange"

        return Godv()
if __name__=='__main__':
    MainApp().run()

