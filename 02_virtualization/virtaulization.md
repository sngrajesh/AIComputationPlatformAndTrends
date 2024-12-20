
## Virtualization 🧑‍💻

### Table of Contents
1. [Introduction to Virtualization](#introduction-to-virtualization)
2. [Types of Hypervisors](#types-of-hypervisors)
   - [Type 1: Bare Metal](#type-1-bare-metal)
   - [Type 2: Application](#type-2-application)
3. [Key Concepts](#key-concepts)
4. [Advantages of Virtualization](#advantages-of-virtualization)
5. [Limitations of Virtualization](#limitations-of-virtualization)
6. [Use Cases](#use-cases)

---

### Introduction to Virtualization 🌐

- **Virtualization**: The process of creating virtual instances of computing resources such as hardware, storage, or networks.
- **Hypervisor**: Software used to create and manage virtual machines (VMs).

---

### Types of Hypervisors 🖥️

#### Type 1: Bare Metal ⚙️
- **Definition**: Installed directly on hardware without a host operating system.
- **Usage**: Common in enterprise environments for high performance.
- **Features**:
  - Integrated with the OS.
  - More efficient resource usage.
- Examples Applications:
  - Linux KVM
  - Microsoft Hyper-V
  - VMware ESX Server

##### Diagram
```plaintext
🖥️ Hardware   
└── 🖧 Hypervisor  
    └── 💻 Virtual Machine  
        ├── 📱 App  
        ├── 🐍 Python  
        ├── 🖥️ OS  
        └── ⚙️ Virtual Hardware  
```

---

#### Type 2: Application 🛠️
- **Definition**: Installed on top of an existing operating system.
- **Usage**: Ideal for desktop virtualization or testing environments.
- **Features**:
  - Simpler to set up.
  - Dependent on the host OS.
- Examples Applications:
  - Oracle VirtualBox
      - Network Adapter
         - NAT:  Thhe VM is able to access the internet by usingohysical machine.
         - Bridged Adapter: The VM ip is open to outside network. 
         - Host-Only Adapter: The VM is restricted to the host machine. Can only communicate with the host machine.
      - Storage Controller
         - IDE Controller: The VM can access the host machine’s hard drive.
         - SATA Controller: The VM can access the host machine’s SATA drive.
         - SCSI Controller: The VM can access the host machine’s SCSI drive.
      - USB Controller
          - USB Controller: The VM can access the host machine’s USB devices.
      - Audio Controller
          - Audio Controller: The VM can access the host machine’s audio devices.
      - Video Controller
          - VGA Controller: The VM can access the host machine’s VGA device.
          - Display Controller: The VM can access the host machine’s display device.
      - Shared Folders
          - Shared Folders: The VM can access the host machine’s shared folders.
  - VMware Workstation Player/Pro



##### Diagram
```plaintext
🖥️ Hardware  
└── 🖥️ Operating System  
    └── 🖧 Hypervisor  
        └── 💻 Virtual Machine  
            ├── 📱 App  
            ├── 🐍 Python  
            ├── 🖥️ OS  
            └── ⚙️ Virtual Hardware  

```

---

### Key Concepts 💡

- **Virtual Machine (VM)**:
  - A virtual environment emulating physical hardware.
  - Includes its own OS and applications.
- **Virtual Hardware**:
  - Resources like CPU, memory, storage, and network are allocated to VMs.

---

### Advantages of Virtualization 🌟

1. **Resource Efficiency**:
   - Maximize hardware utilization.
2. **Isolation**:
   - Each VM runs independently.
3. **Flexibility**:
   - Easy to provision and decommission resources.
4. **Scalability**:
   - Accommodate growth without additional physical hardware.
5. **Cost Savings**:
   - Reduce hardware and energy expenses.

---

### Limitations of Virtualization ⚠️

1. **Performance Overhead**:
   - Slight performance loss due to virtualization layers.
2. **Hardware Dependency**:
   - Limited by the physical machine’s capacity.
3. **Complexity**:
   - Requires expertise for management and troubleshooting.

---

### Use Cases 💼

1. **Server Consolidation**:
   - Run multiple services on fewer physical machines.
2. **Testing and Development**:
   - Create isolated environments for coding and testing.
3. **Disaster Recovery**:
   - Quickly restore operations using VM backups.
4. **Cloud Computing**:
   - Foundation of IaaS (Infrastructure as a Service) platforms.

