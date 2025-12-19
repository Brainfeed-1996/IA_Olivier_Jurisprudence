# ⚖️ JurisExpert : Assistant Legal Tech

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/flask-%23000.svg?logo=flask&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-AI-orange?logo=googlegemini)
![License](https://img.shields.io/badge/license-MIT-green)

**JurisExpert** est une application intelligente conçue pour analyser des problématiques juridiques complexes (comme les *Management Fees* en schémas de Holding). Elle utilise l'IA de Google (Gemini) pour transformer des questions brutes en analyses structurées.

---

## 📑 Sommaire

- [🚀 Installation et Configuration](#-installation-et-configuration)
- [📂 Structure du Projet](#-structure-du-projet)
- [⚙️ Le Coeur du Système (Backend)](#️-le-coeur-du-système-backend)
- [💻 L'Interface Utilisateur (Frontend)](#-linterface-utilisateur-frontend)
- [🛠️ Dépannage (Troubleshooting)](#️-dépannage-troubleshooting)
- [🔮 Évolutions Futures](#-évolutions-futures)

---

## 🚀 Installation et Configuration

### 1. Prérequis
* **Python 3.11** ou supérieur.
* Une clé API valide depuis [Google AI Studio](https://aistudio.google.com/).
* Un éditeur de code (VS Code recommandé).

### 2. Étape 1 : Préparation de l'environnement

Ouvrez votre terminal et créez un environnement virtuel pour isoler le projet :

```bash
# Création de l'environnement
python -m venv venv

# Activation (Windows)
venv\Scripts\activate

# Activation (Mac/Linux)
source venv/bin/activate

```
### 3. Étape 2 : Installation des bibliothèques
```bash
pip install flask python-dotenv google-genai
```


### 4. Étape 3 : Configuration du fichier .env
Créez un fichier nommé .env à la racine et collez-y vos identifiants :

```plaintext

GEMINI_API_KEY=VOTRE_CLE_API_ICI
PORT=8080
```
### 📂 Structure du Projet
```plaintext

IA_Olivier_Jurisprudence/
├── app.py              # Le cerveau (Flask + Gemini)
├── .env                # Vos secrets (Clé API) - NE PAS PARTAGER
├── requirements.txt    # Liste des outils Python
├── check_models.py     # Diagnostic de votre accès API
└── templates/          # Dossier des pages web
    └── index.html      # L'interface visuelle (HTML/CSS/JS)

```
### ⚙️ Le Coeur du Système (Backend)
Le fichier app.py utilise une logique de Prompt Engineering sécurisée :

Modèle utilisé : models/gemini-flash-latest (ou adapté selon check_models.py).

Sécurité : Les instructions système sont fusionnées au message utilisateur pour garantir la stabilité des réponses.

Port Réseau : Le port 8080 est forcé pour éviter les conflits de sécurité Windows courants (Error 10013).

### 💻 L'Interface Utilisateur (Frontend)
L'interface index.html a été conçue pour offrir une expérience Premium :

Design Adaptatif : Support du Mode Sombre (Dark Mode) automatique.

Rendu Markdown : Les listes et le gras s'affichent proprement grâce à la librairie Marked.js.

UX : Un "Spinner" de chargement indique visuellement que l'analyse est en cours.

### 🛠️ Dépannage (Troubleshooting)
> [!TIP]
> **Erreur 404 (Model Not Found)** : Lancez `python check_models.py`. Ce script interroge Google pour lister les modèles exacts auxquels votre projet a droit.

> [!IMPORTANT]
> **Erreur 500 (Internal Server Error)** : Vérifiez votre terminal. Le message d'erreur s'y affichera en rouge avec les détails de la ligne en cause.

> [!WARNING]
> **Erreur de Port (Permission Denied)** : Assurez-vous qu'aucune autre instance de `app.py` ne tourne. Fermez le terminal et relancez-le si nécessaire.
### 🔮 Évolutions Futures
[ ] Export PDF : Transformer l'analyse en document officiel d'un clic.

[ ] Mémoire : Implémenter une base de données pour l'historique des échanges.

[ ] Multi-modèles : Sélecteur pour passer de Gemini Flash à Gemini Pro.

### Visuel

[![JurisExpert](https://i.postimg.cc/SxQDJyZ8/Capture-d-ecran-2025-12-19-160857.jpg)](https://postimg.cc/tYfhcHGC)

[!CAUTION] Note Juridique : Cet outil est un assistant à la décision. L'analyse finale doit toujours être validée par un professionnel qualifié.
