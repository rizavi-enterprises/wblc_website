from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('base.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Programs route
@app.route('/programs')
def programs():
    return render_template('programs.html')

# Fees route
@app.route('/fees')
def fees():
    return render_template('fees.html')

# Contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
