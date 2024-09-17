from flask import Flask,render_template,request
import pickle





app = Flask(__name__)

with open ('RFC_churn.pkl','rb') as f:
    model=pickle.load(f)

#by default method get
@app.route('/')   #it is use to routing path for url
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result',methods=['POST','GET'])
def result():
    tenure=float (request.form.get('utenure'))
    monthly=float(request.form.get('umonthly'))
    total=float(request.form.get('utotal'))
    gender=int( request.form.get('ugender'))
    phoneservice=float(request.form.get('phone_service'))
    internet=float(request.form.get('Internet'))
    device=float(request.form.get('device_protection'))
    Contract=float(request.form.get('contract'))
    paperless=float(request.form.get('PapaerLess'))
    Payment=float(request.form.get('payment'))

    input=[[tenure,monthly,total,gender,phoneservice,internet,device,Contract,paperless,Payment]]

    predict=model.predict(input)
    print(predict)
    if predict==[0] :
        result="No Churn"
    else:
        result="Churn"







    return render_template('result.html' ,res= result)


if __name__=='__main__':
    app.run(debug=True)