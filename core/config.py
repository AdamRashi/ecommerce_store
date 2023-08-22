import os
from dotenv import load_dotenv
import pathlib


dotenv_path = pathlib.Path(__file__).parents[1] / ".env.example"
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


SECRET_KEY = os.getenv("SECRET_KEY")
