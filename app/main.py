
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app import database, models
from app.routers import auth, legends, categories, locations

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Legends API",
    description="API para gestión de leyendas costarricenses",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=database.engine)


app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(legends.router,  tags=["Legends"])
app.include_router(categories.router,  tags=["Categories"])
app.include_router(locations.router,  tags=["Locations"])


app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Legends API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)