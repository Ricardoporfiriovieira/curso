from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from typing import List, Optional

from models import Curso

app = FastAPI()

cursos = {
    1:{
        "titulo" : "dale e sua filosofia",
        "aulas" : 300,
        "horas" : 1000 
    },
    2:{
        "titulo" : "vapo e sua forma de ver o mundo",
        "aulas" : 200,
        "horas" : 700
    }, 

}

@app.get("/cursos")
async def get_cursos():
    return cursos

@app.get("/cursos/{id_curso}")
async def query_cursos(id_curso: int):
    try:
        query_cursos = cursos[id_curso]
        query_cursos.update({"id":"{id_curso}"})

        return query_cursos
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')



@app.post("/cursos")
async def update_curso(curso: Curso, status_code=status.HTTP_201_CREATED):

    prox_id: int = len(cursos)+1
    cursos[prox_id] = curso
    del cursos[prox_id].id
    return cursos[prox_id]
    
    

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

