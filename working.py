from fastapi import FastAPI 

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

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]