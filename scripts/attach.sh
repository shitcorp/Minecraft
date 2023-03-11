#!/bin/bash
container_name="minecraft-minecraft";
docker_id="$(docker ps --filter="name=$container_name" --format {{.ID}})"
echo "ID: " $docker_id
docker attach $docker_id
