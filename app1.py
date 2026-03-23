from flask import Flask, render_template, request
import easyocr
from deep_translator import GoogleTranslator
import os

app = Flask(__name__)

# Create uploads folder if not exists
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 🔹 Dynamic OCR reader based on language
def get_reader(lang):
    if lang == 'ja':
        return easyocr.Reader(['ja', 'en'])
    elif lang == 'hi':
        return easyocr.Reader(['hi', 'en'])
    elif lang == 'kn':
        return easyocr.Reader(['kn', 'en'])
    else:
        return easyocr.Reader(['en'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    conversion = request.form['conversion']
    input_lang = request.form['input_lang']
    output_lang = request.form['output_lang']
    text = request.form['text']

    # 🔹 Handwritten → Text
    if conversion in ['h2t', 'h2h']:
        image = request.files['image']

        if image.filename != "":
            image_path = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(image_path)

            reader = get_reader(input_lang)  # 🔥 FIXED HERE
            result = reader.readtext(image_path, detail=0)
            text = " ".join(result)

    # 🔹 Translation (Text → Text OR Handwritten → Handwritten)
    if conversion in ['t2t', 'h2h']:
        translated = GoogleTranslator(source='auto', target=output_lang).translate(text)
    else:
        translated = text

    return render_template('result.html', text=translated)
@app.route('/convert')
def convert():
    return render_template('convert.html')
if __name__ == '__main__':
    app.run(debug=True)