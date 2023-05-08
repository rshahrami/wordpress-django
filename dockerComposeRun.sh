echo "remove all docker compose container"
docker compose down 
echo "remove all container"
docker ps -a | awk '{print $1}' | xargs docker rm --force
echo "remove all images with none tag"
docker images | grep none | awk '{print $3}' | xargs docker rmi --force
echo "remove all images with latest tag"
docker images | grep latest | awk '{print $3}' | xargs docker rmi --force
echo "docker compose building and runing"
docker compose build --no-cache && docker compose up
