# Fake News Detection App

## 📌 Features
- 📰 **Pandas** for data processing
- 🤖 **Scikit-learn** for machine learning (Logistic Regression)
- 💾 Model serialization with **joblib**
- 🌐 Web interface powered by **Streamlit**

## 🚀 Installation
### 📥 Clone the Repository
```bash
git clone https://github.com/your-username/fake-news-detection.git
cd fake-news-detection
```

### 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

## 📊 Dataset
- The model is trained using a dataset containing labeled fake and real news articles.
- Preprocessing includes text vectorization using **TF-IDF Vectorizer**.

## 🏋️ Model Training
- The dataset is preprocessed using **Pandas**.
- Text features are extracted using **TfidfVectorizer**.
- The model is trained using **Logistic Regression**.
- The trained model is saved using **joblib**.

## ▶️ Running the Streamlit App
```bash
streamlit run app.py
```

## 🛠️ Usage
1. Enter a news article text in the input box.
2. Click the **Detect** button.
3. The model will classify the article as **Real** or **Fake**.

## 🎮 Live Demo
Check out the live demo of the app here: [Fake News Detector](https://fake-news-detection3.streamlit.app/)
- Deployed at **Streamlit Community Cloud**

## 📌 Dependencies
```bash
# Required Libraries
Python 3.x
Pandas
Scikit-learn
Joblib
Streamlit
```

## 📜 License
This project is open-source under the MIT License.

---

💡 *Feel free to contribute and improve this project!* 🚀

