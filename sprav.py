from flask import Flask, render_template

app = Flask(__name__)

@app.route('/glav')
@app.route('/')
def glav():
    return render_template('/glav.html')

@app.route('/index')
def index():
    return render_template('index.html')

#вкладка виды игр    

@app.route('/about')
def about():
    return render_template('about.html')

#вкладки с названием игр и их описанием    

@app.route('/hok')
def hok():
    return render_template('hok.html')

@app.route('/fig')
def fig():
    return render_template('fig.html')

@app.route('/kon')
def kon():
    return render_template('kon.html')

@app.route('/biat')
def biat():
    return render_template('biat.html')

@app.route('/sky')
def sky():
    return render_template('sky.html')

@app.route('/sky2')
def sky2():
    return render_template('sky2.html')

@app.route('/gor_sky')
def gor_sky():
    return render_template('gor_sky.html')

@app.route('/tramp')
def tramp():
    return render_template('tramp.html')

@app.route('/fris')
def fris():
    return render_template('fris.html')

@app.route('/snoub')
def snoub():
    return render_template('snoub.html')

@app.route('/short')
def short():
    return render_template('short.html')

@app.route('/bob')
def bob():
    return render_template('bob.html')

@app.route('/san')
def san():
    return render_template('san.html')

@app.route('/ker')
def ker():
    return render_template('ker.html')

@app.route('/skel')
def skel():
    return render_template('skel.html')

#вкладки с названием игр и их описнаием (конец)

@app.route('/posl_igr')
def posl_igr():
    return render_template('posl_igr.html')

@app.route('/bud_igr')
def bud_igr():
    return render_template('bud_igr.html')

@app.route('/dost')
def dost():
    return render_template('dost.html')

if __name__ == '__main__':
    app.run(debug = True)
    
