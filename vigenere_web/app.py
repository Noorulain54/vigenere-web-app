from flask import Flask, render_template, request
import re

app = Flask(__name__)

def clean_text(text):
    return re.sub(r'[^A-Za-z]', '', text).upper()

def vigenere_cipher(text, key, mode='encrypt'):
    text = clean_text(text)
    key = clean_text(key)
    result = ""
    for i in range(len(text)):
        t = ord(text[i]) - ord('A')
        k = ord(key[i % len(key)]) - ord('A')
        if mode == 'encrypt':
            r = (t + k) % 26
        else:
            r = (t - k + 26) % 26
        result += chr(r + ord('A'))
    return result

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        message = request.form.get("message", "")
        key = request.form.get("key", "")
        action = request.form.get("action", "encrypt")
        result = vigenere_cipher(message, key, action)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
