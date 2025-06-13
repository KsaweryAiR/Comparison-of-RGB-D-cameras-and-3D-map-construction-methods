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

> 🔧 **TODO**: Uzupełnij dokładne nazwy kamer i funkcje paczek.

---

## 🖼️ Przykładowe zdjęcia / Wizualizacje

Dodaj tutaj zrzuty ekranu z RViz, graficzne diagramy przepływu danych lub inne ilustracje pokazujące działanie systemu.

```
📷 [Tutaj dodaj obrazek z RViz]
```

### Wymagania:
- Docker
- System z obsługą USB 

## Pobierz repozytorium

```bash
git clone
```

## 🐳 Docker – Instalacja dla każdej kamery

### 1️⃣ Azure Kinect DK

#### 🔧 Budowanie obrazu

```bash
cd 
```

```bash
docker build -t azure_kinect_cam docker/azure_kinect/
```

#### 🚀 Uruchamianie kontenera

```bash
docker run -it --rm --net=host --privileged \
  -v /dev:/dev \
  --device-cgroup-rule='c 81:* rmw' \
  azure_kinect_cam
```

> ⚠️ Upewnij się, że masz zainstalowany `libk4a` oraz `k4a-tools` w systemie hosta lub dodaj je do Dockera.

---

### 2️⃣ Orbbec Femto Mega

#### 🔧 Budowanie obrazu

```bash
docker build -t orbbec_femto_cam docker/orbbec_femto/
```

#### 🚀 Uruchamianie kontenera

```bash
docker run -it --rm --net=host --privileged \
  -v /dev:/dev \
  orbbec_femto_cam
```

> 📄 Zainstaluj SDK od Orbbeca i odpowiedni `udev` rules file (może być skopiowany do kontenera).

---

### 3️⃣ Intel RealSense D435

#### 🔧 Budowanie obrazu

```bash
docker build -t realsense_cam docker/realsense_d435/
```

#### 🚀 Uruchamianie kontenera

```bash
docker run -it --rm --net=host --privileged \
  -v /dev:/dev \
  --device=/dev/video0 \
  realsense_cam
```

> 📦 Upewnij się, że biblioteka `librealsense2` została poprawnie zainstalowana w kontenerze.

---

## 🧠 ROS 2 Paczki

```bash
ros2_ws/
└── src/
    ├── camera_processing_pkg/
    └── camera_launch_pkg/
```

### 🛠️ Budowanie workspace

```bash
cd ros2_ws
colcon build --symlink-install
source install/setup.bash
```

---

## ✅ TODO

- [ ] Dodać launchery dla każdej kamery w `camera_launch_pkg`
- [ ] Dodać dokumentację do `camera_processing_pkg`
- [ ] Uzupełnić konfiguracje RViz
- [ ] Ustawić automatyczne uruchamianie z ROS 2 launch

---

## 📚 Wymagania

- ROS 2 Humble (w Dockerze lub lokalnie)
- Docker + opcjonalnie NVIDIA Container Toolkit
- SDK i `udev` rules do: Azure Kinect, Orbbec Femto Mega, RealSense D435

---

## 👤 Autorzy

- Imię i nazwisko / nick (Tu wpisz siebie, Mój Panie)
- Współpracownicy (opcjonalnie)

---

## 📝 Licencja

Projekt dostępny na licencji [MIT / BSD-3 / inna].


