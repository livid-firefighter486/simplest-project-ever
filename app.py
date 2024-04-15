from flask import Flask, render_template, request, redirect, url_for
from database import create_tables, add_email, get_emails

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_email', methods=['POST'])
def submit_email():
    email = request.form['email']
    add_email(email)
    return redirect(url_for('waitlist'))

@app.route('/waitlist')
def waitlist():
    emails = get_emails()
    return render_template('waitlist.html', emails=emails)

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
