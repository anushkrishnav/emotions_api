import threading
import asyncio
from flask import Flask, jsonify, request
from score import get_video, process_data, score_data

print(f"In flask global level: {threading.current_thread().name}")
app = Flask(__name__)

@app.route("/score", methods=["POST"])
def index():
    content = request.json
    link, user = content["link"], content["user"]
    link = get_video(link, user)
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(process_data(link, user))
    df = score_data(result)
    df["user"] = user
    return jsonify(df)

@app.route("/", methods=["GET"])
def home():
    return "Hello World!"


  
if __name__ == "__main__":
    app.run()
