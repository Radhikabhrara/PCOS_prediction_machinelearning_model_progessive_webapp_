import os
import pickle
import numpy as np
from flask import Flask, request, render_template
y="general_information.pkl" 
z="general_and_medical_information.pkl"
model = pickle.load(open(y, 'rb')) 
mod = pickle.load(open(z, 'rb')) 
# Create application
app = Flask(__name__,template_folder='templates')

# Bind home function to URL
@app.route('/')
def home():
    return render_template("menu.html")
@app.route('/general_information')
def general_information():
	
	return render_template("general_information.html")
@app.route('/general_and_medical_information')
def general_and_medical_information():
	
	return render_template("general_and_medical_information.html")
@app.route('/predict', methods =['POST'])
def predict():
	
    # Put all form entries values in a list 
    int_features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(int_features)]
    # Predict features
    prediction = model.predict(array_features)
    output = prediction
    # Check the output values and retrive the result with html tag based on the value
    if output == 0:
        return render_template('general_information.html', 
                               result = 'The patient is not likely to have PCOS!')
    else:
        return render_template('general_information.html', 
                               result = 'The patient is likely to have PCOS!')


@app.route('/pred', methods =['POST'])
def pred():
	
    # Put all form entries values in a list 
    int_features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(int_features)]
    # Predict features
    prediction = mod.pred(array_features)
    output = prediction
    # Check the output values and retrive the result with html tag based on the value
    if output == 0:
        return render_template('general_and_medical_information.html', 
                               result = 'The patient is not likely to have PCOS!')
    else:
        return render_template('general_and_medical_information.html', 
                               result = 'The patient is likely to have PCOS!')

if __name__ == '__main__':
#Run the application
    app.run(debug=True)
