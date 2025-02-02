from bevyframe import *


def reset_read(context: Context) -> JavaScript:
    context.read = None
    return JavaScript(context.start_redirect('/read_order'))
