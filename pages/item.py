from bevyframe import *
from objects.Item import Item
from widgets.back_button import BackButton


def get(context: Context) -> Page:
    index = int(context.query.get('item'))
    item = Item(context.items[index])
    count = 0
    for i in context.order:
        if i == item.id:
            count += 1
    # noinspection PyTypeChecker
    return Page(
        title="DigitalMenu",
        color='blank',
        childs=[
            BackButton(),
            Root([
                Image(
                    item.photo,
                    alt='Banner',
                    border_radius=Size.pixel(10),
                    width=substract_style(Size.Viewport.width(100), Size.pixel(15)),
                ),
                Container(
                    margin=Margin(left=Size.pixel(20)),
                    childs=[
                        Title(
                            innertext=item.name,
                            margin=Margin(top=Size.pixel(5))
                        ),
                        Label(
                            innertext=item.description,
                            margin=Margin(top=Size.pixel(-20)),
                            font_size=Size.Relative.font(.8),
                            color='#80808080'
                        ),
                        Line([
                            Label(Bold(item.price), no_newline=True),
                            ' ',
                            Label(
                                innertext=item.exchange,
                                no_newline=True,
                                font_size=Size.Relative.font(.8),
                                color='#80808080'
                            ),
                        ]),
                        Button(
                            selector='mini',
                            innertext=context.string('add_to_order', context.browser.language),
                            width=Size.max_content,
                            onclick=context.execute.add_to_order(item.id)
                        ),
                        Button(
                            selector='mini',
                            innertext=context.string('remove_from_order', context.browser.language),
                            width=Size.max_content,
                            onclick=context.execute.remove_from_order(item.id),
                            margin=Margin(left=Size.pixel(10)),
                        ),
                        Label(
                            context.string('already_added_1', context.browser.language) +
                            f" {count} " +
                            context.string('already_added_2', context.browser.language),
                            id='already_added',
                        )
                    ]
                )
            ])
        ]
    )
