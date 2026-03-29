from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from app.models import AddTodo
from app.database import SessionLocal
from app.crud import *
from app.database import Base,engine
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/AddTodos')
def add_todos(todo : AddTodo, db : Session = Depends(get_db)):
    try:
        data = create_todo(db,todo)
        
        return { "data" : data, "status": 200,"success" : True}
    except Exception as e:
        print(e)
        return {"status" : 400,"success" : False}
@app.get('/GetTodos')
def get_todos_all(skip : int = 0,limit : int = 10,db: Session = Depends(get_db)):
    
    try:
        data,count = get_todos(db,skip,limit)
        remaining = count - (skip+limit)
        return {"data" : data, "remaining" : remaining, "status": 200,"success" : True}
    except Exception as e:
        print(e)
        return {"status" : 400,"success" : False}
    
@app.put('/UpdateTodos')
def update_todos(todo,db: Session = Depends(get_db)):
    try: 
        data = update_todo_by_id(db,todo.todo_id)
        
        return {"data":data,"status": 200,"success" : True}
    except Exception as e:
        print(e)
        return {"status" : 400,"success" : False}

@app.delete('/DeleteTodos')
def delete_tods(todo,db : Session = Depends(get_db)):
    try:
        data = delete_todo_by_id(db,todo.todo_id)
        return {"status": 200,"success" : True}
    except Exception as e:
        print(e)
        return {"status" : 400,"success" : False}