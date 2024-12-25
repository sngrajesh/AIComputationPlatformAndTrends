## Kubernetes 🌐

### Table of Contents
1. [Overview](#overview)
2. [Key Components](#key-components)
3. [Setup and Installation](#setup-and-installation)
4. [Working with Kubernetes Objects](#working-with-kubernetes-objects)
   - [Pods](#pods)
   - [Deployments](#deployments)
   - [Services](#services)
5. [Namespaces](#namespaces)
6. [ConfigMaps and Secrets](#configmaps-and-secrets)
7. [Storage](#storage)
8. [Monitoring and Logging](#monitoring-and-logging)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)
11. [Flowchart](#flowchart)

---

#### Overview
Kubernetes is an open-source container orchestration platform for automating deployment, scaling, and management of containerized applications.

---

#### Key Components 🛠️
| Component      | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Master Node** | Manages the Kubernetes cluster and makes global decisions.                  |
| **Worker Nodes** | Host applications in containers managed by Kubernetes.                     |
| **etcd**        | Key-value store for cluster data and configurations.                       |
| **Controller**  | Maintains desired state of resources in the cluster. (Eg: Node Controller, Replica Controller) |
| **Scheduler**   | Assigns pods to nodes based on resource requirements.                      |
| **Kubelet**     | Runs on worker nodes, ensuring container health and resource usage.         |
| **kubectl**     | Command-line tool for interacting with the cluster.                        |

---

#### Setup and Installation 🚧

**Update System**
```bash
sudo apt update -y
sudo apt install -y curl wget apt-transport-https
```

**Download the Minikube binary**
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
```

**Install the downloaded MiniKube**
```bash
sudo install minikube-linux-amd64 /usr/local/bin/minikube

```

**Verify Minikube installation.**
```bash
minikube version
```

**Download Kubectl binary.**
```bash
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
```

**Converting the downloaded binary to executable.**
```bash
chmod  +x  kubectl
```

**Moving the binary to /usr/local/bin.**
```bash
sudo mv kubectl /usr/local/bin
```

**Verify Kubectl version.**
```bash
kubectl version -o yaml
```

**Give user permission to run docker commands (after creating a user).**
```bash
usermod   -G docker   $(whoami)
```

**Logout from ubuntu and login again. This will apply the user group membership. Then start the Minikube.**
```bash
minikube start — driver=docker
``` 
---

#### Working with Kubernetes Objects 💚

##### Pods
- Smallest deployable unit in Kubernetes.
- Create a pod:
  ```yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: example-pod
  spec:
    containers:
    - name: nginx
      image: nginx
  ```
  Apply it:
  ```bash
  kubectl apply -f pod.yaml
  ```
- List pods:
  ```bash
  kubectl get pods
  ```

##### Deployments
- Manages replicas of pods for scaling and updates.
- Create a deployment:
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: example-deployment
  spec:
    replicas: 2
    selector:
      matchLabels:
        app: nginx
    template:
      metadata:
        labels:
          app: nginx
      spec:
        containers:
        - name: nginx
          image: nginx
  ```
  Apply it:
  ```bash
  kubectl apply -f deployment.yaml
  ```
- Scale deployment:
  ```bash
  kubectl scale deployment example-deployment --replicas=3
  ```

##### Services
- Expose applications running in pods to the network.
- Types: 
  - **ClusterIP (default)** : Exposes the service on a cluster-internal IP. Can be accessed only from within the cluster.
  - **NodePort** : A port is assigned to a service which is mapped on all the computers within the cluster. The service can be accessed from outside the cluster using node IP and the node port.
  - **LoadBalancer** : Exposes the service externally using a cloud provider’s load balancer. NodePort and ClusterIP services, to which the external load balancer will route, should use the same port number.
- Create a service:
  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: example-service
  spec:
    selector:
      app: nginx
    ports:
    - protocol: TCP
      port: 80
      targetPort: 80
    type: ClusterIP
  ```
  Apply it:
  ```bash
  kubectl apply -f service.yaml
  ```

---

#### Namespaces 🌐
- Logical isolation for resources in a cluster.
- List namespaces:
  ```bash
  kubectl get namespaces
  ```
- Create a namespace:
  ```bash
  kubectl create namespace example-namespace
  ```
- Use a namespace:
  ```bash
  kubectl config set-context --current --namespace=example-namespace
  ```

---

#### ConfigMaps and Secrets 🔒
- **ConfigMaps**: Store configuration data.
  ```bash
  kubectl create configmap example-config --from-literal=key=value
  ```
- **Secrets**: Store sensitive data.
  ```bash
  kubectl create secret generic example-secret --from-literal=username=admin
  ```
- View resources:
  ```bash
  kubectl get configmaps
  kubectl get secrets
  ```

---

#### Storage 🛢️
- **Persistent Volumes (PV):** Pre-provisioned storage.
- **Persistent Volume Claims (PVC):** Request for storage.
  ```yaml
  apiVersion: v1
  kind: PersistentVolumeClaim
  metadata:
    name: example-pvc
  spec:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  ```

---

#### Monitoring and Logging 📸
- Use tools like Prometheus, Grafana, and ELK stack.
- View pod logs:
  ```bash
  kubectl logs <pod-name>
  ```
- Describe resources:
  ```bash
  kubectl describe pod <pod-name>
  ```

---

#### Best Practices 💪
1. Use namespaces for resource isolation.
2. Limit resource usage with requests and limits.
3. Automate scaling with Horizontal Pod Autoscaler (HPA).
4. Store sensitive data in Secrets, not ConfigMaps.
5. Regularly update images and Kubernetes versions.

---

#### Troubleshooting 🌧️
1. **Check pod status:**
   ```bash
   kubectl get pods -o wide
   ```
2. **Debug pod issues:**
   ```bash
   kubectl describe pod <pod-name>
   kubectl logs <pod-name>
   ```
3. **Get events:**
   ```bash
   kubectl get events --sort-by=.metadata.creationTimestamp
   ```
4. **Check node status:**
   ```bash
   kubectl get nodes
   ```

---

#### Flowchart 📝
![alt text](../images/kubernetees.gif)
