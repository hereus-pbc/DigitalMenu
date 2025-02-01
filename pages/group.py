import requests
from bevyframe import *
from objects.Group import Group
from widgets.back_button import BackButton


def get(context: Context) -> Page:
    domain = context.query.get('domain')
    index = int(context.query.get('group'))
    group = Group(context.groups[index])
    context.items = [i.id for i in group.items]
    return Page(
        title="DigitalMenu",
        color='blank',
        childs=[
            BackButton(),
            Root([
                Image(
                    group.photo,
                    alt='Banner',
                    border_radius=Size.pixel(10),
                    width=substract_style(Size.Viewport.width(100), Size.pixel(15)),
                ),
                Container(
                    margin=Margin(left=Size.pixel(20)),
                    childs=[
                        Title(
                            innertext=group.name,
                            margin=Margin(top=Size.pixel(5))
                        ),
                        Label(
                            innertext=group.description,
                            margin=Margin(top=Size.pixel(-20)),
                            font_size=Size.Relative.font(.8),
                            color='#80808080'
                        ),
                    ]
                ),
                Container(
                    margin=Margin(left=Size.pixel(10)),
                    position=Position.fixed(
                        left=Size.pixel(10),
                        right=Size.pixel(10),
                    ),
                    childs=[
                        Box(
                            width=substract_style(Size.percent(100), Size.pixel(40)),
                            css={'float': 'left'},
                            margin=Margin(
                                right=Size.pixel(10),
                                bottom=Size.pixel(10),
                            ),
                            childs=[
                                Image(
                                    group.items[i].photo,
                                    alt='',
                                    width=add_style(Size.percent(100), Size.pixel(30)),
                                    max_height=multiply_style(add_style(Size.percent(100), Size.pixel(30)), 4),
                                    margin=Margin(
                                        left=Size.pixel(-15),
                                        right=Size.pixel(-15),
                                    ),
                                    border_radius=Size.pixel(20),
                                ),
                                Heading(
                                    innertext=group.items[i].name,
                                    margin=Margin(
                                        top=Size.pixel(5),
                                        bottom=Size.pixel(10),
                                    ),
                                ),
                                Label(
                                    font_size=Size.Relative.font(.8),
                                    color='#80808080',
                                    innertext=group.items[i].name,
                                    margin=Margin(
                                        top=Size.pixel(-5),
                                        bottom=Size.pixel(10),
                                    ),
                                )
                            ],
                            onclick=context.start_redirect(f'/{domain}/{index}/{i}')
                        )
                        for i in range(len(group.items))
                    ]
                )
            ])
        ]
    )
