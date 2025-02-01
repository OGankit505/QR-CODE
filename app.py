from flask import Flask, request, send_file, render_template
import qrcode
from io import BytesIO
from flask_cors import CORS  # Enable CORS to allow frontend requests

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend connection

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate_qr", methods=["POST"])
def generate_qr():
    data = request.form.get("data")
    fg_color = request.form.get("color", "#000000")  # Default: Black
    bg_color = request.form.get("bgcolor", "#FFFFFF")  # Default: White

    if not data:
        return "Missing data", 400

    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fg_color, back_color=bg_color)

    # Save QR code to memory
    img_io = BytesIO()
    img.save(img_io, format="PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
