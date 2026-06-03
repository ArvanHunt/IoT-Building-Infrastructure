# IoT Building Infrastructure 🏢

A production-grade DevOps platform for smart building IoT data management built on Azure Cloud.

## 🏗️ Architecture Overview

This platform simulates a real-world smart building infrastructure that:
- Collects real-time IoT sensor data from multiple buildings
- Manages building access control systems
- Processes and analyzes building data in real time
- Provides observability across all building systems
- Maintains enterprise-grade security and compliance

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Cloud | Microsoft Azure |
| Container Orchestration | Kubernetes (AKS) |
| Infrastructure as Code | Terraform |
| CI/CD | GitHub Actions + Azure DevOps |
| Secrets Management | Azure Key Vault |
| Observability | Prometheus + Grafana + Azure Monitor |
| Security | Trivy + SonarQube + NSG + Azure Firewall |
| Frontend | Vercel |
| Container Registry | Azure Container Registry |

## 📁 Project Structure

IoT-Building-Infrastructure/
├── terraform/          # Azure infrastructure as code
├── kubernetes/         # Kubernetes manifests
├── microservices/      # Application services
├── monitoring/         # Prometheus and Grafana configs
├── frontend/           # Dashboard application
├── .github/workflows/  # CI/CD pipelines
└── docs/               # Architecture documentation

## 🚀 Microservices

### 1. Sensor Simulator
Simulates IoT sensors from multiple buildings sending real-time data:
- Temperature sensors
- Occupancy sensors
- Energy meters
- Access control events

### 2. Access Control Service
Manages building access:
- Entry and exit tracking
- Unauthorized access alerts
- Real-time access logs

### 3. Analytics Service
Processes building data:
- Real-time occupancy analytics
- Energy consumption insights
- Anomaly detection

## 🔐 Security

- Azure Key Vault for secrets management
- Network Security Groups for traffic control
- Azure Firewall for centralized security
- Trivy scanning in every CI/CD pipeline
- Zero plain-text credentials anywhere

## 📊 Observability

- Prometheus for metrics collection
- Grafana dashboards per building
- Azure Monitor for cloud-level visibility
- Automated alerts for anomalies

## 🏃 Getting Started

### Prerequisites
- Azure Account
- Azure CLI
- Terraform
- kubectl
- Docker

### Setup
```bash
# Clone the repository
git clone https://github.com/ArvanHunt/IoT-Building-Infrastructure.git

# Navigate to project
cd IoT-Building-Infrastructure

# Initialize Terraform
cd terraform
terraform init

# Deploy infrastructure
terraform plan
terraform apply
```

## 📈 Architecture Diagram

Coming soon!

## 👨‍💻 Author

**Arvan** — DevOps / Platform Engineer
- GitHub: [@ArvanHunt](https://github.com/ArvanHunt)

## 📄 License

MIT License

