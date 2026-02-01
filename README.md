# Flask TODO App

Простое веб-приложение для управления списком задач на Flask.

## Возможности

- Создание, редактирование и удаление задач
- Хранение данных в JSON файле
- Минималистичный интерфейс с Material Icons

## Технологии

- Python 3
- Flask 3.0.3
- Jinja2 шаблоны
- JSON для хранения данных

## Установка

1. Клонировать репозиторий:
```bash
git clone https://github.com/Lu7474/flask-todo-app.git
cd flask-todo-app
```

2. Создать виртуальное окружение:
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

3. Установить зависимости:
```bash
pip install flask
```

4. Запустить приложение:
```bash
python main.py
```

5. Открыть http://127.0.0.1:5000 в браузере

## Структура проекта

```
TODO/
├── main.py           # Flask роуты и конфигурация
├── todo.py           # Логика работы с задачами (CRUD)
├── todo_list.json    # Хранилище данных
├── templates/
│   ├── index.html    # Главная страница
│   └── edit_task.html # Страница редактирования
├── requirements.txt
└── README.md
```

## API

| Маршрут | Метод | Описание |
|---------|-------|----------|
| `/` | GET | Список всех задач |
| `/add_task` | POST | Добавить задачу |
| `/delete/<id>` | GET | Удалить задачу |
| `/edit/<id>` | GET/POST | Редактировать задачу |

## Лицензия

MIT
