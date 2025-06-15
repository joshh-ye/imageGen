import mimetypes

from googleapiclient.http import MediaFileUpload

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import streamlit as st
import json
from datetime import datetime

SCOPES = ['https://www.googleapis.com/auth/drive']


def get_credentials():
    creds = None

    # If token.json exists, load stored credentials
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If no valid creds, run the browser-based login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # This launches a browser window to log in
            config = json.loads(st.secrets["credentials"])
            flow = InstalledAppFlow.from_client_config(config, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for next time
        with open("token.json", "w") as token_file:
            token_file.write(creds.to_json())

    return creds


def upload_to_folder(folder_id, picPath):
    """Upload a file to the specified folder and prints file ID, folder ID
    Args: Id of the folder
    Returns: ID of the file uploaded

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    try:
        # create drive api client

        # using secrets.toml or get_credentials for local (non-streamlit)
        if "token" in st.secrets:
            tokenReadable = json.loads(st.secrets["token"])
            creds = Credentials.from_authorized_user_info(tokenReadable, SCOPES)
        else:
            creds = get_credentials()

        service = build("drive", "v3",
                        credentials=creds)  # creds modified for streamlit deployment. Set to creds if running locally (commented out above)

        file_metadata = {"name": f"uploaded_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}", "parents": [folder_id]}

        mimetype, _ = mimetypes.guess_file_type(picPath)

        media = MediaFileUpload(
            picPath, mimetype=mimetype, resumable=True
        )
        # pylint: disable=maybe-no-member
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )
        print(f'File ID: "{file.get("id")}".')
        return file.get("id")

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


if __name__ == "__main__":
    upload_to_folder(folder_id="1l_FSxH89e9iR6C32PcLWdqpJ3cdnEDPi", picPath='hi.txt')
