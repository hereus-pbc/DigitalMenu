from bevyframe import *
from widgets.back_button import BackButton


def get(context: Context) -> Page:
    return Page(
        title="DigitalMenu",
        color='blank',
        childs=[
            BackButton(),
            Root([
                Label(i)
                for i in context.order
            ])
        ]
    )
