from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ""
    selected_src = 'auto'  # Default: auto-detect
    selected_dest = 'hi'   # Default: Hindi

    if request.method == 'POST':
        input_text = request.form['text']
        selected_src = request.form['source_lang']
        selected_dest = request.form['dest_lang']

        if input_text:
            translated = translator.translate(input_text, src=selected_src, dest=selected_dest)
            translation = translated.text

    return render_template('index.html',
                           translation=translation,
                           languages=LANGUAGES,
                           selected_src=selected_src,
                           selected_dest=selected_dest)

if __name__ == '__main__':
    app.run(debug=True)
