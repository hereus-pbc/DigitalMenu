from bevyframe import *


def get(context: Context) -> Page:
    return Page(
        title="DigitalMenu",
        color=context.user.id.settings.theme_color,
        childs=[
            # Place Navbar above Root,
            Root([
                # Place your content here
            ])
        ]
    )
            