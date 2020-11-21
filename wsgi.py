from app.main import app
from os import getenv
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    app.run(host = "0.0.0.0", port = getenv("APP_PORT"), debug = getenv("APP_DEBUG") == "true")
