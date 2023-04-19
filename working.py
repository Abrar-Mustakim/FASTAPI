from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

# uvicorn working:app --reload
app = FastAPI()

class Item(BaseModel):
    name : str
    price : float 
    brand : Optional[str] = None

class UpdateItem(BaseModel):
    name : Optional[str] = None 
    price : Optional[float] = None 
    brand : Optional[str] = None 

@app.get("/")
def home():
    #return {"Data":"Test"}
    return "Hello World"

@app.get("/about")
def about():
    return {"Data":"about"}

'''
inventory = {
    1 : {"Name": "Air Force 1",
         "Price": 100,
         "Brand": "Nike"}
}
'''
inventory = {}
'''
@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]
'''

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the Item you would like to view", gt=0, le=10)): #ge= greater than or equal, gt: greater than, le: less than or equal
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="The Item ID Not Exist")
    return inventory[item_id]


'''
@app.get("/get-by-name/{item_id}")
def get_item(*, item_id:int, Name: Optional[str] = None, test: int=None):

    for item_id in inventory:
        if inventory[item_id].name == Name: 
            return inventory[item_id]
        
    return {"Data" : "Not Found"}
'''

@app.get("/get-by-name/")
def get_item(*, Name: Optional[str] = None, test: int=None):

    for item_id in inventory:
        if inventory[item_id].name == Name: 
            return inventory[item_id]
        
    raise HTTPException(status_code=404, detail="Data Not Found") #status_code=status.HTTP_404_NOT_FOUND


@app.post("/create-item/{item_id}")
def create_item(item_id:int, item : Item):
    if item_id in inventory:
        raise HTTPException(status_code=404, detail="The Item already exist")
    inventory[item_id] = item
    return inventory[item_id]


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item:UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="The Item ID Not Exist")
    
    if item.name != None:
        inventory[item_id].name = item.name 

    if item.price != None:
        inventory[item_id].price = item.price 

    if item.brand != None:
        inventory[item_id].brand = item.brand 
    
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id:int = Query(..., description="The ID of the item to DELETE", gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="The Item ID Not Exist")
    
    del inventory[item_id]
    return {"Success": "Item Deleted"}



'''
Small Documents for Query Parameters

from fastapi import Depends, FastAPI, Query

app = FastAPI()


class CustomQueryParams:
    def __init__(
        self,
        foo: str = Query(..., description="Cool Description for foo"),
        bar: str = Query(..., description="Cool Description for bar"),
    ):
        self.foo = foo
        self.bar = bar


@app.get("/test-query/")
async def get_by_query(params: CustomQueryParams = Depends()):
    return params
'''