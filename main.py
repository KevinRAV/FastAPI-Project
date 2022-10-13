from fastapi import FastAPI

from routers import auths
from routers import products
from routers import categories
from routers import carts
from routers import commands
from routers import users

app = FastAPI()

app.include_router(auths.router)
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(carts.router)
app.include_router(commands.router)
app.include_router(users.router)
