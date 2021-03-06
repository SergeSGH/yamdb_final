![yamdb forkflow status](https://github.com/SergeSGH/yamdb_final/workflows/yamdb_workflow/badge.svg)
# yamdb_final
### Описание:
проект по предоставлению информации о медиаконтенте, в том числе с ревью и отзывами.
Аналог imdb, metacritic, kinopoisk и др.

### Войти в админ зону и отредактировать данные проекта можно здесь:
http://gbu-1541.hopto.org/admin/

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
В папке проекта создать файл .env в котором определить ключевые переменные:  
```
DB_ENGINE: вид БД
DB_NAME: имя БД
POSTGRES_USER: логин пользователя БД
POSTGRES_PASSWORD: пароль пользователя БД
DB_HOST: приложение БД 
DB_PORT: порт БД
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