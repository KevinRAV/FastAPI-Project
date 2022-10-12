# Leboncoing (online marketplace)'s API.

```uvicorn main:app --reload``` in terminal to run on ```localhost:8000```

## End Points (24)

---

### &nbsp; 1) Profile

---
 
#### POST /auth/signup
**params**: { }

**request body**: {
&nbsp; mail: str
&nbsp; name: str
&nbsp; password: str
}
*return auth_token: str*

#### POST /auth/login
**params**: { }

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

---

#### GET /products
**request body**: {}

**params**: {}

**queries**: {

&nbsp; **filter** ( category = str, seller = int, name = str, price > = < float)

&nbsp; **sort** ( id: int, price: int, name: str, category: str )

&nbsp; **pagination** ( page_size: int, page: int )

}

*return products: list[Product]*

#### GET /products/{id}
**params**: {

&nbsp; id: int

}

**request body**: {}

**queries**: {

&nbsp; **filter** ( fields = [Enum] )

}

*return products: Product **or** list[Product.fields]*

#### GET /categories
**params**: {}

**request body**: {}

**queries**: {

&nbsp; **filter** ( name = str )

&nbsp; **sort** ( id: int, name: str )

}

*return categories: list[Category]*

#### GET /categories/{id}
**params**: {

&nbsp; id: int

}

**request body**: {}

**queries**: { }

*return categorie: Category*

#### GET /comments/{product_id}
**params**: {

&nbsp; product_id: int

}

**request body**: {}

**queries**: {

&nbsp; **filter** ( stars > = < int, message = str )

&nbsp; **sort** ( stars: int )

&nbsp; **pagination** ( page_size: int, page: int )

}

*return comments: list[Comment]*

#### PUT /comments/{product_id}
**params**: {

&nbsp; product_id: int

}

**request body**: {

&nbsp; auth_token: str

&nbsp; stars: int

&nbsp; message: str

}

**queries**: {}

*return updated_comment: Comment*

#### POST /comments/{product_id}
**params**: {

&nbsp; product_id: int

}

**request body**: {

&nbsp; auth_token: str

&nbsp; stars: int

&nbsp; message: str

}

**queries**: { }

*return new_comment: Comment*

#### DELETE /comments/{product_id}
**params**: {

&nbsp; product_id: int

}

**request body**: {

&nbsp; auth_token: str

}

**queries**: { }

*return deleted_comment: Comment*

### &nbsp; 3) Cart

---

#### GET /carts
**params**: { }

**request body**: {

&nbsp; auth_token: str

}

**queries**: { }

*return carts: list[Cart]*


#### DELETE /carts
**params**: { }

**request body**: {

&nbsp; auth_token: str

}

**queries**: {}

*return deleted_carts: list[Cart]*

#### PATCH /carts/{product_id}
**params**: {

&nbsp; product_id: int

}

**request body**: { 

&nbsp; auth_token: str

&nbsp; quantity: int 

}

**queries**: { }

*return carts: Cart*

#### POST /carts
**params**: { }

**request body**: {

&nbsp; auth_token: str

&nbsp; product_id: int

&nbsp; quantity: int 

}

**queries**: {}

*return carts: Cart*

#### DELETE /carts/{product_id}
**params**: {

&nbsp; product_id: int

}

**request body**: {

&nbsp; auth_token: str

}

**queries**: { }

*return carts: Cart*

#### POST /commands
**params**: { }

**request body**: {

&nbsp; auth_token: str

}

*return commands: list[Command]*

<br>

### &nbsp; 4) Selling

---

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

---

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