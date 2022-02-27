![example workflow](https://github.com/SergeSGH/yamdb_final/actions/workflows/yamdb_workflow/badge.svg)
# yamdb_final
### Описание:
проект по предоставлению информации о медиаконтенте, в том числе с ревью и отзывами.
Аналог imdb, metacritic, kinopoisk и др.

### Автор:
Сергей Приходько

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/SergeSGH/yamdb_final.git
```
```
cd yamdb_final/infra
```

Собрать и запустить контейнеры:
```
docker-compose up -d --build
```

Инициировать БД и перенести в нее данные:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py loaddata fixtures.json
```