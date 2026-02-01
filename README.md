# Flask TODO App

Simple web application for task management built with Flask.

## Features

- Create, edit and delete tasks
- Data stored in JSON file
- Minimalist interface with Material Icons
- Russian language UI

## Tech Stack

- Python 3
- Flask 3.0.3
- Jinja2 templates
- JSON for data storage

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/flask-todo-app.git
cd flask-todo-app
```

2. Create virtual environment:
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install flask
```

4. Run the application:
```bash
python main.py
```

5. Open http://127.0.0.1:5000 in your browser

## Project Structure

```
TODO/
├── main.py           # Flask routes and app configuration
├── todo.py           # Task management logic (CRUD)
├── todo_list.json    # Data storage
├── templates/
│   ├── index.html    # Main page
│   └── edit_task.html # Task editing page
├── requirements.txt
└── README.md
```

## API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Display all tasks |
| `/add_task` | POST | Add new task |
| `/delete/<id>` | GET | Delete task |
| `/edit/<id>` | GET/POST | Edit task |

## License

MIT
