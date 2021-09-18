from flask import Flask, render_template,url_for
app =  Flask(__name__)
print(__name__)

@app.route('/')
def dashboards():
    return render_template('index.html')

@app.route('/')
def appointment():
    return render_template('index.html')

@app.route('/')
def charts():
    return render_template('index.html')

@app.route('/')
def department():
    return render_template('index.html')

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/')
def payment():
    return render_template('index.html')

@app.route('/')
def reports():
    return render_template('index.html')

@app.route('/')
def patient():
    return render_template('index.html')

@app.route('/')
def form():
    return render_template('index.html')
