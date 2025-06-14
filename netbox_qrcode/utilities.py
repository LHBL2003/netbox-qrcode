import base64
from io import BytesIO
from PIL import Image
import qrcode
import barcode
from barcode.writer import ImageWriter
from pylibdmtx.pylibdmtx import encode

# ******************************************************************************************
# Includes useful tools to create barcode content as images (QR, Code128, Data Matrix etc.).
# ******************************************************************************************

##################################          
# Creates a QR code as an image.: https://pypi.org/project/qrcode/3.0/
# --------------------------------
# Parameter:
#   text: Text to be included in the QR code.
#   **kwargs: List of parameters which properties the QR code should have. (e.g. version, box_size, error_correction, border etc.)
def get_qr(text, **kwargs):
    qr = qrcode.QRCode(**kwargs)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.get_image()
    return img

##################################
# Creates a Code128 barcode and returns it as Base64-encoded PNG.
# --------------------------------
# Parameters:
#   text: Text to be encoded in the Code128 barcode.
def get_1D_Barcode(text):
    code128 = barcode.get('code128', text, writer=ImageWriter())
    img = code128.render(writer_options={"write_text": False})
    return img

##################################
# Creates a Data Matrix code and returns it as Base64-encoded PNG.
# --------------------------------
# Parameters:
#   text: Text to be encoded in the Data Matrix barcode.
def get_datamatrix(text):
    encoded = encode(text.encode('utf-8'))
    img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
    return img

##################################          
# Converts an image to Base64
# --------------------------------
# Parameter:
#   img: PIL Image object.
def get_img_b64(img):
    stream = BytesIO()
    img.save(stream, format='png')
    return str(base64.b64encode(stream.getvalue()), encoding='ascii')