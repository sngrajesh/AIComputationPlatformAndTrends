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

**1. Update System**
```bash
sudo apt update && sudo apt upgrade -y
```

**2. Install Docker**
```bash
sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
```

**3. Add Kubernetes Repository**
```bash
sudo apt install -y apt-transport-https ca-certificates curl
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
```

**4. Install Kubernetes Tools**
```bash
sudo apt update
sudo apt install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```

**5. Start and Verify Installation**
```bash
kubeadm version
kubectl version --client
```

**6. Initialize Kubernetes (Optional)**
For a single-node cluster:
```bash
sudo kubeadm init
```

Follow the on-screen instructions to set up your `kubectl` configuration.

**7. Allow Non-Root Access (Optional)**
```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

**8. Install Network Plugin**
Example (Calico):
```bash
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
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
- Types: ClusterIP (default), NodePort, LoadBalancer.
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