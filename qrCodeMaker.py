import qrcode
import qrcode.constants
from secrets import token_urlsafe

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

qrID = token_urlsafe(16)

qr.add_data(f"http://10.0.0.45:5000/{qrID}")
qr.make(fit=True)

img = qr.make_image()
img.save("qr.png")