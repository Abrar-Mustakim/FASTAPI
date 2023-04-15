from fastapi import FastAPI, Path
from typing import Optional


# uvicorn working:app --reload
app = FastAPI()

@app.get("/")
def home():
    #return {"Data":"Test"}
    return "Hello World"

@app.get("/about")
def about():
    return {"Data":"about"}


inventory = {
    1 : {"Name": "Air Force 1",
         "Price": 100,
         "Brand": "Nike"}
}
'''
@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]
'''

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the Item you would like to view", gt=0, le=10)): #ge= greater than or equal, gt: greater than, le: less than or equal
    return inventory[item_id]



@app.get("/get-by-name/{item_id}")
def get_item(*, item_id:int, Name: Optional[str] = None, test: int=None):

    for item_id in inventory:
        if inventory[item_id]["Name"] == Name: 
            return inventory[item_id]
        
    return {"Data" : "Not Found"}