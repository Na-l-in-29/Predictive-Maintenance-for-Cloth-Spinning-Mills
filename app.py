from flask import Flask, render_template, request
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('models/model.pkl', 'rb'))

# Define failure types mapping based on your provided labels
failure_types = {
    0: 'No Failure',
    1: 'Overstrain Failure',
    2: 'Power Failure',
    3: 'Random Failures',
    4: 'Tool Wear Failure'
}

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        air_temp = float(request.form['air_temp'])
        process_temp = float(request.form['process_temp'])
        rpm = float(request.form['rpm'])
        torque = float(request.form['torque'])
        tool_wear = float(request.form['tool_wear'])

        # Predict with the model
        prediction = model.predict([[air_temp, process_temp, rpm, torque, tool_wear]])

        # Get the predicted failure type
        predicted_failure = failure_types.get(prediction[0], 'Unknown Failure Type')

        # Return the result page with the prediction
        return render_template('result.html', prediction=predicted_failure)

    except KeyError as e:
        return f"Error: Missing key {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
