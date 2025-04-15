from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        contact = request.form["contact"]
        email = request.form["email"]
        # Store or validate if needed
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    result = None
    amplitude_questions = []

    if request.method == "POST":
        student_class = request.form["student_class"]
        subject = request.form["subject"]
        pdf = request.files["pdf"]
        
        if pdf:
            text = extract_text_from_pdf(pdf)
            result = generate_summary(text, subject)
            amplitude_questions = generate_amplitude_questions(student_class)

    return render_template("dashboard.html", result=result, amplitude_questions=amplitude_questions)
