from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)


@app.route("/")
def home():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)


@app.route("/job/<id>")
def job(id):
    job = load_job_from_db(id)
    return render_template("jobpage.html", job=job)


@app.route("/job/<id>/apply", methods=["POST"])
def apply_job(id):
    data = request.form
    job = load_job_from_db(id)
    add_application_to_db(id, data)
    return render_template("application_submitted.html", application=data, job=job)


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route("/api/job/<id>")
def job_details(id):
    job = load_job_from_db(id)
    return jsonify(job)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
