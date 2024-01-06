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


@app.get("/users/{users_id}")
async def usersId(users_id : int):
        return {"hi , you are in the root users /users " : {users_id}}

class FoodCategoryEnum (str,Enum):
    candy =  'candy'
    fruits = 'fruits'
    water = 'water'
    
@app.get('/Foodmasurment/{foodName}')
async def Get_food(foodName :FoodCategoryEnum ):
    if foodName ==FoodCategoryEnum.candy :
        return {"hi , you are in a " :foodName  }
    elif foodName ==FoodCategoryEnum.fruits :
        return {"hi , you are in a " :foodName  }
    elif foodName ==FoodCategoryEnum.water :
        return {"hi , you are in a " :foodName  }
    
  

    
