from fastapi import FastAPI
from src.users import router as router_auth
from src.authdata import actual_user
from src.notes import router as router_notes
from src.statistics import router as router_stat

import uvicorn

app = FastAPI(title='MyNotes')


@app.get('/')
def root():
    return {'message': f'{actual_user.__int__()}'}


app.include_router(router_auth)

app.include_router(router_notes)

app.include_router(router_stat)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
