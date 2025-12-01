# 📧 Spam Email Classifier

This is a small project where I built a machine-learning model that can tell whether an email is **Spam** or **Ham (not spam)**. I used Python, TF-IDF, Logistic Regression, and Streamlit to make a simple web app where you can paste any email and instantly check if it looks suspicious.

The project takes raw message text, cleans it, turns it into numerical features, trains on a dataset of tagged emails, and then makes predictions in real time. The goal wasn’t to make a perfect enterprise-level solution, just something clean, simple, and useful to understand how spam classification works.

---

## 🚀 What this project does

- Loads a dataset with two columns:  
  **Category** → spam / ham  
  **Message** → the actual email text  
- Converts labels into numbers:  
  `spam → 0` and `ham → 1`
- Cleans the message text (removes URLs, punctuation, digits, extra spaces, etc.)
- Converts text into TF-IDF vectors
- Trains a Logistic Regression model
- Saves:
  - `feature_extraction.jb` (TF-IDF vectorizer)
  - `spam_model.jb` (trained ML model)
- Uses Streamlit to give a simple “Paste email → Get result” interface

---

## 🧠 How it works (simple explanation)

1. The dataset is split into training and testing parts.  
2. Text is transformed using TF-IDF, which basically turns words into numbers based on how important they are.  
3. A Logistic Regression model is trained to spot patterns that look like spam.  
4. When you run the Streamlit app, it uses the saved model to predict if a new email is spam or ham.  

It’s basically a text-cleaning → vectorization → prediction pipeline.

---

## 🧪 Streamlit App Flow

You type/paste an email →  
The app cleans and transforms it →  
Model predicts:  
- **1 = Ham**  
- **0 = Spam**

It then shows a simple message:

- ✔️ Ham  
- ❌ Spam

---

## 🛠️ How to run it

### 1. Clone this repo
```bash
git clone https://github.com/your-username/spam-email-classifier.git
cd spam-email-classifier
