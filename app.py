import os
import traceback
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from google import genai

# 1. Chargement du .env
load_dotenv()

app = Flask(__name__)

# 2. Initialisation du client
_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=_api_key) if _api_key else None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    if not client:
        return jsonify({"error": "Clé API non configurée"}), 500

    data = request.get_json(silent=True) or {}
    question = data.get("question")

    if not question:
        return jsonify({"error": "Question manquante"}), 400

    try:
        # 3. PROMPT FUSIONNÉ
        prompt_complet = (
            "Consigne : Tu es un assistant juridique expert en droit français. "
            "Réponds de manière structurée et professionnelle.\n\n"
            f"Question : {question}"
        )

        # 4. UTILISATION DU MODÈLE IDENTIFIÉ DANS VOTRE LISTE
        # J'utilise 'models/gemini-flash-latest' car il est présent dans votre check_models.py
        response = client.models.generate_content(
            model="models/gemini-flash-latest", 
            contents=prompt_complet,
            config={
                "temperature": 0.2,
            }
        )

        return jsonify({"answer": response.text})

    except Exception as exc:
        traceback.print_exc()
        return jsonify({
            "error": "Erreur lors de la génération",
            "details": str(exc)
        }), 500

if __name__ == "__main__":
    # Port 8080 pour éviter les conflits Windows
    app.run(host="0.0.0.0", port=8080, debug=True)