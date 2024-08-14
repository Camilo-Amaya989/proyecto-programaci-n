from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def principal():
    return render_template('home.html')

@app.route('/mision')
def mision():
    return render_template('mision.html')

@app.route('/vision')
def vision():
    return render_template('vision.html')

@app.route('/objetivo')
def objetivo():
    return render_template('objetivo.html')

#ejecutar el servidor

if __name__ == '__main__':
    app.run(debug=True) 

