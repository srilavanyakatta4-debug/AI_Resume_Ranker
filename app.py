from flask import Flask, request
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)

UPLOAD_FOLDER = "resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        reader = PdfReader(pdf_path)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    except Exception as e:
        print("PDF Error:", e)

    return text


@app.route("/", methods=["GET", "POST"])
def home():

    html = """
    <html>
    <head>
        <title>AI Resume Ranker</title>
    </head>
    <body>

        <h1>AI Resume Ranker</h1>

        <form method="POST" enctype="multipart/form-data">

            <h3>Upload Resumes (PDF)</h3>

            <input type="file" name="resumes[]" multiple required>

            <br><br>

            <h3>Job Description</h3>

            <textarea name="job_description"
                      rows="10"
                      cols="80"
                      required></textarea>

            <br><br>

            <button type="submit">Rank Resumes</button>

        </form>
    """

    if request.method == "POST":

        job_description = request.form["job_description"]
        uploaded_files = request.files.getlist("resumes[]")

        # Debugging
        print(uploaded_files)
        print(len(uploaded_files))

        html += f"<h3>Files Uploaded: {len(uploaded_files)}</h3>"

        resume_paths = []

        for file in uploaded_files:

            if file.filename:

                filepath = os.path.join(
                    UPLOAD_FOLDER,
                    file.filename
                )

                file.save(filepath)

                resume_paths.append(filepath)

                html += f"<p>{file.filename}</p>"

        if len(resume_paths) > 0:

            documents = [job_description]

            for resume in resume_paths:
                documents.append(
                    extract_text_from_pdf(resume)
                )

            vectorizer = TfidfVectorizer(stop_words="english")

            tfidf = vectorizer.fit_transform(documents)

            scores = cosine_similarity(
                tfidf[0:1],
                tfidf[1:]
            ).flatten()

            results = []

            for resume, score in zip(resume_paths, scores):
                results.append(
                    (
                        os.path.basename(resume),
                        round(score * 100, 2)
                    )
                )

            results.sort(
                key=lambda x: x[1],
                reverse=True
            )

            html += "<hr>"
            html += "<h2>Resume Rankings</h2>"

            for i, (name, score) in enumerate(results, start=1):
                html += f"<p>{i}. {name} → {score}%</p>"

            html += f"<h3>Top Candidate: {results[0][0]}</h3>"

    html += """
    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(debug=True)