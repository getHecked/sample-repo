from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
sum1=2
app = Flask(__name__)

@app.route('/hit', methods=['GET','POST'])
def index():
    return render_template('index.html', user_sum=sum1)

if __name__ == '__main__':
	app.run(debug=True)
