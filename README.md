# 🪨 Rock vs Mine Prediction (Machine Learning Project)

An end-to-end **Machine Learning project** that predicts whether an object detected by sonar signals is a **Rock or a Mine** using classification algorithms.

🚀 **Live Demo:** https://stonevsmine.streamlit.app/

---

## 📌 Project Overview

This project uses a dataset of sonar signals to classify objects into:

* 🪨 Rock
* 💣 Mine

The model learns patterns from the signal frequencies and predicts the correct category with high accuracy.

---

## 🎯 Features

* 📊 Data preprocessing and analysis
* 🤖 Machine Learning model training
* 📈 Prediction system
* 🌐 Interactive web app using Streamlit
* 🚀 Deployed and accessible online

---

## 🧠 Tech Stack

* **Python**
* **NumPy, Pandas**
* **Scikit-learn**
* **Streamlit**
* **Pickle (Model Saving)**

---

## 📂 Project Structure

```
stone_v-s_mine_ml_proj/
│
├── dataset/
│   └── rockvsmine.csv
│
├── app.py                  # Streamlit web app
├── main.py                 # Training script
├── RockVsMinePrediction.ipynb  # Jupyter notebook
├── rock_vs_mine_model.pkl  # Trained model
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

1. Load sonar dataset
2. Preprocess data
3. Train classification model
4. Save trained model (`.pkl`)
5. Use Streamlit UI for prediction

---

## 🚀 Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Just-Binod/stone_v-s_mine_ml_proj.git
cd stone_v-s_mine_ml_proj
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the app

```bash
streamlit run app.py
```

---

## 🌐 Deployment

This project is deployed using **Streamlit Cloud**, which allows easy deployment directly from GitHub repositories. ([Data Science Dojo][1])

👉 Live App: https://stonevsmine.streamlit.app/

---

## 📊 Dataset

* Sonar dataset (Rock vs Mine classification)
* Contains numerical signal features
* Used for binary classification

---

## 📸 Demo

Try the app by entering input values and get instant predictions!

---

## 💡 Future Improvements

* Improve model accuracy
* Add multiple ML models comparison
* Enhance UI/UX
* Add visualization dashboard

---

## 🙌 Author

**Binod Pant**

* GitHub: https://github.com/Just-Binod

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🤝 Contribute

---

## 📜 License

This project is open-source and available under the MIT License.

---

[1]: https://learn.datasciencedojo.com/wp-content/uploads/2024/12/Project-Deployment-on-Streamlit.pdf?utm_source=chatgpt.com "Project Deployment on Streamlit"
