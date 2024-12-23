### Docker 🐳

---

### Table of Contents
1. [What is Docker?](#what-is-docker)
2. [Docker Installation](#docker-installation)
3. [Docker Commands Overview](#docker-commands-overview)
   - [Images](#images)
   - [Containers](#containers)
   - [Volumes](#volumes)
   - [Networks](#networks)
4. [Dockerfile Basics](#dockerfile-basics)
5. [Docker Compose](#docker-compose)
6. [Docker Lifecycle Chart](#docker-lifecycle-chart)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)
9. [Workflow](#workflow)

---

### What is Docker? 📦
Docker is a platform for developing, shipping, and running applications inside lightweight, portable containers.  

---

### Docker Installation 🛠️
1. Download Docker from [docker.com](https://www.docker.com/)
2. Install Docker Desktop (Windows/macOS) or Docker Engine (Linux)
3. Verify installation:
   ```bash
   docker --version
   ```

---

### Docker Commands Overview ⚡

#### Images 🖼️
- List images:  
  ```bash
  docker images
  ```
- Pull an image:  
  ```bash
  docker pull <image-name>
  ```
- Remove an image:  
  ```bash
  docker rmi <image-id>
  ```

#### Containers 🛳️
- List running containers:  
  ```bash
  docker ps
  ```
- List all containers (including stopped):  
  ```bash
  docker ps -a
  ```
- Run a container:  
  ```bash
  docker run -d -p <host-port>:<container-port> <image-name>
  ```
- Stop a container:  
  ```bash
  docker stop <container-id>
  ```
- Remove a container:  
  ```bash
  docker rm <container-id>
  ```

#### Volumes 📂
- Create a volume:  
  ```bash
  docker volume create <volume-name>
  ```
- List volumes:  
  ```bash
  docker volume ls
  ```
- Remove a volume:  
  ```bash
  docker volume rm <volume-name>
  ```

#### Networks 🌐
- Create a network:  
  ```bash
  docker network create <network-name>
  ```
- List networks:  
  ```bash
  docker network ls
  ```
- Connect a container to a network:  
  ```bash
  docker network connect <network-name> <container-id>
  ```

---

### Dockerfile Basics 📝
1. Create a `Dockerfile`:
   ```dockerfile
   # Use base image
   FROM python:3.9-slim

   # Set working directory
   WORKDIR /app

   # Copy files
   COPY . .

   # Install dependencies
   RUN pip install -r requirements.txt

   # Expose port
   EXPOSE 5000

   # Run the application
   CMD ["python", "app.py"]
   ```
2. Build the image:  
   ```bash
   docker build -t <image-name> .
   ```

---

### Docker Compose 🧩
- Create a `docker-compose.yml`:
   ```yaml
   version: '3.8'
   services:
     app:
       build: .
       ports:
         - "5000:5000"
       volumes:
         - .:/app
       networks:
         - app-network
   networks:
     app-network:
       driver: bridge
   ```
- Start services:  
  ```bash
  docker-compose up -d
  ```
- Stop services:  
  ```bash
  docker-compose down
  ```

---

### Docker Lifecycle Chart 🔄
```plaintext
Image Management
    Pull → docker pull
    Build → docker build
    Remove → docker rmi

Container Management
    Run → docker run
    Stop → docker stop
    Remove → docker rm

Volume & Network
    Create → docker volume create / docker network create
    Connect → docker network connect
    Remove → docker volume rm / docker network rm
```

---

### Best Practices ✅
- Use `.dockerignore` to exclude unnecessary files.
- Keep your `Dockerfile` small and efficient.
- Use multi-stage builds to reduce image size.
- Avoid running containers as root.
- Regularly clean unused images, containers, and volumes:
  ```bash
  docker system prune -a
  ```

---

### Troubleshooting 🛠️
- View logs of a container:  
  ```bash
  docker logs <container-id>
  ```
- Access a running container shell:  
  ```bash
  docker exec -it <container-id> /bin/bash
  ```
- Debug container network issues:  
  ```bash
  docker network inspect <network-name>
  ```

---
 


### Workflow 📝

![!\[alt text\](1_Pf8Y1uhAN0RHy1sqG_qz5A.gif)](../images/docker.gif)