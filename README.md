# Leboncoing (online marketplace)'s API.

```uvicorn main:app --reload``` in terminal to run on ```localhost:8000```

## End Points

### 1) Authentification
 
#### POST /auth/signup
**request body**: {
<br>
&nbsp; mail: str
<br> &nbsp; nom: str
<br> &nbsp; mdp: str
<br>}
<br>
*return auth_token: str*

#### POST /auth/login
**request body**: {
<br>
&nbsp; mail: str
<br> &nbsp; mdp: str
<br>
}
<br>
*return auth_token: str*

### 2) Navigation

#### GET /products/all
**request body**: {}
<br>
**queries**: {
<br>&nbsp;
    **filter** ( category = str, name = str, price > = < float )
<br>&nbsp;
    **sort** ( id: int, price: int, name: str, category: str )
<br>&nbsp;
    **pagination** ( itemsperpage: int, page: int )<br>
}<br>
*return articles: list[Article]*

#### GET /products/{id}
**params**: {
<br>&nbsp;
    id: int
<br>}<br>
**request body**: {}
<br>
**queries**: {
<br>&nbsp; 
    **filter** ( fields = [Enum] )
<br>}<br>
*return articles: Article **or** list[Article.fields]* 

#### GET /categories
**request body**: {}
<br>
**queries**: {
<br>&nbsp; 
    **filter** ( name = str)
<br>}<br>
*return categories: list[Category]* 