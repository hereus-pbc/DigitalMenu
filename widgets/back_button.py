from bevyframe import *


class BackButton(Button):
    def __init__(self, close: bool = False) -> None:
        super().__init__(
            'mini',
            innertext=Icon('close' if close else 'arrow_back'),
            onclick=('window.location.href = \'/\'' if close else 'history.back()'),
            width=Size.pixel(30),
            height=Size.pixel(30),
            padding=Padding(
                top=Size.pixel(3),
                left=Size.pixel(3),
            ),
            position=Position.fixed(
                left=Size.pixel(15),
                top=Size.pixel(15),
            )
        )