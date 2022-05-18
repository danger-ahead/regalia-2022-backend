from PIL import Image, ImageDraw, ImageFont
import pyqrcode
from routes.resend_email_scripts import mail
from routes.resend_email_scripts import create_pass

template = Image.open("routes/resend_email_scripts/templates/pass_template.png")
detailsFont = ImageFont.truetype("routes/resend_email_scripts/templates/fonts/Poppins-Regular.ttf", 60)
allowedFont = ImageFont.truetype("routes/resend_email_scripts/templates/fonts/Poppins-SemiBold.ttf", 65)


def makeCertificate(email, name, roll_number, allowed):
    response = create_pass.create_pass(email, name, roll_number, allowed)

    cert = template.copy()
    draw = ImageDraw.Draw(cert)
    # qrcodes
    size = makeQR(response["_id"])
    pos = ((842 - int(size / 2)), 160)
    cert.paste(Image.open("routes/resend_email_scripts/templates/qr_code.png"), pos)
    # unique number
    w, h = draw.textsize(response["_id"].upper(), detailsFont)
    draw.text(
        xy=((1684 - w) / 2, 1100),
        text=response["_id"].upper(),
        fill="#03045E",
        font=detailsFont,
    )
    # name
    nameFont = 150
    w, h = draw.textsize(
        name.upper(), ImageFont.truetype("routes/resend_email_scripts/templates/fonts/Poppins-Bold.ttf", nameFont)
    )
    difference = w - (1682 - 440)
    if difference > 0 and difference <= 100:
        nameFont = 130
    elif difference > 100 and difference <= 250:
        nameFont = 110
    elif difference > 250 and difference <= 400:
        nameFont = 100
    elif difference > 400:
        nameFont = 80
    else:
        nameFont = 150
    draw.text(
        xy=(220, 1450),
        text=name.upper(),
        fill="white",
        font=ImageFont.truetype("routes/resend_email_scripts/templates/fonts/Poppins-Bold.ttf", nameFont),
    )
    # email
    draw.text(xy=(220, 1650), text=email, fill="white", font=detailsFont)
    # roll
    draw.text(xy=(220, 1740), text=roll_number.upper(), fill="white", font=detailsFont)
    # allowed
    allowText = "Single Entry Only"
    match allowed:
        case 3:
            allowText = "+2 allowed"
        case 2:
            allowText = "+1 allowed"
    draw.text(xy=(360, 2330), text=allowText, fill="white", font=allowedFont)

    cert.save("routes/resend_email_scripts/templates/pass.png")

    # send email
    mail.send_mail(email, name, response["_id"], str(response["allowed"]))


def makeQR(data):
        qr = pyqrcode.create(data)
        qr.png(
            "routes/resend_email_scripts/templates/qr_code.png", scale=30, module_color="#03045E", background="#538EFF"
        )
        return qr.get_png_size(30)
