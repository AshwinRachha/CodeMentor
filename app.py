from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/explain', methods=['POST'])
def explain_code():
    code = request.form['code']
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Explain the following Python code: \"{code}\" Line by line.",
        max_tokens=150,
        temperature=0
    )
    explanation = response.choices[0].text.strip()
    return explanation

if __name__ == '__main__':
    app.run(debug=True)
