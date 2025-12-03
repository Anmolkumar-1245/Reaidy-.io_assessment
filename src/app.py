#This reads env variables and prints environment details.
from flask import Flask
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    env = os.getenv("ENVIRONMENT")
    log_level = os.getenv("LOG_LEVEL")
    db_url = os.getenv("DB_URL")
    return f"Hello from {env} environment!<br>Log Level: {log_level}<br>DB URL: {db_url}"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
