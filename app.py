from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

# File to store completed projects
COMPLETED_PROJECTS_FILE = 'completed_projects.json'

# Centralized project data - this is where you manage all projects
PROJECTS_DATA = [
    {
        "id": "1",
        "title": "Email Automation",
        "description": "This script sends a daily motivational email using Python. It uses the `smtplib` library for sending emails and the `schedule` library for scheduling the email to be sent at a specific time each day.",
        "tags": ["Python", "smtplib", "schedule", "Automation"],
        "links": {
            "github": "https://github.com/Junate-World/email-automation",
            "demo": "https://github.com/Junate-World/email-automation",
            "documentation": "https://github.com/Junate-World/email-automation"
        }
    },
    {
        "id": "2",
        "title": "Image-Uploader-Application",
        "description": "This is a simple image uploader application built using Flask, a micro web framework for Python. The application allows users to upload images, view uploaded images, and delete images.",
        "tags": ["Flask", "Python", "File Upload", "Web App"],
        "links": {
            "github": "https://github.com/Junate-World/image-uploader",
            "demo": "https://github.com/Junate-World/image-uploader",
            "documentation": "https://github.com/Junate-World/image-uploader"
        }
    },
    {
        "id": "3",
        "title": "JW-Flask-form",
        "description": "A Flask application to collect and manage user information.",
        "tags": ["Flask", "Forms", "Data Collection"],
        "links": {
            "github": "https://github.com/Junate-World/jw-flask-form",
            "demo": "https://github.com/Junate-World/jw-flask-form"
        }
    },
    {
        "id": "4",
        "title": "QR-Code-Generator",
        "description": "This is a Python script to generate QR codes from input text or data. The QR code is saved as an image file in PNG format.",
        "tags": ["Python", "QR Code", "Image Generation"],
        "links": {
            "github": "https://github.com/Junate-World/qr-generator",
            "demo": "https://github.com/Junate-World/qr-generator"
        }
    },
    {
        "id": "5",
        "title": "Motion Detector",
        "description": "This project is a basic motion detector implemented using Python and OpenCV. It captures video from a webcam and detects motion by applying background subtraction.",
        "tags": ["Python", "OpenCV", "Computer Vision", "Motion Detection"],
        "links": {
            "github": "https://github.com/Junate-World/motion-detector",
            "demo": "https://github.com/Junate-World/motion-detector"
        }
    },
    {
        "id": "6",
        "title": "Graph Bar",
        "description": "This project is designed to visualize the tower heights of various IHS sites using data stored in an Excel file. The visualization is performed using Matplotlib and pandas.",
        "tags": ["Python", "Matplotlib", "Pandas", "Data Visualization"],
        "links": {
            "github": "https://github.com/Junate-World/graph-bar",
            "demo": "https://github.com/Junate-World/graph-bar"
        }
    },
    {
        "id": "7",
        "title": "ChatGPT Clone",
        "description": "This is a simple Flask web application that interacts with the OpenAI GPT-3.5 model to create a chatbot. Users can send messages to the bot, and it will respond accordingly using OpenAI's API.",
        "tags": ["Flask", "OpenAI API", "Chatbot", "AI"],
        "links": {
            "github": "https://github.com/Junate-World/chatgpt-clone",
            "demo": "https://github.com/Junate-World/chatgpt-clone"
        }
    },
    {
        "id": "8",
        "title": "Mobile-Geolocation-Tracker",
        "description": "A simple Tkinter application that tracks the location of a phone number and displays it on a map using the OpenCage Geocode API and Folium.",
        "tags": ["Python", "Tkinter", "Geolocation", "Maps"],
        "links": {
            "github": "https://github.com/Junate-World/geolocation-tracker",
            "demo": "https://github.com/Junate-World/geolocation-tracker"
        }
    },
    {
        "id": "9",
        "title": "Hangman Game",
        "description": "This is a simple Hangman game implemented in Python. The game is played by guessing letters and guessing the correct word.",
        "tags": ["Python", "Game", "CLI"],
        "links": {
            "github": "https://github.com/Junate-World/hangman-game",
            "demo": "https://github.com/Junate-World/hangman-game"
        }
    },
    {
        "id": "10",
        "title": "Number Guess Game",
        "description": "This is a simple number guess game in Python. The game is played by guessing a number between 1 and 100.",
        "tags": ["Python", "Game", "CLI"],
        "links": {
            "github": "https://github.com/Junate-World/number-guess",
            "demo": "https://github.com/Junate-World/number-guess"
        }
    },
    {
        "id": "11",
        "title": "Resume Builder",
        "description": "A Flask-based web application that allows users to dynamically create and generate professional resumes in PDF format.",
        "tags": ["Flask", "PDF Generation", "Web App"],
        "links": {
            "github": "https://github.com/Junate-World/resume-builder",
            "demo": "https://github.com/Junate-World/resume-builder"
        }
    },
    {
        "id": "12",
        "title": "Distributed Web Scraper",
        "description": "This project is a distributed web scraper built using **Scrapy** and **Selenium**. It is designed to handle websites with dynamic content (JavaScript-rendered) and allows for scalable scraping of multiple websites.",
        "tags": ["Python", "Scrapy", "Selenium", "Web Scraping"],
        "links": {
            "github": "https://github.com/Junate-World/web-scraper",
            "demo": "https://github.com/Junate-World/web-scraper"
        }
    },
    {
        "id": "13",
        "title": "Voice Activated Chatbot With Learning Ability",
        "description": "This is a Python-based voice-activated chatbot that can recognize your speech, match your question to a knowledge base, and provide an appropriate response using text-to-speech (TTS). If the chatbot doesn't know the answer, you can teach it new responses that are saved to the knowledge base for future conversations.",
        "tags": ["Python", "Speech Recognition", "Text-to-Speech", "AI", "Machine Learning"],
        "links": {
            "github": "https://github.com/Junate-World/voice-chatbot",
            "demo": "https://github.com/Junate-World/voice-chatbot"
        }
    },
    {
        "id": "14",
        "title": "Project Management Web App",
        "description": "A simple Flask-based task management application with user registration, login, password reset functionality (via email), and basic CRUD operations on tasks. Password reset is powered by SendGrid through Flask-Mail.",
        "tags": ["Flask", "Python", "JavaScript", "CSS", "HTML", "SendGrid", "Flask-Mail"],
        "links": {
            "github": "https://github.com/Junate-World/junate",
            "demo": "https://junate.onreader.com/"
        }
    },
    {
        "id": "15",
        "title": "Family Tree Web App",
        "description": "This is a web-based family management and genealogy app built with Flask. It allows registered users to add, edit, view, and delete family members, and visualize family relationships through a family tree interface.",
        "tags": ["Python", "JavaScript", "CSS", "HTML", "Flask", "Genealogy"],
        "links": {
            "github": "https://github.com/Junate-World/family-website",
            "demo": "https://family-website.ll5z.onrender.com/"
        }
    },
    {
        "id": "16",
        "title": "PDF Merger & Encryptor",
        "description": "This is a Flask-based web application that allows users to upload multiple PDF files, merge them into a single PDF, and optionally encrypt the merged output with a password.",
        "tags": ["Python", "JavaScript", "CSS", "HTML", "Flask", "PDF Processing"],
        "links": {
            "github": "https://github.com/Junate-World/pdf-merger-encryptor",
            "demo": "https://github.com/Junate-World/pdf-merger-encryptor"
        }
    }
]

