import json

import requests
import pytest
#NAME:
def test_get_posts():
#ACTION: Отправить запрос на получение списка постов
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
#ACTION: Получить код ответа
    status_code = response.status_code
#ACTION: Получить ответ в виде JSON
    data = response.json()
    print(data)
#ACTION: Проверить что статус кода ответа 200
    assert response.status_code == 200
#ACTION: Проверить что в списке постов, указаны все посты, которы есть в базе данных
    assert len(data) == 100
#NAME:
def test_posts_posts():
#ACTION: Сгенирировать тело запроса
    payload = {
    "userId": 1,
    "title": "testik",
    "body": "testik"
    }
#ACTION: Отправить запрос на создание поста
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
#ACTION: Получить код ответа
    status_code = response.status_code
#ACTION: Получить ответ в виде JSON
    data = response.json()
    print(data)
#ACTION: Проверить что статус кода ответа 201
    assert status_code == 201
#ACTION: Проверить что поля созданного поста соотвествуют значениям тела, которого мы передавали
    assert data["userId"] == payload["userId"]
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]

#NAME
def test_put_posts():
#ACTION: Создать новый пост
    payload_to_create = {
        "userId": 2,
        "title": "test",
        "body": "test"
    }
    response_create_post = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload_to_create).json()
#ACTION: Сгенерировать данные для обновления поста
    payload_to_update = {
        "userId": 1,
        "title": "testik",
        "body": "testik"
    }
#ACTION: Отправить запрос на обновление поста
    response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{response_create_post["id"]}", json=payload_to_update)
#ACTION: Получить код ответа
    status_code = response.status_code
    print(status_code)
#ACTION: Получить ответ в виде JSON
    data = response.json()
#ACTION: Проверить что статус кода ответа 200
    assert status_code == 200
#ACTION: Проверить что поля созданного ранее поста обновились
    assert data["userId"] == 1
    assert data["title"] == "testik"
    assert data["body"] == "testik"

#NAME
def test_delete_posts():
#ACTION: Создать новый пост
    payload_to_create = {
        "userId": 2,
        "title": "test",
        "body": "test"
    }
    response_create_post = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload_to_create).json()
#ACTION: Отправить запрос на получение списка постов
    response = requests.delete(f"https://jsonplaceholder.typicode.com/post/{response_create_post["id"]}").json()
#ACTION: Получить код ответа
    status_code = response.status_code
#ACTION: Проверить что пост был удален, с помощью запроса на чтение
    read_post = requests.get(f"https://jsonplaceholder.typicode.com/posts/{response_create_post["id"]}")
#ACTION: Проверить что статус кода ответа 204
    assert status_code == 204
#ACTION: Проверить, что запрос на чтение поста по айди падает с 404 ошибкой, потому что пост удален
    assert read_post.status_code == 404


@pytest.mark.parametrize(
    "field, value",
    [
        ("userId", "3"),
        ("title", "testik"),
        ("body", "testik")

    ]
)
#NAME
def test_patch_patch(field,value):
#ACTION: Создать новый пост
    payload_to_create = {
        "userId": 2,
        "title": "test",
        "body": "test"
    }
    response_create_post = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload_to_create).json()
#ACTION: Отправить запрос на обновление поста
    response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{response_create_post["id"]}", json={field : value})
#ACTION: Получить код ответа
    status_code = response.status_code
    print(status_code)
#ACTION: Получить ответ в виде JSON
    data = response.json()
#ACTION: Проверить что статус кода ответа 200
    assert status_code == 200
#ACTION: Проверить что поля созданного ранее поста обновились
    assert data[field] == value
