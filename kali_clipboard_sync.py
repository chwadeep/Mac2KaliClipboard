from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/sync", methods=["POST"])
def sync_clipboard():
    clipboard_data = request.form.get("clipboard", "")
    os.system(f"echo '{clipboard_data}' | xclip -selection clipboard")
    return "Clipboard synced"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
