from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# im able to add any routes depends on my project requeiremnts
 
@app.get("/" , description='This is my first get api')
async def root():
    return {"hi , you are in the root get / "}

@app.post("/")
async def root():
    return {"hi , you are in the root post / "}


@app.get('/users')
async def users():
        return {"hi , you are in the root users /users "}


@app.get("/users/{users_id}" ,  description= " pelease enter only integer variables")
async def usersId(users_id : int):
        return {"hi , you are in the root users /users " : {users_id}}




class FoodCategoryEnum (str,Enum):
    candy =  'candy'
    fruits = 'fruits'
    water = 'water'
@app.get('/Foodmasurment/{foodName}' , description= "you have to only add candy , fruits or water arg")
async def Get_food(foodName :FoodCategoryEnum ):
    if foodName ==FoodCategoryEnum.candy :
        return {"hi , you are in a " :foodName  }
    elif foodName ==FoodCategoryEnum.fruits :
        return {"hi , you are in a " :foodName  }
    elif foodName ==FoodCategoryEnum.water :
        return {"hi , you are in a " :foodName  }
    
 
 
    
fake_items_DB = [{"items_Name": "cake"}, {"items_Name": "drink"}, {"items_Name": "beer"}]
@app.get('/items')
async def List_items(skip: int = 0, limit: int = 10):
    return fake_items_DB[skip: skip + limit]



# using in the url : /items/{item_id}?q=33&short=True
@app.get("/items/{item_id}")
async def addItems(item_id: str, query: str | None = None , short:bool =False):
       item = {"item_id": item_id}
       if query:
        item.update({"item_id": item_id, "query": query})
       if short == True :
        item.update({"description " : " you selected the short True"})
       return item
   

