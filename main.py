from flask import Flask, request, render_template

app = Flask(__name__, template_folder='face')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            shift_text = alphabet.index(letter)
            new_position = (shift_text + shift) % 26
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += letter
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:
            shift_text = alphabet.index(letter)
            new_position = (shift_text - shift) % 26
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += letter
    return decrypted_text

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        direction = request.form['direction']
        text = request.form['text'].lower()
        shift = int(request.form['shift']) % 26
        if direction == 'encode':
            result = encrypt(text, shift)
        elif direction == 'decode':
            result = decrypt(text, shift)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=False)
