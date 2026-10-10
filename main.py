from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.network.urlrequest import UrlRequest
from kivy.core.window import Window
from kivy.utils import platform
import json

Window.clearcolor = (0.04, 0.07, 0.06, 1)

JSON_URL = "RAW_LINK_HERE"

COLORS = [
    (0.10, 0.60, 0.35, 1),
    (0.85, 0.65, 0.10, 1),
    (0.15, 0.50, 0.75, 1),
    (0.75, 0.25, 0.30, 1),
    (0.55, 0.30, 0.75, 1),
]


def open_stream(url):
    if platform == "android":
        from jnius import autoclass
        Intent = autoclass("android.content.Intent")
        Uri = autoclass("android.net.Uri")
        Activity = autoclass("org.kivy.android.PythonActivity")
        intent = Intent(Intent.ACTION_VIEW)
        intent.setDataAndType(Uri.parse(url), "video/*")
        Activity.mActivity.startActivity(intent)


class SadiqKora(App):
    def build(self):
        self.title = "Sadiq Kora"
        root = BoxLayout(orientation="vertical", padding=12, spacing=10)

        root.add_widget(Label(
            text="SADIQ KORA",
            font_size="30sp",
            bold=True,
            color=(0.95, 0.80, 0.25, 1),
            size_hint_y=None,
            height=90,
        ))

        self.status = Label(
            text="Loading...",
            color=(1, 1, 1, 0.7),
            size_hint_y=None,
            height=40,
        )
        root.add_widget(self.status)

        scroll = ScrollView()
        self.box = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            spacing=12,
        )
        self.box.bind(minimum_height=self.box.setter("height"))
        scroll.add_widget(self.box)
        root.add_widget(scroll)

        UrlRequest(
            JSON_URL,
            on_success=self.load,
            on_failure=self.fail,
            on_error=self.fail,
        )
        return root

    def fail(self, *args):
        self.status.text = "Could not load channels"

    def load(self, req, data):
        if isinstance(data, (str, bytes)):
            data = json.loads(data)
        self.status.text = ""
        for i, ch in enumerate(data):
            b = Button(
                text=ch["name"],
                font_size="20sp",
                bold=True,
                size_hint_y=None,
                height=130,
                background_normal="",
                background_color=COLORS[i % len(COLORS)],
            )
            b.bind(on_release=lambda x, u=ch["url"]: open_stream(u))
            self.box.add_widget(b)
          SadiqKora().run()
