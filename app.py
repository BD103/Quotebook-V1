import os

import quotebook

app = quotebook.create_app(__name__)
app.secret_key = os.getenv("SECRET_KEY")
