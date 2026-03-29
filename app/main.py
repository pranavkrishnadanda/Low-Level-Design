from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/AddTodos')
def ImplmentTodos():
    # Logic for Implmenting Todos
    
    return {"status": 200,"success" : True}

@app.get('GetTodos')
def GetTodos():
    # Logic for Getting Todos
    
    return {"status": 200,"success" : True}
    
@app.post('/UpdateTodos')
def UpdateTodos():
    #Logic for Updating Todos
    
    return {"status": 200,"success" : True}
