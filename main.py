from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        # Process data
        return jsonify({"message": "Data received successfully"}), 201

    except Exception as e:
        app.logger.error(f"Error processing data: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    import os
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')