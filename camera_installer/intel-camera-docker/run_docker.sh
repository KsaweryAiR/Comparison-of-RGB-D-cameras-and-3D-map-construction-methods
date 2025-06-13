#!/bin/bash

# Zezwól lokalnie rootowi (kontenerowi) na połączenie z X11 (tylko raz, ale warto mieć w s>
xhost +local:root

# Uruchomienie kontenera z GUI i dostępem do USB
docker run -it \
  --rm \
  --shm-size=1g \
  --ulimit memlock=-1 \
  --env="DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --privileged \
  --volume="/home/$user/idmp_shared:/root/Shared:rw" \
  --device=/dev/usb \
  --gpus all \
  --env="XAUTHORITY=$XAUTH" \
  --volume="$XAUTH:$XAUTH" \
  --env="NVIDIA_VISIBLE_DEVICES=all" \
  --env="NVIDIA_DRIVER_CAPABILITIES=all" \
  --network=host \
  --privileged \
  --device=/dev/bus/usb \
  -e DISPLAY=$DISPLAY \
  --name intel_rviz_container \
  intel_rviz \
  bash
