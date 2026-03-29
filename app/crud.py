from app.database import SessionLocal
from app.tables import Todo

def create_todo(db,todo):
    db_todo = Todo(title = todo.title,description = todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todos(db,todo):
    
    return db.query(Todo).all()

def get_todos_by_id(db,todo):
    
    return db.query(Todo).filter(Todo.todo_id == todo.todo_id).first()

def update_todo_by_id(db,todo):
    
    db_todo = db.query(Todo).filter(Todo.todo_id == todo.todo_id).first()
    if not db_todo:
        return "No Todos to Update"
    db_todo.status = todo.status
    db_todo.title = todo.title
    db_todo.description = todo.description
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo_by_id(db,todo):
    db_todo = get_todos_by_id(db,todo)
    if not db_todo:
        return "No Todos to delete"
    db.delete(db_todo)
    db.commit()
    return db_todo