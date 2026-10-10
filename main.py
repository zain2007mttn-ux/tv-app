from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.network.urlrequest import UrlRequest
from kivy.core.window import Window
import json, webbrowser

Window.clearcolor = (0.04, 0.07, 0.06, 1)
URL = "https://raw.githubusercontent.com/zain2007mttn-ux/tv-app/main/channels.json"
C = [(0.1, 0.6, 0.35, 1), (0.85, 0.65, 0.1, 1), (0.15, 0.5, 0.75, 1)]

class SadiqKora(App):
    def build(self):
        self.box = BoxLayout(orientation="vertical", size_hint_y=None, spacing=10, padding=10)
        self.box.bind(minimum_height=self.box.setter("height"))
        sv = ScrollView()
        sv.add_widget(self.box)
        UrlRequest(URL, on_success=self.load)
        return sv

    def load(self, req, data):
        if isinstance(data, (str, bytes)):
            data = json.loads(data)
        for i, ch in enumerate(data):
            b = Button(text=ch["name"], size_hint_y=None, height=130, background_normal="", background_color=C[i % 3])
            b.bind(on_release=lambda x, u=ch["url"]: webbrowser.open(u))
            self.box.add_widget(b)

SadiqKora().run()
