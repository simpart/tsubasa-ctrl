from flask import Flask
flask_app = Flask(__name__)

# 各ルーティングモジュールのインポートと初期化
from . import list
