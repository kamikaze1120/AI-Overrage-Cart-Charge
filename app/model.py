import requests
from PIL import Image
import io

def count_bags(image_url):
    # Fetch the image
    response = requests.get(image_url)
    img = Image.open(io.BytesIO(response.content))
    
    # Here you would implement your AI model logic
    # For demonstration, let's assume a mock function
    return mock_bag_count(img)

def mock_bag_count(image):
    # Mock function to simulate counting bags
    return 5  # Replace with actual model prediction logic
