from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

# Create an instance of FastAPI
app = FastAPI()



# class to define what a user can send data

class Post(BaseModel):
    name: str
    address: str
    published: bool = True
    rating: Optional[int] = None


my_post = [{"name": "My Nsme is Obama", "address": "I live in America", "id": 1},
           {"name": "My Nsme is Putin", "address": "I live in Russia", "id": 2}]


# Decorator(Router)
@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_post():
    return {"data": my_post}

# @app.post("/createpost")
# def create_post(payLoad:dict = Body(...)):
#     print(payLoad)
#     return {"new_post": f"title: {payLoad['title']} content: {payLoad['contents']}"}


# Post validates whether or not it has title and contents
@app.post("/createpost")
def create_post(post:Post):
    print(post.rating)
    print(post.dict())   # convert pydantic model to dictionary
    return {"data": post}

@app.post("/posts")
def create_post(post:Post):
    print(post.rating)
    print(post.dict())   # convert pydantic model to dictionary
    return {"data": post}







