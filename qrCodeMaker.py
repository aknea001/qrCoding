import qrcode
import qrcode.constants
from secrets import token_urlsafe

from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

qrID = token_urlsafe(16)

sqlConfig = {
    "host": "100.94.183.127",
    "user": "keali",
    "password": os.getenv("SQLPASSWD"),
    "database": "qrCoding"
}

def addToDB(time):
    db = None

    try:
        db = mysql.connector.connect(**sqlConfig)
        cursor = db.cursor(buffered=True)

        query = "INSERT INTO qrs (id, expiration) VALUES (%s, DATE_ADD(NOW(), INTERVAL %s HOUR));"
        cursor.execute(query, (qrID, time))
        db.commit()
    except mysql.connector.Error as e:
        print(f"ERROR: {e}")
        exit()
    finally:
        if db != None and db.is_connected():
            cursor.close()
            db.close()

def main():
    time = input("Hours: ")

    addToDB(time)

    qr.add_data(f"http://10.0.0.45:5000/{qrID}")
    qr.make(fit=True)

    img = qr.make_image()
    img.save(f"qr__{qrID}.png")

if __name__ == "__main__":
    main()