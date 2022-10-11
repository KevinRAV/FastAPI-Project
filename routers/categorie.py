from fastapi import APIRouter

router = APIRouter()


@router.get("/categorie")
def get_categorie(search: str = "", sort: str = ""):
    categorie = {"searching": search, "sorting": sort}
    return categorie

