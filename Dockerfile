# Utiliser une image Python légère
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code du projet
COPY . .

# Définir le port (Cloud Run utilise 8080 par défaut)
ENV PORT 8080

# Lancer l'application avec Gunicorn (plus robuste que le serveur de test Flask)
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app