# quiz-platform Application
# Overview:
This project demonstrates the automated deployment of a Python application and MongoDB using Docker Compose, orchestrated by Jenkins on an EC2 instance provisioned with Terraform. The goal of the project is to set up a fully automated pipeline for deploying the application and managing infrastructure.

# Key Features:
Infrastructure as Code: The EC2 instance is provisioned using Terraform, making the deployment repeatable and scalable.
Automated Configuration: Ansible is used to configure the EC2 instance by installing Docker and Jenkins.
Application Deployment: Docker Compose is used to manage the deployment of the Python application (running on port 8080) and MongoDB (running on port 27017).
Continuous Integration: The project integrates with GitHub through a webhook, allowing Jenkins to automatically build and deploy the application whenever new code is pushed to the repository.

# Architecture:
AWS EC2 Instance: The application runs on an EC2 instance, provisioned using Terraform in the us-east-1 region.
Jenkins: Jenkins automates the CI/CD pipeline, handling tasks like building and deploying the application.
Docker Compose: Used for containerizing both the Python app and MongoDB, ensuring that the application is consistently deployed across different environments.
MongoDB: The application connects to MongoDB for database storage.

# Prerequisites:
Terraform
Ansible
Docker
Jenkins
AWS Account

# Getting Started:
1. Clone the Repository
Clone this repository to your local machine:
git clone https://github.com/shehabmohamed99/quiz-platform.git

2. Terraform Deployment:
Ensure you have Terraform installed, then run the following commands to provision the EC2 instance:
cd terraform
terraform init
terraform apply

3. Ansible Configuration:
Once the EC2 instance is provisioned, use Ansible to configure it by installing Docker and Jenkins:
ansible-playbook -i <your-ec2-instance-ip>, playbook.yml

4. Jenkins Setup:
Set up Jenkins on the EC2 instance.
Create a pipeline Job to pull the latest code from GitHub and run the following command:

5. Continuous Integration
Configure a GitHub Webhook to trigger the Jenkins job automatically on every push to the repository.

# Technologies Used:
AWS EC2
Terraform
Docker & Docker Compose
Jenkins
Ansible
MongoDB
Python

Docker Compose is used to define and manage the multi-container application setup, where the Python app and MongoDB run as separate containers.
Jenkins automates the build and deployment process. It pulls the latest code from GitHub, runs docker-compose up --build, and ensures that the Python app and MongoDB are properly configured.
GitHub Webhook triggers Jenkins automatically on new commits, enabling Continuous Integration for the project.
