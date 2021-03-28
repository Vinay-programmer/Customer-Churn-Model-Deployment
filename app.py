import numpy as np
import flask as Flask, requests, render_template
import pickle
app = Flask(__name__)
lr = pickle.load(open('lr.pkl','rb'))

@app.route('/')
def home():
    return render_template(index.html)

@app.route('/getprediction', methods=['POST']
def getprediction():
    input = [float(x) for x in request.form.value()]
    final_input = [np.array(input)]
    prediction = model.predict(final_input)


    return render_template('index.html', output = 'Churn out of customer: {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)

