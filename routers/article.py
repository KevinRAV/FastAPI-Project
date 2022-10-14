from fastapi import APIRouter

# class Article(BaseModel):
#     id: str
#     name: str
#     vendeur: float
#     categorie: []
#     price: float
#     avis: []
#     description: str
#     stock: int


router = APIRouter()


@router.get("/articles")
def get_all_articles(article_id: str, name: str):
    articles = {"id": article_id, "name": name}
    return articles


@router.get("/articles/{article_id}")
def get_factory_by_id(article_id: str, needy: str):
    article = {"id": article_id, "needy": needy}
    return article

