from bevyframe import *
import os


def get(context: Context) -> Page | Response:
    if context.email.split('@')[0] == 'Guest':
        resp = context.start_redirect('/')
        resp.credentials = {
            'email': f"{os.urandom(32).hex()}@{context.ip}",
            'token': ''
        }
        return resp
    return Page(
        title="DigitalMenu",
        color='blank',
        style={'user-select': NoStyle},
        childs=[
            Root(
                margin=Margin(
                    left=Size.auto,
                    right=Size.auto,
                    top=Size.Viewport.height(20),
                ),
                width=Size.max_content,
                childs=[
                    Title(context.string('scan_qr')),
                    Box(
                        border_radius=Size.pixel(10),
                        width=Size.Viewport.width(90),
                        height=Size.Viewport.width(90),
                        padding=Padding(
                            top=Size.pixel(0),
                            left=Size.pixel(0),
                            right=Size.pixel(0),
                            bottom=Size.pixel(-5),
                        ),
                        css={
                            'overflow': Visibility.hidden
                        },
                        id="box",
                        childs=[
                            '<video id="video" autoplay></video>'
                        ]
                    ),
                ]
            ),
            Button(
                selector='mini',
                position=Position.fixed(
                    top=Size.pixel(10),
                    right=Size.pixel(10),
                ),
                innertext=context.string('read_order', context.browser.language),
                onclick=context.start_redirect('/read_order')
            ),
            Container(
                position=Position.fixed(
                    bottom=Size.pixel(0),
                    left=Size.pixel(5),
                ),
                color='#80808080',
                font_size=Size.Relative.font(.5),
                childs=[
                    Label("HereUS Menu Client for HereUS Menu Schema"),
                    Label('Copyright (c) 2024 HereUS PBC, All rights (of this Product) reserved.'),
                    Label('You can view the source code on ' +
                          '<a href="https://github.com/hereus-pbc/DigitalMenu" style="text-decoration:underline">GitHub</a>' +
                          ' licensed under HereUS OSPL 1.0'),
                    Label('By using this app, you are accepting ' +
                          '<a href="https://static.hereus.net/web_tos.html" style="text-decoration:underline">Terms of Service</a>' +
                          ' for all HereUS websites and web apps.'),
                ]
            ),
            f'<script src="{context.get_asset("__init__.js")}" async></script>',
        ]
    )
