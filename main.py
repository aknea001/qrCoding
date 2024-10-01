from flask import Flask
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

app = Flask(__name__)

sqlConfig = {
    "host": "100.94.183.127",
    "user": "keali",
    "password": os.getenv("SQLPASSWD"),
    "database": "qrCoding"
}

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/<id>")
def checkID(id):
    db = None

    try:
        db = mysql.connector.connect(**sqlConfig)
        cursor = db.cursor(buffered=True)

        query = "SELECT id FROM qrs WHERE id = %s"
        cursor.execute(query, (id, ))
        result = cursor.fetchone()

        if result != None:
            return "Success"
        else:
            return "No viable qr with this ID"
        
    except mysql.connector.Error as e:
        return f"ERROR: {e}"
    finally:
        if db != None and db.is_connected():
            cursor.close()
            db.close()

if __name__ == "__main__":
    app.run(debug=True)