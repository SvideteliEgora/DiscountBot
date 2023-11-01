from dotenv import load_dotenv
import os

load_dotenv('venv/.env')

TOKEN = os.environ.get('TOKEN')
