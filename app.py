from flask import Flask , request ,url_for , render_template
import numpy as np
import pickle


sc = pickle.load(open('C:\miniproject\sc.pkl' , 'rb'))

model = pickle.load(open('C:\miniproject\model.pkl' , 'rb'))
app = Flask(__name__)

@app.route('/')
@app.route('/home1')
def home1():
    return render_template('home1.html')

@app.route('/predict' , methods=['POST','GET'])
def predict():
    inputs = [float(x) for x in request.form.values()]
    inputs = np.array([inputs])
    inputs = sc.transform(inputs)
    output = model.predict(inputs)
    if output < 0.5:
        output = 0
    else:
        output = 1
    return render_template('result.html' , prediction = output)


@app.route('/index')
def Predictor():
    return render_template('index.html')

@app.route('/Contact')
def contact():
    return render_template('Contact.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/hteam')
def hteam():
    return render_template('Team.html')



if __name__ =='__main__':
    app.config['TEMPLAES_AUTO_RELOAD']=True
    app.run(debug=True)