'''
SETUP: Virtual Environments

mkdir myproject
cd myproject
python3 -m venv venv

. venv/bin/activate

pip install Flask

create app.py with the code 

python3 app.py 

Use any browser for: http://127.0.0.1:5000 

'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Yoooh!!!"

if __name__ == "__main__":
    app.run(debug=True)