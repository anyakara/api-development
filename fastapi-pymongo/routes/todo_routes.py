from fastapi import APIRouter
from models.todo import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

# initializing an API Router
router = APIRouter()

# GET Request Method
@router.get('/')
async def get_todos():
    """To fetch todos from the collection."""
    todos = list_serial(collection_name.find())
    return todos


# POST Request Method
@router.post('/')
async def post_todo(todo: Todo):
    """To add a todo to the collection."""
    collection_name.insert_one(dict(todo))
    return {"data": dict(todo)}


# PUT Request Method
@router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    """To update a todo already in the collection."""
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    return {"data": dict(todo)}


# DELETE Request Method
@router.delete("/{id}")
async def delete_todo(id: str):
    """To delete a todo if it's in the collection."""
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"data": id}


'''
# these are routes too, but they are assuming that we are not using
# mongodb as the nosql database. 

# get request
@app.get("/", tags=['ROOT'])
def root() -> dict:
    return {"App name": "Minimal Todo"}


# GET --> Read Todo
@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    """Replace returning todos, with some sort of connection
    to a database like mysql or mongodb. see the updates and update accordingly."""
    return {"data": todos}


# POST --> Create Todo
@app.post('/todo', tags=['todos'])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return { "data": "A todo has been added!" }


# PUT --> Update Todo
@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todo['Activity'] = body['Activity']
            return {"data": f"Todo with id {id} has been updated"}
    return {
        "data": f"Todo with this id number {id} was not found!"
        }

# DELETE --> Delete Todo
@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been deleted"
            }
    return {
        "data": f"this todo with id {id} wasn't found!"
    }

# especially useful for testing purposes
todos = [
    {
        "id": "1",
        "Activity": "Jogging for 2 hours at 7:00 AM."
    },
    {
        "id": "2",
        "Activity": "Writing 3 pages of my new book at 2:00 PM."
    }
]


'''