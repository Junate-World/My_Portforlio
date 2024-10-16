# Flask Portfolio Website

This is a Flask-based portfolio website showcasing personal projects, skills, and contact information. The website has multiple pages such as Home, About, Projects, and Contact.

## Features

- **Home Page**: Introduction and brief about yourself.
- **About Page**: Your bio, background, and skills.
- **Projects Page**: Display your projects, with descriptions and links.
- **Contact Page**: A contact form or contact details.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Junate-World/My_Portfolio
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo-name
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

   - On Windows:

    ```bash
    venv\Scripts\activate
    ```

   - On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the Flask application:

    ```bash
    python app.py
    ```

7. Open your browser and go to `http://127.0.0.1:5000/` to view your portfolio.

## File Structure

```plaintext
.
├── app.py              # Main Flask application file
├── templates           # Folder for HTML files
│   ├── index.html      # Home page
│   ├── about.html      # About page
│   ├── projects.html   # Projects page
│   └── contact.html    # Contact page
├── static              # Folder for static assets like CSS, JS, and images
│   ├── css
│   │   └── styles.css  # Main CSS file
├── .gitignore          # Git ignore file
├── README.md           # Project documentation
└── requirements.txt    # Dependencies file
#   M y _ P o r t f o r l i o 
 
 