from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_path):
    text = ""

    reader = PdfReader(pdf_path)

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text


def rank_resumes(job_description, resume_files):
    documents = [job_description]

    for file in resume_files:
        documents.append(extract_text_from_pdf(file))

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_scores = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    ).flatten()

    rankings = []

    for file, score in zip(resume_files, similarity_scores):
        rankings.append({
            "resume": file.split("\\")[-1],
            "score": round(score * 100, 2)
        })

    rankings.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return rankings