from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv("DB_USER")
db_name = os.getenv("DB_NAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

port = os.getenv("PORT")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)
