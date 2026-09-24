import os
from flask import Flask, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=BASE_DIR)

DOMAIN = "twinity.localhost"
PORT = 80  # Default HTTP port (no :port needed in browser)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    print(f"\n==================================================")
    print(f" 🚀 Twinity Search Online")
    print(f" URL: http://{DOMAIN}")
    print(f" (Fallback: http://127.0.0.1:{PORT})")
    print(f"==================================================\n")

    try:
        app.run(host='0.0.0.0', port=PORT, debug=True)
    except PermissionError:
        print("\n[!] Port 80 requires Administrator/sudo privileges.")
        print("[!] Falling back to port 5000...")
        app.run(host='0.0.0.0', port=5000, debug=True)
