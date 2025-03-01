from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route('/')
def home():
    locations = util.get_location_names()
    return render_template('index.html', locations=locations, estimated_price=None)

@app.route('/predict_home_prices', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    
    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    locations = util.get_location_names()
    
    return render_template('index.html', locations=locations, estimated_price=estimated_price)

if __name__ == "__main__":
    print("Starting Python Flask Server for House Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)