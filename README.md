# 🏢 IoT Building Infrastructure Platform

A production-grade smart building DevOps platform built on **Microsoft Azure** — simulating real-world IoT sensor data from multiple buildings with full CI/CD, observability, security, and a live dashboard.

🌐 **Live Dashboard:** [https://iot-building-dashboard.vercel.app](https://iot-building-dashboard.vercel.app)

---

## 🎯 What This Project Does

- 📡 Simulates **real-time IoT sensor data** from 3 buildings — temperature, occupancy, energy, air quality, access control
- ☁️ Runs everything on **Microsoft Azure** using AKS, Key Vault, VNet, and Container Registry
- 🔄 Fully automated **CI/CD pipeline** using GitHub Actions with security scanning
- 📊 Complete **observability stack** — Prometheus, Grafana, and Uptime Kuma
- 🔔 **Instant alerting** via Telegram when anomalies are detected
- 🔐 **Enterprise-grade security** — Azure Key Vault, NSG, Firewall rules, Trivy scanning
- 🌐 **Live frontend dashboard** deployed on Vercel

---

## 🏗️ Architecture

GitHub Actions CI/CD
↓
Docker Build + Trivy Security Scan
↓
Push to Azure Container Registry
↓
Deploy to Azure Kubernetes Service (AKS)
↓
Prometheus + Grafana + Uptime Kuma → Telegram Alerts
↓
Live Dashboard on Vercel

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| ☁️ Cloud | Microsoft Azure |
| ☸️ Container Orchestration | Kubernetes (AKS) |
| 🏗️ Infrastructure as Code | Terraform |
| 🔄 CI/CD | GitHub Actions |
| 🐳 Containers | Docker + Azure Container Registry |
| 🔐 Secrets Management | Azure Key Vault |
| 🌐 Networking | Azure VNet + NSG + Firewall |
| 📊 Metrics | Prometheus + Grafana |
| ⏱️ Uptime Monitoring | Uptime Kuma |
| 🔔 Alerting | Telegram Bot |
| 🛡️ Security Scanning | Trivy |
| 🌐 Frontend | Vercel |

---

## 📁 Project Structure

IoT-Building-Infrastructure/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions CI/CD pipeline
├── terraform/
│   ├── main.tf                 # Azure infrastructure (AKS, VNet, Key Vault, ACR)
│   ├── variables.tf            # Input variables
│   ├── outputs.tf              # Output values
│   └── terraform.tfvars        # Variable values
├── kubernetes/
│   └── sensor-service/
│       └── deployment.yaml     # Kubernetes deployment and service
├── microservices/
│   └── sensor-simulator/
│       ├── app.py              # IoT sensor simulator with Flask health endpoint
│       ├── requirements.txt    # Python dependencies
│       └── Dockerfile          # Container image definition
├── monitoring/
│   ├── prometheus/
│   │   └── values.yaml         # Prometheus + Grafana Helm values
│   └── uptime-kuma.yaml        # Uptime Kuma deployment
├── frontend/
│   └── dashboard/
│       └── index.html          # Live smart building dashboard
└── README.md

---

## 🚀 Infrastructure

All Azure resources are provisioned using **Terraform**:

| Resource | Name | Purpose |
|---|---|---|
| Resource Group | iot-building-rg | Container for all resources |
| Virtual Network | iotbuilding-vnet | Private networking |
| AKS Cluster | iotbuilding-aks | Kubernetes orchestration |
| Container Registry | iotbuildingregistry | Docker image storage |
| Key Vault | iotbuilding-kv | Secrets management |
| NSG | iotbuilding-nsg | Network security rules |

---

## 🔄 CI/CD Pipeline

Every push to `main` branch triggers:

1 Code checkout
2 Python dependency install
3 Trivy security scan (filesystem)
4 Docker image build
5 Trivy image scan (CVE check)
6 Push to Azure Container Registry
7 Deploy to AKS
8 Verify rollout
9 Telegram notification

---

## 📊 Observability Stack

| Tool | Purpose | Access |
|---|---|---|
| **Prometheus** | Metrics collection | kubectl port-forward :9090 |
| **Grafana** | Dashboards and visualization | kubectl port-forward :3000 |
| **Uptime Kuma** | Uptime monitoring | kubectl port-forward :3001 |
| **Telegram** | Instant alert notifications | Bot notifications |

---

## 🔐 Security Features

- ✅ **Azure Key Vault** — all secrets stored and rotated securely
- ✅ **NSG Rules** — only necessary traffic allowed
- ✅ **Non-root containers** — all pods run as non-root user
- ✅ **Trivy scanning** — CVE scanning on every pipeline run
- ✅ **GitHub Secrets** — no plain text credentials anywhere
- ✅ **RBAC** — role-based access control in Kubernetes
- ✅ **Private VNet** — no resources directly exposed to internet

---

## 🏃 Getting Started

### Prerequisites
- Azure Account (free tier works)
- Azure CLI
- Terraform
- kubectl
- Docker
- Git

### Deploy Infrastructure

```bash
# Clone the repository
git clone https://github.com/ArvanHunt/IoT-Building-Infrastructure.git
cd IoT-Building-Infrastructure

# Login to Azure
az login

# Deploy infrastructure
cd terraform
terraform init
terraform plan
terraform apply

# Connect to AKS
az aks get-credentials --resource-group iot-building-rg --name iotbuilding-aks

# Deploy application
kubectl apply -f kubernetes/sensor-service/deployment.yaml

# Install monitoring
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
kubectl apply -f monitoring/uptime-kuma.yaml
```

### Access Services

```bash
# Grafana Dashboard
kubectl port-forward -n monitoring svc/prometheus-grafana 3000:80

# Uptime Kuma
kubectl port-forward -n monitoring svc/uptime-kuma-service 3001:3001

# Sensor Health Check
kubectl port-forward svc/sensor-simulator-service 8080:80
# Visit: http://localhost:8080/health
```

---

## 📡 Sensor Data

The IoT simulator generates realistic building data every 5 seconds:

| Sensor | Range | Alert Threshold |
|---|---|---|
| Temperature | 17°C — 30°C | > 26°C |
| Occupancy | 0 — 300 people | — |
| Energy | 80 — 520 kWh | — |
| Air Quality (AQI) | 0 — 100 | > 80 |
| Unauthorized Access | 0 — 2 | > 0 |

---

## 🌐 Live Dashboard

Visit the live dashboard:
👉 **[https://iot-building-dashboard.vercel.app](https://iot-building-dashboard.vercel.app)**

Features:
- Real-time KPI strip
- Per-building sensor metrics
- Live sparkline charts
- Active alerts panel
- Access control log
- Energy distribution ring chart
- Occupancy trend bar chart
- Infrastructure status panel

---

## 👨‍💻 Author

**Arvan** — DevOps / Platform Engineer

- 🐙 GitHub: [@ArvanHunt](https://github.com/ArvanHunt)
- ☸️ CKA Certified Kubernetes Administrator
- ☁️ Multi-cloud: AWS, Azure, GCP

---

## 📄 License

MIT License — feel free to use and modify!