# Flask CI/CD Pipeline

Automated deployment pipeline demonstrating DevOps practices with Flask, Docker, GitHub Actions, and AWS EC2.

## 🎯 Project Overview

End-to-end CI/CD implementation that automates testing, containerization, and deployment of a Flask REST API. Built to demonstrate modern DevOps workflows with focus on automation and security best practices.

**Start Date:** November 8, 2025  
**Status:** Week 1 - In Progress

---

## 🚀 Features

- **Flask REST API** with health check and data endpoints
- **Automated Testing** with pytest
- **Docker Containerization** with multi-stage builds
- **CI/CD Pipeline** using GitHub Actions
- **Automated Deployment** to AWS EC2
- **Security Best Practices** (secrets management, non-root containers)

---

## 📋 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message |
| `/health` | GET | Health check status |
| `/api/data` | GET | Sample data response |

---

## 🛠️ Tech Stack

- **Backend:** Python 3.x, Flask
- **Testing:** pytest
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Cloud:** AWS EC2
- **Version Control:** Git, GitHub

---

## 📦 Project Structure
```
flask-cicd-pipeline/
├── app/
│   ├── __init__.py       # Flask app initialization
│   └── routes.py         # API route definitions
├── tests/
│   └── test_app.py       # pytest test cases
├── .github/
│   └── workflows/
│       └── ci-cd.yml     # GitHub Actions pipeline
├── Dockerfile            # Multi-stage Docker build
├── requirements.txt      # Python dependencies
├── run.py               # Application entry point
└── README.md            # Project documentation
```

---

## 🚦 Getting Started

### Prerequisites

- Python 3.8+
- Docker (optional, for containerization)
- AWS account (for deployment)

### Local Development

1. **Clone the repository**
```bash
   git clone https://github.com/YOUR-USERNAME/flask-cicd-pipeline.git
   cd flask-cicd-pipeline
```

2. **Create virtual environment**
```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Run the application**
```bash
   python run.py
```

5. **Test the endpoints**
```bash
   curl http://127.0.0.1:5000/
   curl http://127.0.0.1:5000/health
   curl http://127.0.0.1:5000/api/data
```

### Running Tests
```bash
pytest tests/
```

### Docker
```bash
# Build image
docker build -t flask-cicd-app .

# Run container
docker run -p 5000:5000 flask-cicd-app
```

---

## 🔄 CI/CD Pipeline

The pipeline automatically:
1. ✅ Runs tests on every push
2. 🐳 Builds Docker image
3. 📦 Pushes image to Docker Hub
4. 🚀 Deploys to AWS EC2

**Pipeline Status:** [![CI/CD](https://github.com/YOUR-USERNAME/flask-cicd-pipeline/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/YOUR-USERNAME/flask-cicd-pipeline/actions)

---

## 📈 Week 1 Progress

- [x] Flask app with 3 routes
- [ ] pytest test suite
- [ ] Docker containerization
- [ ] GitHub Actions workflow
- [ ] AWS EC2 deployment
- [ ] Complete documentation

---

## 🔐 Security

- Secrets managed via GitHub Secrets
- Environment variables for sensitive data
- Docker containers run as non-root user
- Security groups restrict EC2 access

---

## 📝 What I Learned

- Flask application structure and routing
- Test-driven development with pytest
- Docker multi-stage builds for optimization
- GitHub Actions workflow configuration
- AWS EC2 deployment automation
- Secret management in CI/CD pipelines

---

## 🔮 Future Improvements

- [ ] Add database integration (PostgreSQL)
- [ ] Implement authentication (JWT)
- [ ] Add monitoring with Prometheus/Grafana
- [ ] Implement blue-green deployment
- [ ] Add API documentation (Swagger)
- [ ] Set up automated rollbacks

---

## 📧 Contact

**GitHub:** [@Pranav Ghorpade](https://github.com/ghorpadeire)  
**LinkedIn:** [Pranav Ghorpade](https://linkedin.com/in/pranav-ire)  
**Email:** pranav.ghorpade3108@gmail.com

---

## 📄 License

This project is for educational and portfolio purposes.

---

