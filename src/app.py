import os
import pathlib
from functools import lru_cache  # cache the os variables so that they are not loaded each time from os variable
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent  # means src directory

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


# http://localhost:4000/abc # route --> # path
# https://www.awesomesite.com/abc

# print('AIRTABLE_BASE_ID', os.environ.get('AIRTABLE_BASE_ID'))  # get the os variable here but data is not loaded

@lru_cache
def cached_dotenv():
    load_dotenv()  # load the data


cached_dotenv()
print('AIRTABLE_BASE_ID', os.environ.get('AIRTABLE_BASE_ID'))  # show the data now


@app.get('/')
def home_view(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post('/')
def home_signup_view(request: Request, email: str = Form(...)):
    """
    TODO add csrf for security
    """
    # to send email to airtable.

    return templates.TemplateResponse("home.html", {"request": request, "submitted_email": email})
