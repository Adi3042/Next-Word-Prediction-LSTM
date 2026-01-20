Before using this project, ensure you have the following prerequisites in place:

* Python (**3.11**)
* Required dependencies (install with `pip install -r requirements.txt`)
* Access to a web browser 🌐

---

## Installation 💻

##### Step 1 – Clone the repository to your local machine using Git

```bash
git clone https://github.com/Adi3042/Next-Word-Prediction-LSTM.git
cd Next-Word-Prediction-LSTM
```

---

##### Step 2 – Create a Conda environment after opening the repository

```bash
conda create -n venv python==3.11 -y
conda activate venv
```

---

##### Step 3 – Install the required dependencies

Open your terminal and execute the following command:

```bash
pip install -r requirements.txt
```

---

##### Step 4 – Run the Streamlit application server

Open your terminal and execute the following command:

```bash
streamlit run app.py
```

---

##### Step 5 – Use the Web Application

1. Visit the web app: 👉 [http://127.0.0.1:8501/](http://127.0.0.1:8501/)
2. Enter the **seed text** in the input box.
3. Select the **number of words** to generate.
4. Click **Generate** to see **real-time next-word prediction** using LSTM.