from wsgiref import simple_server
from flask import Flask, request, app,render_template
from flask import Response
from flask_cors import CORS
from logistic_deploy import predObj

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True


class ClientApi:

    def __init__(self):
        self.predObj = predObj()



@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predictRoute():
    try:
        Pregnancies=int(request.form['Pregnancies'])
        Glucose = int(request.form['Glucose Level'])
        BloodPressure = int(request.form['BloodPressure'])
        SkinThickness = int(request.form['SkinThickness'])
        Insulin = int(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = int(request.form['Age'])
        data = [[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
        print('data is:     ', data)
        pred=predObj()
        res = pred.predict_log(data)

        print('result is        ',res)
        return render_template('result.html', prediction_text='{}'.format(res))
    except ValueError:
        return Response("Value not found")
    except Exception as e:
        print('exception is   ',e)
        return Response(e)


if __name__ == "__main__":
    clntApp = ClientApi()
    #host = '0.0.0.0'
    #port = 5000
    app.run(debug=True)