# Описание
Этот проект разрабатывает **RESTful API** для социальной сети, позволяя пользователям регистрироваться, создавать профили, публиковать посты и комментарии, а также управлять подписками на других пользователей.
Он также включает в себя функциональность аутентификации и авторизации, фильтрацию и поиск постов, и обеспечивает проверки, чтобы пользователи не могли подписаться на самих себя или создать дублирующие подписки.
Этот проект предоставляет мощное средство для взаимодействия с социальной сетью через программный интерфейс.
# Установка
## Как развернуть проект на локальной машине
### Клонировать репозиторий и перейти в него в командной строке
```
  git clone https://github.com/N0len-sasha/api_final_yatube.git
```
```
  api_final_yatube
```
### Создать и активировать виртуальное окружение
```
  python -m venv venv
```
```
  source venv/Scripts\activate
```
### Установить зависимости
```
  pip install -r requirements.txt
```
### Выполнить миграции
```
  cd yatube_api
```
```
  python manage.py migrate
```
### Запустить проект
```
  python manage.py runserver
```
# Примеры
## Здесь представлены некоторые примеры запросов к API**
Запрос:
```
GET http://127.0.0.1:8000/api/v1/posts/
```
Ответ: 
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

Запрос:
```
POST http://127.0.0.1:8000/api/v1/posts/
```
Ответ: 
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Запрос:
```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
Ответ: 
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

Запрос:
```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```
Ответ: 
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
Запрос:
```
POST http://127.0.0.1:8000/api/v1/follow/
```
Ответ: 
```
{
  "following": "string"
}
```



