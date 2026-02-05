## **Next-Word-Prediction-LSTM**

Given three words of a sentence, it should predict next word. I am using LSTM (Long-Short Term Memory) here.

- LSTM stands for Long-Short Term Memory and it is type of recurrent neural network(RNN) architecture that is specially designed to overcome the problem of vanishing gradients in traditional RNNs.
- LSTM stands for Long-Short Term Memory and it is type of recurrent neural network(RNN) architecture that is specially designed to overcome the problem of vanishing gradients in traditional RNNs.
- LSTM stands for Long-Short Term Memory and it is type of recurrent neural network(RNN) architecture that is specially designed to overcome the problem of vanishing gradients in traditional RNNs.
- LSTM networks are particularly well-suited to tasks that require modeling long-term dependencies between input sequences, such as language modeling, speech recognition, and machine translation.
- In an LSTM network, each cell has a "memory" component that can selectively retain or forget information over time.
- The network uses input, output, and forget gates to control the flow of information into and out of the memory cell.
- These gates can be thought of as filters that decide what information should be retained or discarded based on the current input and the previous state of the network.
- LSTM can be used for next word prediction in natural language processing (NLP) tasks.
- In this context, the LSTM network is trained on a large corpus of text to learn the patterns and relationships between words in a sentence or a document.
- At each time step, the LSTM takes in a sequence of words as input and predicts the probability distribution over the vocabulary of possible next words.
- This probability distribution is then used to sample the next word, which becomes the input for the next time step.
- The advantage of using LSTM for next word prediction is that it can capture long-term dependencies between words and phrases in the input sequence.
- This means that the network can use information from earlier parts of the sequence to make more accurate predictions about the next word.

Overall, LSTM can help improve the accuracy and fluency of next word prediction in NLP tasks by leveraging its ability to model long-term dependencies and selectively retain or forget information from the input sequence.

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
