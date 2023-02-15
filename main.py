import io
import base64
import time
import secrets
import qrcode
from solana.rpc.api import Client

def build(publickey,amount,INVOICENUMBER):
    return f"solana:{publickey}?amount={amount}&label=Solana Payments&memo={INVOICENUMBER}"


def generate_qr(data, fill_color, back_color):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(back_color=back_color, fill_color=fill_color)
    data = io.BytesIO()
    img.save(data, "PNG")
    encoded_img_data = base64.b64encode(data.getvalue())
    return encoded_img_data.decode('utf-8')

def generate_id():
    return secrets.token_hex(12)

def build_transaction(publickey,amount, fill_color="#000000", back_color="transparent"):
    invoice_id = generate_id()
    
    return [invoice_id, publickey, generate_qr(build(publickey,amount,invoice_id), fill_color, back_color)]


def get_payment_status(invoice_id,wallet):
    solana_client = Client("https://api.mainnet-beta.solana.com")
    for i in solana_client.get_signatures_for_address(wallet)['result']:

        if i['err'] == None:
            if str(invoice_id) in str(i['memo']):
                return True
    return False

