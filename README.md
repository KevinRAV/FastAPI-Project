# Leboncoing (online marketplace)'s API.

```uvicorn main:app --reload``` in terminal to run on ```localhost:8000```

## End Points (24)

### &nbsp; 1) Profile
 
#### POST /auth/signup
**request body**: {
&nbsp; mail: str
&nbsp; name: str
&nbsp; password: str
}
*return auth_token: str*

#### POST /auth/login
**request body**: {
&nbsp; mail: str
&nbsp; password: str
}
*return auth_token: str*

#### GET /users
**request body**: {
&nbsp;auth_token: str
}
*return active_user: User*

#### GET /commands
**request body**: {
&nbsp;auth_token: str
}
**queries**: {
&nbsp;filter ( product_name = str, date > = < str ),
&nbsp;sort ( product_name: str, date: str, seller: int ),
&nbsp; **pagination** ( pagesize: int, page: int )
}
*return buy_history: list[Command]*

#### GET /commands/{user_id}
**request body**: {
&nbsp;auth_token: str
}
**queries**: {
&nbsp;filter ( product_name = str, date > = < str ),
&nbsp;sort ( product_name: str, date: str, seller: int ),
&nbsp; **pagination** ( pagesize: int, page: int )
}
*return sells_history: list[Command]*

### &nbsp; 2) Browsing

#### GET /products
**request body**: {}
**queries**: {
&nbsp; **filter** ( category = str, seller = int, name = str, price > = < float ),
&nbsp; **sort** ( id: int, price: int, name: str, category: str ),
&nbsp; **pagination** ( pagesize: int, page: int )
}
*return articles: list[Article]*

#### GET /products/{id}
**params**: {
&nbsp; id: int
}
**request body**: {}
**queries**: {
&nbsp; **filter** ( fields = [Enum] )
}
*return articles: Article **or** list[Article.fields]*

#### GET /categories
**request body**: {}
**queries**: {
&nbsp; **filter** ( name = str)
}
*return categories: list[Category]*

#### GET /categories/{id}

#### GET /comments/{product_id}

#### PUT /comments/{product_id}

#### POST /comments/{product_id}

#### DELETE /comments/{product_id}

### &nbsp; 3) Cart

#### GET /carts
**request body**: {}
**queries**: {
&nbsp; **filter** ( owner = str, )
}
*return basket: list[Articles]*

#### DELETE /carts

#### PATCH /carts/{product_id}

#### POST /carts/{product_id}

#### DELETE /carts/{product_id}

#### POST /commands

### &nbsp; 4) Selling

#### POST /products
**request body**: {
&nbsp;auth_token: str,
&nbsp;product_name: str,
&nbsp;price: int,
&nbsp;category: int,
&nbsp;description: str,
&nbsp;stock: int,
&nbsp;image: str,
}
*return new_product: Product

#### PUT /products/{id}
**request body**: {
&nbsp;auth_token: str,
&nbsp;product_name: str,
&nbsp;price: int,
&nbsp;category: int,
&nbsp;description: str,
&nbsp;stock: int,
&nbsp;image: str,
}
*return updated_product: Product

#### DELETE /products/{id}
**request body**: {
&nbsp;auth_token: str
}
*return deleted_product: Product

### &nbsp; 5) Admin

#### POST /auth/admin
**request body**: {
&nbsp; mail: str
&nbsp; name: str
&nbsp; password: str
}
*return auth_token: str*

#### DELETE /comments/{product_id}/{user_id}
**params**: {
&nbsp;product_id: int,
&nbsp;user_id: int,
}
**request body**: {
&nbsp;auth_token: str
}
*return deleted_comment: Comment