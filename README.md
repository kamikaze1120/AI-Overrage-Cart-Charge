# Garbage-Overage-Cart-Charge
AI bot that Tracks overage of Garbage and assigns appropriate fees to the associated record id.
Excel Processing: The process_excel function reads the Excel file and checks each record for overload.
Fee Calculation: The calculate_fee function determines the fee based on the number of overloaded bags.
Image Analysis: The analyze_images function retrieves an image from a URL and can be expanded to include image classification logic.
Running the Bot: The main function orchestrates the workflow.

Instructions to Run
Install Flask: If you haven't already, install Flask using pip:bash (pip install Flask)
Save the HTML: Save the HTML code in a file named index.html.
Run the Flask App: Save the modified bot.py and run it:bash (python bot.py)

Open the Interface: Open your web browser and go to http://127.0.0.1:5000. You may need to serve the HTML file using Flask or serve it through a simple HTTP server.

Note
The HTML form allows users to upload an Excel file, which is processed by the Flask backend.
The results are returned as JSON and displayed on the webpage.
You can enhance the image analysis part as needed.
