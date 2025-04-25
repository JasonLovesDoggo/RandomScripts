# /// script
# dependencies = [
#   "flask<3",
# ]
# ///

from flask import Flask, send_from_directory, request
import os

# Create the Flask app
app = Flask(__name__)

# Root directory to serve files from
ROOT_DIRECTORY = "/path/to/serve"

@app.route('/<path:filename>', methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE'])
@app.route('/', methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE'])
def serve_file(filename=''):
    # Log request details
    print(f"Request Method: {request.method}")
    print(f"Headers:\n{request.headers}")
    
    if not filename:
        filename = "index.html"  # Default file if no path is given
    
    file_path = os.path.join(ROOT_DIRECTORY, filename)
    if os.path.isfile(file_path):
        return send_from_directory(ROOT_DIRECTORY, filename)
    else:
        return "File not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

