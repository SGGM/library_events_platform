# Сервис по созданию и отслеживанию мероприятий.

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fastapi?style=plastic)

## Содержание
- [Сервис по созданию и отслеживанию мероприятий](#сервис-по-созданию-и-отслеживанию-мероприятий)
  - [Содержание](#содержание)
  - [Описание](#описание)
  - [Установка](#установка)
  - [Запуск](#запуск)
  - [Конечные точки](#конечные-точки)
  - [Требования к системе](#требования-к-системе)
  - [Дальнейшее развитие и возможные улучшения](#дальнейшее-развитие-и-возможные-улучшения)
  

## Описание
API сервис позволяет создавать пользователей, организации и мероприятия. Аутентификация реализована при помощи JWT токенов.<br>
Использованный стек технологий: Python, Django, Django_rest_framework, PostgreSQL, Celery, Redis, Docker.<br>


## Установка
```bash
git clone github.com/SGGM/library_events_platform.git
```


## Запуск
```bash
cd library_events_platform/
docker-compose up --build -d
```


## Конечные точки
1. Для регистрации пользователя, входа в систему и выхода из нее:
```bash
0.0.0.0:80/api/v1/user/register/
0.0.0.0:80/api/v1/user/login/
0.0.0.0:80/api/v1/user/logout/
```
superuser:
```txt
{
    "email": "admin@mail.ru",
    "password": "admin"
}
```


2. Для создания организации:
```bash
0.0.0.0:80/api/v1/organization/create/
```


3. Для создания мероприятия, просмотра отдельного мероприятия с выведением всех действующих пользователей по организациям и просмотра всех мероприятий с возможностью фильтрации и поиска, а также пагинацией.
```bash
0.0.0.0:80/api/v1/event/create/
0.0.0.0:80/api/v1/event/<str:event_title>/
0.0.0.0:80/api/v1/all_events/
```


4. Для подключения к чату. **На данный момент не работает при использовании docker.**
```bash
0.0.0.0:80/chat/
```


## Требования к системе
- [x] DRF >= 3.12, Django >= 3.2.
- [x] Реализована возможность хранения номера телефона пользователя, использовано поле PhoneNumberField из библиотеки phonenumber_field.
- [x] При создании и авторизации пользователя используется email, вместо username.
- [x] Для аутентификации используется JWT Token.   
- [x] Создана модель Organization со следующими полями:
```txt
{
    "title": CharField,
    "description": TextField,
    "address": CharField,
    "postcode": CharField,
    "employees": ManyToManyField
}
```
- [x] Создана моедель Event со следающими полями:
```txt
{
    "title": CharField,
    "description": TextField,
    "organizations": ManyToManyField,
    "image": ImageField,
    "date": DateTimeField,
    "created": BooleanField
}
```
- [x] Для запуска проекта используется Docker.
- [x] В панели администратора добавлена фильтрация и поиск.
- [x] Вывод информации и создание записей по api доступно только зарегистрированным пользователям.
- [x] При создании мероприятия используется sleep 60 секунд. Для фоновой обработки используется Celery + Redis.
- [ ] Создан чат для пользователей. На данный момент при использовании Docker не работает.
Запуск:
```bash
daphne -b 0.0.0.0 -p 8080 library_events_platform.asgi:application
```
- [ ] При просмтре мероприятия выведение превью изображения.

## Дальнейшее развитие и возможные улучшения
1. **Реализация работы чата с использованием Docker**.
2. **Реализация вывода превью изображения**.
3. Улучшение системы аутентификации при помощи JWT:
    - Использование access и refresh токенов при помощи djangorestframework-simplejwt.
4. Создание openapi документации.
5. Написание тестов.
