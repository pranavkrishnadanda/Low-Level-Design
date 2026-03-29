from fastapi import FastAPI
from app.models import AddTodo
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/AddTodos')
def add_todos(todo : AddTodo):
    
    print(todo.title)
    print(todo.description)
    
    return {"status": 200,"success" : True}

@app.get('/GetTodos')
def get_todos():
    
    # Logic for Getting Todos
    
    return {"status": 200,"success" : True}
    
@app.post('/UpdateTodos')
def update_todos(todo_id):
    
    # Logic for Updating Todos
    
    return {"status": 200,"success" : True}
