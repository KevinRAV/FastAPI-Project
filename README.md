# Leboncoing (online marketplace)'s API.

---

```uvicorn main:app --reload``` in terminal to run on ```localhost:8000```

## End Points (24)

### &nbsp; 1) Profile

---
 

* #### POST /auths/signup

**params**: { }

**request body**: {

&nbsp; mail: str

&nbsp; name: str

&nbsp; password: str

}

*return auth_token: str*

<br>

* #### POST /auths/login
**params**: { }

**request body**: {

&nbsp; mail: str

&nbsp; password: str

}

*return auth_token: str*

<br>

* #### GET /users/me

**Header** : { 

&nbsp; auth_token: str

}

**request body**: { }

*return active_user: User*

<br>

* #### GET /commands

**Header** : { 

&nbsp; auth_token: str

}

**request body**: { }

**queries**: {

&nbsp; filter ( product_name = str, date > = < str ),

&nbsp; sort ( product_name: str, date: str, seller: int ),

&nbsp; **pagination** ( pagesize: int, page: int )

}

*return buy_history: list[Command]*

<br>

* #### GET /commands/{user_id}

**Header** : { 

&nbsp; auth_token: str

}

**request body**: { }

**queries**: {

&nbsp; filter ( product_name = str, date > = < str ),

&nbsp; sort ( product_name: str, date: str, seller: int ),

&nbsp; **pagination** ( pagesize: int, page: int )

}

*return sells_history: list[Command]*

<br>

### &nbsp; 2) Browsing

---

* #### GET /products
**request body**: { }

**params**: { }

**queries**: {

&nbsp; **filter** ( category = str, seller = int, name = str, price > = < float)

&nbsp; **sort** ( id: int, price: int, name: str, category: str )

&nbsp; **pagination** ( page_size: int, page: int )

}

*return products: list[Product]*

<br>

* #### GET /products/{id}
**params**: {

&nbsp; id: int

}

**request body**: { }

**queries**: {

&nbsp; **filter** ( fields = [Enum] )

}

*return products: Product **or** list[Product.fields]*

<br>

* #### GET /categories
**params**: { }

**request body**: { }

**queries**: {

&nbsp; **filter** ( name = str )

&nbsp; **sort** ( id: int, name: str )

}

*return categories: list[Category]*

<br>

* #### GET /comments/{product_id}
**params**: {

&nbsp; product_id: int

}

**request body**: { }

**queries**: {

&nbsp; **filter** ( stars > = < int, message = str )

&nbsp; **sort** ( stars: int )

&nbsp; **pagination** ( page_size: int, page: int )

}

*return comments: list[Comment]*

<br>

* #### PUT /comments/{product_id}

**Header** : { 

&nbsp; auth_token: str

}

**params**: {

&nbsp; product_id: int

}

**request body**: {

&nbsp; stars: int

&nbsp; message: str

}

**queries**: { }

*return updated_comment: Comment*

<br>

* #### POST /comments/{product_id}

**Header** : { 

&nbsp; auth_token: str

}

**params**: {

&nbsp; product_id: int

}

**request body**: {

&nbsp; stars: int

&nbsp; message: str

}

**queries**: { }

*return new_comment: Comment*

<br>

* #### DELETE /comments/{product_id}

**Header** : { 

&nbsp; auth_token: str

}

**params**: {

&nbsp; product_id: int

}

**request body**: { }

**queries**: { }

*return deleted_comment: Comment*

<br>

### &nbsp; 3) Cart

---

* #### GET /carts

**params**: { }

**Header** : { 

&nbsp; auth_token: str

}

**request body**: { }

**queries**: { }

*return carts: list[Cart]*

<br>


* #### DELETE /carts

**Header** : { 

&nbsp; auth_token: str

}

**params**: { }

**request body**: { }

**queries**: { }

*return deleted_carts: list[Cart]*

<br>

* #### PATCH /carts/{product_id}

**Header** : { 

&nbsp; auth_token: str

}

**params**: {

&nbsp; product_id: int

}

**request body**: {

&nbsp; quantity: int 

}

**queries**: { }

*return carts: Cart*

<br>

* #### POST /carts

**Header** : { 

&nbsp; auth_token: str

}

**params**: { }

**request body**: {

&nbsp; product_id: int

&nbsp; quantity: int 

}

**queries**: { }

*return carts: Cart*

<br>

* #### DELETE /carts/{product_id}
**Header** : { 

&nbsp; auth_token: str

}

**params**: {

&nbsp; product_id: int

}

**request body**: { }

**queries**: { }

*return carts: Cart*

<br>

* #### POST /commands
**Header** : {

&nbsp; auth_token: str

}

**params**: { }

**request body**: { }

*return commands: list[Command]*

<br>

### &nbsp; 4) Selling

---

* #### POST /products

**Header** : { 

&nbsp; auth_token: str

}

**request body**: {

&nbsp; product_name: str,

&nbsp; price: int,

&nbsp; category: int,

&nbsp; description: str,

&nbsp; stock: int,

&nbsp; image: str,

}

*return new_product: Product*

<br>

* #### PUT /products/{id}

**Header** : { 

&nbsp; auth_token: str

}

**params**: { 

&nbsp; id: int,

}

**request body**: {

&nbsp; product_name: str,

&nbsp; price: int,

&nbsp; category: int,

&nbsp; description: str,

&nbsp; stock: int,

&nbsp; image: str,

}

*return updated_product: Product*

<br>

* #### DELETE /products/{id}

**Header** : { 

&nbsp; auth_token: str

}

**params**: { 

&nbsp; id: int,

}

**request body**: { }


*return deleted_product: Product*

<br>

### &nbsp; 5) Admin

---

* #### DELETE /comments/{product_id}/{user_id}

**params**: {

&nbsp; product_id: int

&nbsp; user_id: int

}

**request body**: { }

*return deleted_comment: Comment*

<br>

* #### POST /products/{seller_id}

**Header** : { 

&nbsp; auth_token: str

}

**params**: {

&nbsp; seller_id: int

}

**request body**: {

&nbsp; name : str

&nbsp; price : float

&nbsp; description : str | none

&nbsp; image : str | none

&nbsp; stock : int 

&nbsp; category_id : int 

&nbsp; seller_id : int

}

*return posted_product: Product*

<br>

* #### POST /categories/

**Header** : { 

&nbsp; auth_token: str

}

**params**: { }

**request body**: {

category_name : str

}

*return posted_category: Category*

* #### DELETE /categories/{id}

**Header** : { 

&nbsp; auth_token: str

}

**params**: { 

id : int

}

**request body**: { }

*return deleted_category: Category*
