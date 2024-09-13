## Описание

Тестовое задания для компании Brendwall.
Создал небольшое Django-приложение, которое состоит из двух частей:

- RESTful API для работы с продуктами (создание продукта c POST и получение списка c GET).
- Страница на HTML с использованием JavaScript для отправки данных на RESTful API и отображения продуктов.


## Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/kirillkiselev-slim/brendwall/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt, переходим в бекенд:

```
cd brendwall
```

```
pip install -r requirements.txt
```

## Запуск проекта 
Запустите бекенд

```
python manage.py runserver
```

Запустите фронтенд

```
cd .. && cd brendwall_frontend && python3 -m http.server 3000
```

Пройдите на фронтенд по ссылке `http://localhost:3000/product.html`

## Примеры запросов для API

### 1-ый пример
Method: `Post`
Endpoint: `http://127.0.0.1:8000/api/products/`

Body: 

```
    {   
        "name": "Лед",
        "description": "Очень полезный лед",
        "price": "23"
    }
```

Response: 

```
{
    "id": 18,
    "name": "Лед",
    "description": "Очень полезный лед",
    "price": "23.00"
}
```

Status code: 201
|

### 2-ой пример

Method: `GET`
Endpoint: `http://127.0.0.1:8000/api/products/`

Response: 

```
[
    {
        "id": 19,
        "name": "Арбуз",
        "description": "nice watermelon",
        "price": "2.92"
    },
    {
        "id": 20,
        "name": "Арбуз 23",
        "description": "nice watermelon",
        "price": "2.92"
    },
    {
        "id": 22,
        "name": "Арбуз 2323",
        "description": "nice watermelon",
        "price": "83.00"
    },
    {
        "id": 21,
        "name": "Арбуз 3",
        "description": "nice watermelon",
        "price": "4.00"
    },
    {
        "id": 23,
        "name": "Арбуз 63",
        "description": "nice watermelon",
        "price": "83.00"
    },
    {
        "id": 18,
        "name": "Лед",
        "description": "Очень полезный лед",
        "price": "23.00"
    },
    {
        "id": 25,
        "name": "Морковь",
        "description": "nice carrot",
        "price": "12.32"
    },
    {
        "id": 24,
        "name": "Морковь2",
        "description": "great carrot",
        "price": "23.00"
    }
]
```

Status code: 200


### Использованные технологии

* Python 3.12
* JavaScript
* HTML
* Django 5.1.1
* Django REST framework 3.15.2 
* Sqlite (дефолт для Django)

### Автор

[Кирилл Киселев](https://github.com/kirillkiselev-slim)

