# Todo list Website

Build API website with python, and sqlite

## Framework & Library
- [flask](https://pypi.org/project/Flask/)
- [flask_login](https://pypi.org/project/Flask-Login/)
- [flask_wtf](https://pypi.org/project/Flask-WTF/)
- [wtforms](https://pypi.org/project/WTForms/)
- [flask_sqlalchemy](https://pypi.org/project/Flask-SQLAlchemy/)
- [flask_migrate](https://pypi.org/project/Flask-Migrate/)
- 
### Run

```
pip install -r requirements.txt
flask run
```

## APIs

**User**

| Method | Link    | Request   | Decription            |
|--------|---------|-----------|-----------------------|
| POST   | /signup | Form-data | Create a new user     |
| POST   | /login  | Form-data | Login for the website |
| GET    | /logout |           | Login for the website |

**Note**

| Method    | Link                 | Request   | Decription             |
|-----------|----------------------|-----------|------------------------|
| POST, GET | /notes/:username     | Form-data | Create/read a new note |
| POST      | /deleteNote/:note_id |           | Delete a note          |
