# LocalCrafts - Connecting Users with Artisans

LocalCrafts is a web-based platform for showcasing and managing workshops. 
Users can view workshop details like the title, location, and price. The project uses Flask, PostgreSQL, and Docker for a complete backend-to-frontend experience.

## Features

- **Workshop Listings**: Display upcoming workshops
- **Pub/Sub Integration**: Integration with Google Pub/Sub for notifications
- **Scalable Setup**: Dockerized setup for easy deployment
- **User-Friendly Interface**: Interactive UI with a modern look and feel.


## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Pub/Sub**: Google Cloud Pub/Sub
- **Containerization**: Docker, Docker Compose

## Prerequisites

To run this project, you will need to have the following:

1. **Docker and Docker Compose**:
   - Install Docker from (https://www.docker.com/).

2. **Google Cloud Account**:
   - Set up a Google Cloud project.
   - Enable the **Pub/Sub API**.
   - Create a **service account** and download the JSON key file (`credentials.json`).
   - Grant **Pub/Sub roles** to the service account.


## Steps to Execute

1. Clone the repository and go to the project folder.
2. Place your credentials.json file in the main folder.
3. Run docker-compose up --build to start the application.
4. Open http://localhost:5001/workshops/ to check the workshop data.
5. Open http://localhost:5001 to view the homepage.


## File Structure

```plaintext
.
├── Dockerfile                # Docker setup for Flask app
├── docker-compose.yml        # Compose file for multi-container setup
├── app/
│   ├── main.py               # Main Flask application
│   ├── models.py             # Database models
│   ├── routes/               # Route definitions
│   │   ├── notifications.py  # Pub/Sub notification routes
│   │   ├── users.py          # User-related routes
│   │   └── workshops.py      # Workshop-related routes
│   ├── static/               # Static files
│   │   ├── scripts.js        # Frontend JavaScript
│   │   └── styles.css        # Frontend styling
│   └── templates/            # HTML templates
│       └── index.html        # Main template
├── credentials.json          # Google Cloud credentials for Pub/Sub
├── requirements.txt          # Python dependencies
├── wait-for-it.sh            # Script to wait for dependencies
└── README.md                 # Project documentation
```

## Interaction of Software and Hardware Components

**UI**: Users interact with the platform via a web interface to explore and book workshops.

**Data Storage and Processing**: Information about workshops, bookings, and user details is stored in PostgreSQL (managed by Docker) and processed for seamless operations.


**Queue Management**: Google Cloud Pub/Sub ensures efficient handling of asynchronous tasks like sending notifications and booking confirmations.


**Workshop Management**: Handles user requests to create, view, or book workshops by interacting with the database and responding through the REST API.


**Containerization**: Docker is used to containerize the application, ensuring consistency and easy deployment across environments.

