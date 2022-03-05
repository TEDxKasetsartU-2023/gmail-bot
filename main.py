# gmail bot
# | IMPORT SECTION
import base64
import mimetypes
import os
import pickle
import time

from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

# | GLOBAL VARIABLES
CREDENTIALS_FILENAME = "credentials.json"
MAIL_LIST_FILENAME = "mail_list.csv"
RESULT_FILENAME = "result.csv"
SCOPES = ["https://mail.google.com/"]
TOKEN_FILENAME = "token.pickle"

# | FUNCTIONS
def create_service():
    creds = None

    if os.path.exists(TOKEN_FILENAME):
        with open(TOKEN_FILENAME, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILENAME, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILENAME, "wb") as token:
            pickle.dump(creds, token)

    try:
        service = build("gmail", "v1", credentials=creds)
        print("service created successfully")
        return service
    except Exception as e:
        print("Unable to connect.")
        print(e)
        return None


def create_message_with_inline_image(receiver, subject, text, img):
    message = MIMEMultipart()
    message["to"] = receiver
    message["subject"] = subject

    msg = MIMEText(text, "html")
    message.attach(msg)

    if img is not None:
        content_type, encoding = mimetypes.guess_type(img)
        if content_type is None or encoding is not None:
            content_type = "application/octet-stream"
        main_type, sub_type = content_type.split("/", 1)
        if main_type == "image":
            with open(img, "rb") as fp:
                msg = MIMEImage(fp.read(), _subtype=sub_type)

        filename = os.path.basename(img)
        msg.add_header("Content-Id", "<image1>")
        msg.add_header("Content-Disposition", "inline", filename=filename)
        message.attach(msg)

    return {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}


def send_msg(service, user_id, message):
    try:
        res = service.users().messages().send(userId=user_id, body=message).execute()
        return res
    except HttpError as error:
        print(f"Error\n\n{error}")
        return None


def get_msg_from_file(file):
    with open(file, "rt", encoding="utf-8") as file:
        return file.read()


def replace_place_holder(string, old_string, new_string):
    return string.replace(old_string, new_string)


def from_csv_to_lst_of_dct(file):
    with open(file, "rt", encoding="utf-8") as file:
        data = file.readlines()
        data = [line.strip() for line in data if line.strip() != ""]
        return [
            {"name": line.split(",")[0], "email": line.split(",")[1]} for line in data
        ]


def create_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S")

# | MAIN
if __name__ == "__main__":
    if os.path.exists(TOKEN_FILENAME):
        os.remove(TOKEN_FILENAME)

    service = create_service()
    sending_lst = from_csv_to_lst_of_dct(MAIL_LIST_FILENAME)
    print(len(sending_lst))
    msg = get_msg_from_file("content.html")
    for r in sending_lst:
        name = r["name"]
        email = r["email"]
        print(f"{name} - {email}")
        r_msg = replace_place_holder(msg, "~~~", name)
        content = create_message_with_inline_image(
            email, "Some Header", r_msg, "TEDxKasetsartU_square.jpg"
        )
        res = send_msg(service, "me", content)
        print(res)
        print()
        with open(RESULT_FILENAME, "at", encoding="utf-8") as file:
            file.write(f"{name},{email},{'SENT' if res is not None else 'NOT SENT'},{create_timestamp()}\n")
        time.sleep(0.5)
