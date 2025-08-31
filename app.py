from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
API_KEY = "962c44e9196c83a55e2b170b2a69ae3b"

@app.route('/weather')
def weather():
    lat=request.args.get('lat')
    lon=request.args.get('lon')
    
    if lat is None or lon is None:
        return jsonify({'error': 'Missing latitude or longitude'}), 400
    url = "http://api.weatherstack.com/current?access_key="+API_KEY+"&query=" +lat+","+lon
    response = requests.get(url)
    if response.status_code !=200:
        return jsonify({'error': 'Weather data not found'}), 500
    data=response.json()
    location=data['location']['name']
    temperature = data['current']['temperature']
    description = data['current']['weather_descriptions'][0]
    
    return jsonify({
        'location':location,
        'temperature':temperature,
        'description':description
    })
    
if __name__ == '__main__':
    app.run(debug=True)
