# 1. Use `pip install Flask` to install the required libraries/modules.
# 2. Run the server using `python server.py`.

from flask import Flask, request, jsonify
from flask_cors import CORS


# Create a Flask application
app = Flask(__name__)
CORS(app) 

# Define a route and its handler
@app.route('/dip-req', methods=['GET'])
def hello():
    data = request.args.get('image_URL')
    print(data)
    if not data:
        return jsonify({"status": "Failure - Image not found"}), 404
        

    return jsonify({"status": "success", "written": "url which will have the output"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
