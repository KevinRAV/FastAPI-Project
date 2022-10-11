from fastapi import APIRouter

router = APIRouter()


@router.get("/categorie")
def get_categorie(categorie_id: str, name: str):
    categorie = {"id": categorie_id, "name": name}
    return categorie

