from fastapi import FastAPI
app = FastAPI()

@app.get('/api/main')
def get_mapdata():
    return {'foo':'bar'}

@app.post('/api/main')
def get_mapdata():
    return {'foo':'bar'}