def load_completed_projects():
    """Load completed projects from JSON file"""
    if os.path.exists(COMPLETED_PROJECTS_FILE):
        with open(COMPLETED_PROJECTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_completed_projects(completed_projects):
    """Save completed projects to JSON file"""
    with open(COMPLETED_PROJECTS_FILE, 'w') as f:
        json.dump(completed_projects, f)

#The decorators for each route.
@app.route('/')
def home():
    completed_projects = load_completed_projects()
    completed_ids = [p['id'] for p in completed_projects]
    return render_template('index.html', projects=PROJECTS_DATA, completed_projects=completed_ids)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS_DATA)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/complete-project', methods=['POST'])
def complete_project():
    """Backend route to mark a project as completed"""
    try:
        data = request.get_json()
        project_id = data.get('project_id')
        project_title = data.get('project_title')
        
        if not project_id:
            return jsonify({'error': 'Project ID is required'}), 400
        
        # Load current completed projects
        completed_projects = load_completed_projects()
        
        # Add project to completed list if not already there
        project_info = {
            'id': project_id,
            'title': project_title,
            'completed_at': request.get_json().get('timestamp', '')
        }
        
        if project_info not in completed_projects:
            completed_projects.append(project_info)
            save_completed_projects(completed_projects)
        
        return jsonify({
            'success': True,
            'message': f'Project "{project_title}" marked as completed',
            'completed_projects': completed_projects
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/completed-projects')
def get_completed_projects():
    """Get list of completed projects"""
    try:
        completed_projects = load_completed_projects()
        return jsonify({
            'success': True,
            'completed_projects': completed_projects
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
