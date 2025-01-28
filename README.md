## Описание
Сервис для выбора фильма.

Основные возможности:
- добавить мнение о фильме
- получить рандомный фильм с рецензией

## Технический стек
- Python
- Flask
- Alembic
- Jinja2

## Запуск проекта

1.Создайте файл .env. По необходимости, внесите свои данные.
```
cp env_example .env
nano .env
```

2.Установите и активируйте виртуальное окружение

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

3.Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 


4.Запустите проект:

```
flask run
```