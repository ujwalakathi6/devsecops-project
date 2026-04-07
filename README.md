# 🚀 DevSecOps CI/CD Pipeline Project

This project demonstrates a **complete DevSecOps pipeline** by integrating security into every stage of the software development lifecycle using **GitHub Actions, AWS, Docker, and security tools**.

It is designed as a **hands-on learning project** to showcase how modern applications can be built, scanned, and deployed securely.

---

## 📌 Project Objective

The goal of this project is to:

- Automate build and security checks using CI/CD
- Detect vulnerabilities early in development
- Secure infrastructure and application code
- Build and scan container images
- Store security reports for analysis

---

## 🛠️ Tech Stack

- **Programming:** Python (Django + Flask demo)
- **CI/CD:** GitHub Actions
- **Cloud:** AWS (ECR, S3)
- **Containerization:** Docker
- **IaC:** Terraform
- **Security Tools:**
  - Bandit (SAST)
  - Checkov (IaC Scan)
  - Trivy (Container Scan)

---

## 📁 Project Structure

```bash
devsecops-project/
│
├── .github/workflows/
│   └── security-pipeline.yml      # CI/CD pipeline
│
├── secure_app/
│   └── app.py                    # Sample vulnerable app
│
├── terraform/
│   └── main.tf                   # AWS infra (ECR + S3)
│
├── dockerfile                    # Docker build config
├── buildspec.yml                 # AWS CodeBuild config
├── manage.py                     # Django entry point
├── requirements.txt              # Dependencies
├── db.sqlite3                    # Database
└── README.md                     # Documentation

```
---

## ⚙️ DevSecOps Pipeline Flow

```bash
Developer Push
      ↓
GitHub Actions Trigger
      ↓
Bandit scans Python code for hardcoded credentials, insecure coding practices, and vulnerabilities
      ↓
Checkov scans Terraform files for misconfigured resources, public access risks, and missing encryption
      ↓
Build Docker Image
      ↓
Trivy scans Docker image for OS vulnerabilities, dependency issues, and critical CVEs
      ↓
Push to AWS ECR
      ↓
Upload Reports to S3
      ↓
Fail Pipeline if HIGH/CRITICAL ❌

```
---
## ☁️ AWS Integration
- Amazon ECR is used to store Docker images securely
- Amazon S3 is used to store security scan reports

---
## 🚀 Running the Project Locally
1. Clone Repository:  
  git clone https://github.com/Shirisha3141/devsecops-project.git   
  cd devsecops-project
2. Create Virtual Environment:   
  python -m venv venv
3. Activate Environment:  
Windows  
venv\Scripts\activate   
Linux / Mac   
source venv/bin/activate   
4. Install Dependencies:   
pip install -r requirements.txt   
5. Apply Migrations:    
python manage.py migrate    
6. Run Server    
python manage.py runserver   

Access:   

http://127.0.0.1:8000/


---
## 🐳 Run Using Docker
Build Image:   
docker build -t devsecops-project .   
Run Container:    
docker run -p 8000:8000 devsecops-project

---
## 🔄 CI/CD Workflow

The pipeline defined in .github/workflows/security-pipeline.yml performs:

- Code checkout
- AWS authentication
- Python setup
- Security scanning (Bandit + Checkov)
- Docker image build
- Container scanning (Trivy)
- Push to ECR
- Upload reports to S3

---
## 🧪 Security Demonstration

This project includes intentionally vulnerable code (like hardcoded passwords) to demonstrate:

- Real-time vulnerability detection
- Pipeline failure when issues are found
---
## 📊 Expected Output
- ✅ DevSecOps Pipeline → SUCCESS

OR

 - ❌ Pipeline Failed (Vulnerabilities Found)
 ---
 
## 💡 Use Cases
- College Project / Expo
- Resume Project
- Placement Interviews
- DevOps Learning
Security Demonstration

---
## 🔮 Future Improvements
- Add deployment (EC2 / ECS)
- Use AWS Secrets Manager
- Add monitoring & alerts
- Add frontend dashboard
- Add automated testing
- Improve report visualization

---
## 👩‍💻 Author

**Shirisha**
- GitHub: https://github.com/Shirisha3141
