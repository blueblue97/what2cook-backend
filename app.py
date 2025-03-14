from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = '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'

@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    ingredients = data.get('ingredients', '')

    prompt = f"Create a delicious recipe using these ingredients only: {ingredients}. Clearly list ingredients and step-by-step instructions."

    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400,
            temperature=0.7
        )

        recipe = response['choices'][0]['message']['content'].strip()
        return jsonify({"recipe": recipe})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
