from flask import Flask, request, jsonify
import pandas as pd
import requests
from model import count_bags  # Import your image processing function

app = Flask(__name__)

# Define the fee structure for overage types
OVERAGE_FEES = {
    "1 bag over": 1.59,
    "Overloaded Cart": 3.07
}

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
        record_id = row['Event Id']
        image_url = row['3rd Eye Link']
        overage_type = row['Overage Type']
        
        # Calculate the fee based on the overage type
        fee = OVERAGE_FEES.get(overage_type, 0)
        
        # Count bags using the AI model
        bag_count = count_bags(image_url)

        # Total fee calculation
        total_fee = fee + (bag_count * fee) if bag_count > 5 else fee
        
        results.append({
            'RecordID': record_id,
            'BagCount': bag_count,
            'TotalFee': total_fee
        })

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
