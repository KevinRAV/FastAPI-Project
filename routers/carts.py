from fastapi import APIRouter

router = APIRouter()


@router.get("/categories")
def get_categories(search: str = "", sort: str = ""):
    categories = {"searching": search, "sorting": sort}
    return categories

