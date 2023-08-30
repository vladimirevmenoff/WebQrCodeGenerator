from flask import render_template
from flask import request

from app import session
from app import app
                            
def generate_map(url):
	import qrcode

	qr = qrcode.QRCode()

	qr.add_data(url)
	qr.make(fit=True)
	
	map = qr.get_matrix() 

	return render_template('game.html', map = map, width = len(map), height = len(map))
	

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['url'] = str(request.form['url'])
        return generate_map(url = session['url'])
    return render_template('index.html')
