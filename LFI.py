from flask import Flask, request, url_for, render_template, redirect, abor
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/home", methods=['POST'])
def home():
    filename = request.form['filename']
    if not filename:
        filename = "text/default.txt"
        f = open(filename,'r')

    # Define a safe base directory
    base_dir = os.path.join(app.root_path, 'text')

    # Construct the full file path and resolve it to its absolute path
    filepath = os.path.abspath(os.path.join(base_dir, filename))

    # Ensure the file is within the base directory
    if not filepath.startswith(base_dir):
        abort(400, description="Invalid file path.")

    try:
        with open(filepath, 'r') as f:
            read = f.read()
    except IOError:
        abort(404, description="File not found.")

    return render_template("index.html", read=read)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

