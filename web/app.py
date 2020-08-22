from flask import Flask

app = Flask(__name__)

from web import routes  # noqa: E402, F401
