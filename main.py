from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Kalkulator(App):

    def build(self):
        self.angka = ""

        layout = BoxLayout(orientation="vertical")

        self.layar = Label(
            text="0",
            font_size=40
        )

        layout.add_widget(self.layar)

        tombol = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["C", "0", "=", "/"]
        ]

        for baris in tombol:
            row = BoxLayout()

            for teks in baris:
                btn = Button(
                    text=teks,
                    font_size=30
                )

                btn.bind(
                    on_press=self.tekan
                )

                row.add_widget(btn)

            layout.add_widget(row)

        return layout

    def tekan(self, tombol):
        teks = tombol.text

        if teks == "C":
            self.angka = ""
            self.layar.text = "0"

        elif teks == "=":
            try:
                self.layar.text = str(
                    eval(self.angka)
                )
                self.angka = self.layar.text

            except:
                self.layar.text = "Error"
                self.angka = ""

        else:
            self.angka += teks
            self.layar.text = self.angka


Kalkulator().run()
