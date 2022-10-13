from fastapi import APIRouter


router = APIRouter()


@router.get("/articles")
def get_all_articles(article_id: str, name: str):
    articles = {"id": article_id, "name": name}
    return articles


@router.get("/articles/{article_id}")
def get_factory_by_id(article_id: str, needy: str):
    article = {"id": article_id, "needy": needy}
    return article

