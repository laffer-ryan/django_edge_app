# django_edge_app



### Notes
- docker compose up: builds all images in docker compose.yaml
- docker compose --rmi all: Takes down all of the images and require them to be rebuilt
- docker compose down -v: Doesn't take down the container image. The information to spin up the database still exists so it spins up much faster