from sqlalchemy import URL, create_engine, text
import os

db_username = os.environ['DB_USERNAME']
db_password = os.environ['DB_PASSWORD']
db_host = os.environ['DB_HOST']
db_name = os.environ['DB_NAME']

url_object = URL.create(
    "mysql+mysqlconnector",
    username=db_username,
    password=db_password,
    host=db_host,
    database=db_name,
)
engine = create_engine(url_object)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"),
                              {"val": id})
        job = result.all()
        if len(job) == 0:
            return None
        else:
            return job[0]._asdict()


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO `applications`(job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
        )
        result = conn.execute(
            query, {
                "job_id": job_id,
                "full_name": data['full_name'],
                "email": data['email'],
                "linkedin_url": data['linkedin_url'],
                "education": data['education'],
                "work_experience": data['work_experience'],
                "resume_url": data['resume_url']
            })
        conn.commit()
