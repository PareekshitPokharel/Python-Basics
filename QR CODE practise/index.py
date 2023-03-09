import qrcode
from PIL import Image

def qr_generator(*args, **kwargs):
    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size= 20,
        border= 4)

    qr.make(fit=True)
    qr.add_data(*args, **kwargs)

    img = qr.make_image(fill_color="black", back_color="white")
    return img.save('Random_qr.png')

qr_code = input('Please enter your value:')
qr_generator(qr_code)








