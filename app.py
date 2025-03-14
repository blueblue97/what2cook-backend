from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    ingredients = data.get('ingredients', '')

    prompt = f"Create a delicious recipe using these ingredients only: {ingredients}. Clearly list ingredients and step-by-step instructions."

    try:
        response = openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400,
            temperature=0.7
        )

        recipe = response.choices[0].message.content.strip()
        return jsonify({"recipe": recipe})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
