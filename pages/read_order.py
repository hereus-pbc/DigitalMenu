from bevyframe import *
from widgets.back_button import BackButton
from objects.Item import Item
from pages.read_qr import get as mainpage
import gzip


def get(context: Context) -> Page:
    if 'code' not in context.query:
        page: Page = mainpage(context)
        page.content[1] = BackButton(close=True)
        page.content.pop(2)
        return page
    order = {}
    context.order = gzip.decompress(bytes.fromhex(context.query['code'])).decode().split(' ')
    for i in context.order:
        if i in order:
            order[i][1] += 1
        else:
            order.update({i: [Item(i), 1]})
    total = {}
    for i in order:
        if order[i][0].exchange not in total:
            total[order[i][0].exchange] = 0
        total[order[i][0].exchange] += order[i][0].price * order[i][1]
    return Page(
        title="DigitalMenu",
        color='blank',
        childs=[
            BackButton(close=True),
            Root(
                margin=Margin(
                    top=Size.pixel(60)
                ),
                childs=[
                    Box(
                        margin=Margin(
                            bottom=Size.pixel(10)
                        ),
                        childs=[
                            Heading(order[i][0].name),
                            Label(
                                innertext=f"{order[i][1]}x {order[i][0].price} {order[i][0].exchange}",
                                font_size=Size.Relative.font(.8),
                                margin=Margin(top=Size.pixel(-15))
                            ),
                        ]
                    )
                    for i in order
                ] + [
                    Button(
                        selector='mini',
                        innertext=context.string("create_qr", context.browser.language),
                        onclick=context.execute.create_order(context.execute.false),
                    ),
                    Container(
                        margin=Margin(
                            right=Size.pixel(10),
                            top=Size.pixel(-40)
                        ),
                        text_align=Align.right,
                        childs=[
                            Label(f"{total[i]} {i}")
                            for i in total
                        ]
                    ),
                    Button(
                        innertext=context.string("read_new", context.browser.language),
                        onclick=context.start_redirect('/read_order'),
                        position=Position.fixed(
                            bottom=Size.pixel(10),
                            right=Size.pixel(10),
                            left=Size.pixel(10),
                        ),
                        width=substract_style(Size.Viewport.width(100), Size.pixel(20)),
                    )
                ]
            )
        ]
    )
