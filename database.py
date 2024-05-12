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