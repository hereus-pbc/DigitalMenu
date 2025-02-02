from bevyframe import *
import qrcode
import base64
import io
import gzip


def create_order(context: Context) -> change_html:
    qr_content = ' '.join(context.order)
    qr_content = gzip.compress(qr_content.encode()).hex()
    img = qrcode.make(qr_content)
    fake_file = io.BytesIO()
    img.save(fake_file, format='PNG')
    return change_html(
        '#root',
        [
            SubTitle(context.string("qr_to_waiter", context.browser.language)),
            Image(
                src=f"data:image/png;base64,{base64.b64encode(fake_file.getvalue()).decode()}",
                alt='QR Code',
                position=Position.fixed(
                    top=substract_style(
                        substract_style(Size.Viewport.height(50), Size.Viewport.width(50)),
                        Size.pixel(60)
                    ),
                    left=Size.pixel(10),
                    bottom=substract_style(Size.Viewport.height(50), Size.Viewport.width(50)),
                    right=Size.pixel(10),
                ),
                width=substract_style(Size.Viewport.width(100), Size.pixel(20)),
                height=substract_style(Size.Viewport.width(100), Size.pixel(20)),
                border_radius=Size.pixel(20),
            )
        ]
    )
