from bevyframe import *


def add_to_order(context: Context, id: str) -> change_html:
    context.order += [id]
    count = 0
    for i in context.order:
        if i == id:
            count += 1
    return change_html('#already_added', [
        context.string('already_added_1', context.browser.language),
        f" {count} ",
        context.string('already_added_2', context.browser.language),
    ])
