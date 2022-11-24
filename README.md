# SocNetworkDemo
### Реализован следующий функционал:
- Вход, регистрация
- Публикация постов
- Написание комментариев
- Подписка на пользователя
- Лента, состоящая из постов пользователей из подписок
- Просмотр профиля
### В разработке:
- лайки на ajax-запросах
- личные сообщения на websocket'ах
### Текущий стек
- Django
- Postgres
- HTML, CSS
- Django Templates 

## Чтобы запустить, в командной строке нужно:
### Клонировать репозиторий
```
git clone https://github.com/Potagashev/SocNetworkDemo.git
```
### Находясь в корне проекта, провести миграции
```
docker-compose run web python SocialNetworkDemo/manage.py migrate
```
### Запустить
```
docker-compose up
```
### Перейти по ссылке
```
http://127.0.0.1:8000/
```
