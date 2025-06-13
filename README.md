# Projekt: System Kamer RGB-D z ROS 2

## 📦 Opis

W tym repozytorium znajdują się pliki `Dockerfile` dla trzech różnych kamer RGB-D oraz dwie paczki ROS 2 (Humble). Projekt ma na celu stworzenie zunifikowanego środowiska kontenerowego do uruchamiania i testowania strumieni danych z różnych typów kamer głębi w ekosystemie ROS 2.

**Kamery obsługiwane:**
- Kamera 1 (Azure Kinect DK)
- Kamera 2 (Orbbec Femto Mega)
- Kamera 3 (Intel RealSense Depth Camera D435)

**Paczki ROS 2:**
- `camera_processing_pkg` – obsługa przetwarzania danych z kamer
- `camera_launch_pkg` – konfiguracja i uruchamianie kamer

### Wymagania:
- Docker
- System z obsługą USB 

## Pobierz repozytorium

```bash
git clone https://github.com/KsaweryAiR/Comparison-of-RGB-D-cameras-and-3D-map-construction-methods.git
```

```bash
cd Comparison-of-RGB-D-cameras-and-3D-map-construction-methods/
```

## 🐳 Docker – Instalacja dla każdej kamery

### 1️⃣ Azure Kinect DK

#### 🔧 Budowanie obrazu (Podłącz Azure Kinect DK do usb a inne odłącz!!)

```bash
cd camera_installer/kinect-camera-docker/
```

```bash
docker build -t kinect_rviz .
```
#### 🚀 Uruchamianie kontenera
```bash
bash run_docker.sh
```
Akceptacja i instalacja zasad użytkowania (w kontenerze)
```bash
cd azure_kinect_notes
```

```bash
bash install_azure_kinect_camera_u_22.04.sh
```
Budowa paczki ros driver kinect

```bash ros2_ws
cd .. /cd ros2_ws
```

```bash
source /opt/ros/humble/setup.bash
```

```bash
colcon build
```

```bash
source install/setup.bash
```

### 2️⃣ Orbbec Femto Mega

#### 🔧 Budowanie obrazu (Podłącz Orbbec Femto Mega do usb a inne odłącz!!)

```bash
cd camera_installer/orbbec-camera-docker/
```

```bash
docker build -t orbbec_rviz .
```

#### 🚀 Uruchamianie kontenera
```bash
bash run_docker.sh
```
Gotowy do działania :)

### 3️⃣ Intel RealSense D435

#### 🔧 Budowanie obrazu (Podłącz Intel RealSense D435 do usb a inne odłącz!!)

```bash
cd camera_installer/intel-camera-docker/
```

```bash
docker build -t intel_rviz .
```

#### 🚀 Uruchamianie kontenera
```bash
bash run_docker.sh
```
Gotowy do działania :)

### Po instalacji można podłączyć wszystkie kamery na raz

<img src="img/chmura.png" style="width: 80%; height: 80%;"> 

### Zebrane dane można wykorzystać do budowy map 3D 

Bonxai
https://github.com/facontidavide/Bonxai

UFOMap
https://github.com/UnknownFreeOccupied/ufomap

<img src="img/map1.png" style="width: 80%; height: 80%;"> 
<img src="img/map2.png" style="width: 80%; height: 80%;"> 


