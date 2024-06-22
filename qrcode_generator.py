import qrcode
import os

QR_CODE_FOLDER = 'qrcodes'

def generate_qrcode(student_id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"https://c69d-103-248-174-89.ngrok-free.app/student/{student_id}")
    qr.make(fit=True) 

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.path.join(QR_CODE_FOLDER, f'{student_id}.png'))

