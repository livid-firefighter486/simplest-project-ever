from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/popup')
def popup():
    website_url = request.args.get('websiteURL')
    if website_url:
        try:
            page_content = requests.get(website_url).text
        except requests.exceptions.RequestException as e:
            page_content = f"<h1>Error: {e}</h1>"
    else:
        page_content = '<h1>No website preview available.</h1>'
    return render_template('popup.html', page_content=page_content, website_url=website_url)


@app.route('/')
def index():
    return render_template('dashboard.html', title='Dashboard')

@app.route('/tables')
def tables():
    return render_template('tables.html', title='Tables')

@app.route('/billing')
def billing():
    return render_template('billing.html', title='Billing')

@app.route('/widget')
def widget():
    return render_template('widget.html', title='Widget Editor')

@app.route('/rtl')
def rtl():
    return render_template('rtl.html', title='RTL')

@app.route('/profile')
def profile():
    return render_template('profile.html', title='Profile')

@app.route('/sign-in')
def sign_in():
    return render_template('sign-in.html', title='Sign In')

@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html', title='Sign Up')

if __name__ == '__main__':
    app.run(debug=True)

