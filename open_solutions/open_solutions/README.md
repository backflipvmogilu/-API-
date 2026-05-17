# Open Solutions API

Backend API сервис для автоматизации процесса закупок розничной сети.

Проект разработан с использованием Python, Django и Django REST Framework.

---

# Функционал

* регистрация пользователей;
* авторизация пользователей;
* просмотр каталога товаров;
* просмотр карточки товара;
* добавление товаров в корзину;
* удаление товаров из корзины;
* оформление заказов;
* просмотр списка заказов;
* REST API документация Swagger.

---

# Стек технологий

* Python 3
* Django
* Django REST Framework
*  / SQLite
* drf-spectacular (Swagger)
* Git

---

# Установка проекта

## 1. Клонировать репозиторий

```bash
git clone <https://github.com/backflipvmogilu/-API-/tree/main/open_solutions>
```

---

## 2. Перейти в папку проекта

```bash
cd open_solutions
```

---

## 3. Создать виртуальное окружение

```bash
python -m venv .venv
```

---

## 4. Активировать виртуальное окружение

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 5. Установить зависимости

```bash
pip install -r requirements.txt
```

---

# Запуск проекта

## Выполнить миграции

```bash
python manage.py migrate
```

---

## Запустить сервер

```bash
python manage.py runserver
```

---

# Swagger документация

После запуска проекта Swagger доступен по адресу:

```text
http://127.0.0.1:8000/swagger/
```

---

# Основные API endpoints

## Регистрация пользователя

```http
POST /api/v1/user/register/
```

---

## Авторизация пользователя

```http
POST /api/v1/user/login/
```

---

## Список товаров

```http
GET /api/v1/products/
```

---

## Карточка товара

```http
GET /api/v1/products/<id>/
```

---

## Корзина

```http
GET /api/v1/basket/
POST /api/v1/basket/
DELETE /api/v1/basket/
```

---

## Оформление заказа

```http
POST /api/v1/order/confirm/
```

---

## Список заказов

```http
GET /api/v1/orders/
```

---

## Детальная информация о заказе

```http
GET /api/v1/orders/<id>/
```
