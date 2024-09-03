from flask import Flask
app = Flask(__name__)

# 各ルーティングモジュールのインポートと初期化
from . import list
