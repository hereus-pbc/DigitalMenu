from bevyframe import *


def get(context: Context) -> Page:
    return Page(
        title="DigitalMenu",
        color='blank',
        childs=[
            # Place Navbar above Root,
            Root([
                # Place your content here
            ])
        ]
    )
