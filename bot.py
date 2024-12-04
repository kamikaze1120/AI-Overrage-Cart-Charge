from flask import Flask, request, jsonify
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Define the overload threshold
threshold = 5

# Function to calculate fees based on overloaded bags
def calculate_fee(bags_count):
    base_fee = 10  # Base fee per bag
    return (bags_count - threshold) * base_fee

# Function to access and analyze images
def analyze_images(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()  # This is just for demonstration

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    df = pd.read_excel(file)
    results = []
    
    for index, row in df.iterrows():
        record_id = row['RecordID']
        bags_count = row['BagsCount']
        
        if bags_count > threshold:
            fee = calculate_fee(bags_count)
            results.append({
                'RecordID': record_id,
                'Overloaded Bags': bags_count,
                'Fee Assigned': fee
            })
            # Here you could assign the fee to the specified account
            # assign_fee_to_account(record_id, fee)

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
