from bevyframe import *
from widgets.back_button import BackButton
from objects.Item import Item


def get(context: Context) -> Page:
    order = {}
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
            BackButton(),
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
                    Container(
                        margin=Margin(
                            right=Size.pixel(10)
                        ),
                        text_align=Align.right,
                        childs=[
                            Label(f"{total[i]} {i}")
                            for i in total
                        ]
                    )
                ] + [
                    Button(
                        innertext=context.string("create_order", context.browser.language),
                        onclick=context.execute.create_order(),
                    )
                ]
            )
        ]
    )
