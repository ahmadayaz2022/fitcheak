# Fitcheak - BMI & Health Advisor ⚖️💪

Fitcheak is a simple and interactive health advisory tool built using **Streamlit**. It allows users to calculate their **Body Mass Index (BMI)** and provides personalized health suggestions based on their BMI score.

## 🚀 Live Demo

Check out the live app hosted on Hugging Face Spaces:  
👉 [Fitcheak on Hugging Face](https://huggingface.co/spaces/ahmadayaz2022/FitCheck)

## 📋 Features

- 🧮 Calculates BMI using height and weight
- ✅ Provides personalized health advice based on BMI category
- 💡 Clean and modern user interface with custom styling
- 🌐 Deployed for public access on Hugging Face Spaces


## 📸 Screenshot

### ⚠️ Obese Category
![Obese](screenshot)

### ⚠️ Underweight Category
![Underweight](screenshot2)

### ✅ Healthy Weight Category
![Healthy](screenshot3)



## 🛠️ Technologies Used

- **Python 3**
- **Streamlit**
- **Hugging Face Spaces** (for deployment)


## 📁 Project Structure

fitcheak/
├── app.py               # Main Streamlit application
├── requirements.txt     # List of Python dependencies
└── README.md            # Project documentation

## 🧠 How BMI is Calculated
BMI is calculated using the formula:

ini
BMI = weight (kg) / (height (m))²
Based on your BMI, the app gives you health suggestions categorized as:

Underweight

Healthy

Overweight

Obese

## 🧑‍💻 Author
Ahmad Ayaz
📧 ahmadayaz2022@gmail.com

👉 [🌐Github](https://github.com/ahmadayaz2022)
[🔗 LinkedIn](https://www.linkedin.com/in/ahmadayaz99/)




## 📦 Installation & Run Locally

To run this project on your local machine:
```bash
# Clone the repository
git clone https://github.com/ahmadayaz2022/fitcheak.git

# Navigate to project directory
cd fitcheak

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
