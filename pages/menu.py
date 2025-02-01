import requests
from bevyframe import *
from objects.Menu import Menu


def get(context: Context) -> Page:
    domain = context.query.get('domain')
    webfinger = requests.get(f"https://{domain}/.well-known/webfinger?resource=menu:{domain}")
    if webfinger.status_code != 200:
        raise
    uri = ''
    for i in webfinger.json().get('links', []):
        if i['rel'] == 'https://menu.hereus.net/ns/menu':
            uri = i['href']
    if not uri:
        raise
    menu = Menu(uri)
    context.groups = menu.groups
    return Page(
        title="DigitalMenu",
        color='blank',
        childs=[
            # Place Navbar above Root,
            Root([
                Image(
                    menu.banner,
                    alt='Banner',
                    border_radius=Size.pixel(10),
                    width=substract_style(Size.Viewport.width(100), Size.pixel(15)),
                ),
                Image(
                    menu.icon,
                    alt='Icon',
                    border_radius=Size.percent(50),
                    height=Size.pixel(80),
                    width=Size.pixel(80),
                    margin=Margin(
                        left=Size.pixel(20),
                        top=Size.pixel(-45),
                    ),
                ),
                Container(
                    margin=Margin(left=Size.pixel(20)),
                    childs=[
                        Title(
                            innertext=menu.name,
                            margin=Margin(top=Size.pixel(5))
                        ),
                        Label(
                            innertext=menu.description,
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
                        right=Size.pixel(0),
                    ),
                    childs=[
                        Box(
                            width=substract_style(Size.percent(50), Size.pixel(50)),
                            css={'float': 'left'},
                            margin=Margin(
                                right=Size.pixel(10),
                                bottom=Size.pixel(10),
                            ),
                            childs=[
                                Image(
                                    menu.groups[i].photo,
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
                                    innertext=menu.groups[i].name,
                                    margin=Margin(
                                        top=Size.pixel(5),
                                        bottom=Size.pixel(10),
                                    ),
                                )
                            ],
                            onclick=context.start_redirect(f'/{domain}/{i}')
                        )
                        for i in range(len(menu.groups))
                    ]
                )
            ])
        ]
    )
