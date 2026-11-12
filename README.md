Markdown
# Automated CI/CD Pipeline with Monitoring on AWS

This repository contains the source code, deployment workflows, and monitoring configuration for a containerized Python FastAPI application. The project demonstrates a fully automated CI/CD pipeline, infrastructure configuration on AWS EC2, and a comprehensive observability stack.

## 🚀 Architecture Overview
1. **Developer Push:** Code is pushed to the `main` branch on GitHub.
2. **CI/CD Automation:** GitHub Actions triggers a build process, runs automated tests, builds a multi-stage Docker image, and securely SSHs into the AWS EC2 instance.
3. **Deployment:** The new container is deployed. Nginx acts as a reverse proxy, securely routing external HTTP traffic to the internal Docker container.
4. **Monitoring:** Prometheus scrapes host and container metrics via `node_exporter`, which are visualized in real-time on Grafana dashboards.

## 🛠️ Tech Stack
* **Application:** Python, FastAPI, Uvicorn
* **Containerization:** Docker, Docker Compose
* **CI/CD:** GitHub Actions
* **Cloud Infrastructure:** AWS EC2 (Ubuntu), Security Groups, IAM
* **Web Server:** Nginx (Reverse Proxy)
* **Monitoring & Alerting:** Prometheus, Grafana, Node Exporter
* **Scripting:** Bash (Health checks and backups)

## 📁 Repository Structure
```text
├── app/
│   ├── main.py              # FastAPI application (includes /health endpoint)
│   ├── requirements.txt     # Python dependencies
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions CI/CD pipeline
├── nginx/
│   └── default.conf         # Nginx reverse proxy configuration
├── monitoring/
│   ├── prometheus.yml       # Prometheus scrape configs
│   └── docker-compose.yml   # Monitoring stack configuration
├── scripts/
│   ├── health_check.sh      # Bash script for endpoint verification
│   └── backup.sh            # Automated backup script
├── Dockerfile               # Multi-stage Dockerfile for FastAPI
├── docker-compose.yml       # Main application deployment compose file
└── README.md
