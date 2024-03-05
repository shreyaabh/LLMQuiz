from flask import Flask, request, jsonify
from quiz import quiz_generator 

app = Flask(__name__)

@app.route('/quiz_generator', methods=['POST', 'GET'])
def generate_article():
    if request.method == 'POST':

        topic = request.form.get('topic') or request.json.get('topic')
        language = request.form.get('language') or request.json.get('language')
        article = quiz_generator(topic, language)
        return jsonify({'article': article})
    
    elif request.method == 'GET':
        topic = request.args.get('topic')
        language = request.args.get('language')
        article = quiz_generator(topic, language)
        return jsonify({'article': article})
        

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')