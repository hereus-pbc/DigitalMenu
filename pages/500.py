from bevyframe import *


def get(context: Context) -> Page:
    if context.app.debug:
        raise
    return Page(
        title='500 - HereUS Menu',
        color='blank',
        childs=[
            Title(context.string('500')),
            JavaScript([
                context.execute.setTimeout(JavaScript("() => { window.location.href = '/'; }"), 3000)
            ])
        ]
    )