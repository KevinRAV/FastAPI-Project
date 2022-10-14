from fastapi import FastAPI
from routers import auth
from routers import article
from routers import categorie

app = FastAPI()

app.include_router(auth.router)
app.include_router(article.router)
app.include_router(categorie.router)
