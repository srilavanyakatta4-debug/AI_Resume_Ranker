# AI Resume Ranker

## 📌 Project Overview

AI Resume Ranker is a Python-based web application that automatically ranks resumes based on their similarity to a given job description. It uses Natural Language Processing (NLP) techniques and TF-IDF vectorization with Cosine Similarity to identify the most relevant candidates.

This project helps recruiters and HR professionals quickly shortlist resumes by comparing candidate profiles with job requirements.

---

## 🚀 Features

- Upload multiple PDF resumes
- Enter a job description
- Extract text from PDF resumes
- Compare resumes with the job description
- Rank resumes based on similarity score
- Display the top candidate
- Simple and user-friendly web interface using Flask

---

## 🛠️ Technologies Used

- Python 3.x
- Flask
- Scikit-learn
- PyPDF2
- HTML
- TF-IDF Vectorizer
- Cosine Similarity

---

## 📂 Project Structure

```
AI_Resume_Ranker/
│
├── app.py
├── ranker.py (optional)
├── resumes/
├── requirements.txt
├── README.md
└── templates/ (optional)
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI_Resume_Ranker.git
```

### 2. Navigate to the project folder

```bash
cd AI_Resume_Ranker
```

### 3. Create a virtual environment (Optional)

```bash
conda create -n resume_ranker python=3.11
```

Activate the environment

```bash
conda activate resume_ranker
```

### 4. Install dependencies

```bash
pip install flask
pip install PyPDF2
pip install scikit-learn
```

or

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Start the Flask server

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📖 How to Use

1. Open the application.
2. Upload one or more PDF resumes.
3. Enter the job description.
4. Click **Rank Resumes**.
5. View the ranked resumes along with their similarity scores.
6. The highest-ranked resume is displayed as the **Top Candidate**.

---

## ⚙️ How It Works

1. User uploads PDF resumes.
2. The application extracts text using **PyPDF2**.
3. The job description and resume texts are converted into TF-IDF vectors.
4. Cosine Similarity is calculated between the job description and each resume.
5. Resumes are ranked based on similarity scores.
6. Results are displayed in descending order.

---

## 📸 Sample Output

```
Resume Rankings

1. John_Doe.pdf → 89.45%

2. Smith.pdf → 84.20%

3. David.pdf → 76.10%

Top Candidate:
John_Doe.pdf
```

---

## 📌 Future Enhancements

- Better UI using Bootstrap
- Drag-and-drop resume upload
- Support for DOCX resumes
- Resume keyword highlighting
- Resume score visualization using charts
- Export ranking results to Excel or PDF
- AI-powered resume summarization
- Resume feedback and suggestions

---

