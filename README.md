# Python games

Serie of games to learn more about python language.

## Games

1. PONG
2. SNAKE
3. 4 IN LINE

## How to use it with docker

You should have installed *docker* and *docker compose*.

1. Clone repository `git clone https://github.com/javieroc/python-games.git`
2. Run container `docker-compose up -d`
3. Check container id `docker ps`
4. Go into the container `docker exec -it --user $(id -u):$(id -g) [container_id] bash`
5. Execute a game running e.g: `python Pong.py`
