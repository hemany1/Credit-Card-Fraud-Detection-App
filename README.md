Credit Card Fraud Detection App

This project is a Credit Card Fraud Detection App built using Streamlit. The app provides a user-friendly interface to input transaction details and predict the likelihood of fraudulent activity using a pre-trained machine learning model.

Features
	•	A machine learning model trained to detect fraudulent transactions.
	•	Streamlit-based web interface for user interaction.
	•	Input fields to provide transaction details.
	•	Real-time prediction of fraud likelihood.

Table of Contents
	•	Project Overview
	•	Setup and Installation
	•	Usage
	•	File Descriptions
	•	Technologies Used
	•	License

Project Overview

The app uses a machine learning model saved as a .pkl (pickle) file to classify transactions as either legitimate or fraudulent. It leverages Streamlit for the frontend and backend, providing a simple and interactive web application.

Setup and Installation

Prerequisites

Ensure you have the following installed:
	•	Python (>=3.7)
	•	pip (Python package manager)

Steps to Run Locally
	1.	Clone the Repository:

git clone https://github.com/hemany1/Credit-Card-Fraud-Detection-App.git
cd Credit-Card-Fraud-Detection-App


	2.	Install Dependencies:
Install the required Python packages:

pip install -r requirements.txt


	3.	Run the Application:
Start the Streamlit application:

streamlit run app.py


	4.	Access the App:
Open your web browser and go to:

http://localhost:8501

File Descriptions
	•	app.py: The main file that initializes and runs the Streamlit web application.
	•	predict.py: Contains the logic for processing inputs and making predictions using the pre-trained model.
	•	model.pkl: The serialized machine learning model used for predictions.
	•	requirements.txt: Lists the dependencies required to run the application.

Usage
	1.	Run the application as described above.
	2.	Enter the transaction details in the input fields provided in the Streamlit web app.
	3.	Click the “Predict” button to get the fraud prediction.

Technologies Used
	•	Python: Core programming language.
	•	Streamlit: Web framework for building interactive data applications.
	•	Pickle: Used for saving and loading the machine learning model.


Future Improvements
	•	Add more advanced features such as graphs or visualizations for better insights.
	•	Enhance the model’s accuracy with additional training data.
	•	Deploy the app to a cloud platform (e.g., Heroku, AWS, or Streamlit Community Cloud).

Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

