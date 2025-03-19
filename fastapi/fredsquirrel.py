import json

from fastapi import FastAPI

app = FastAPI()


class Squirrel():
    def __init__(self, name, location):
        self.name = name
        self.location = location


class SquirrelEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Squirrel):
            return obj.__dict__
        return super().default(obj)


squirrels = {"0": Squirrel("Fred", "PO369NX")}
id = "0"


@app.get("/")
def get_squirrels():
    return {key: vars(squirrel) for key, squirrel in squirrels.items()}
    # return json.dumps(squirrels, cls=SquirrelEncoder, indent=4)


@app.get("/spot/{id}")
def get_squirrel(id):
    print(type(id))
    squirrel = squirrels.get(id)
    return {
        "name": squirrel.name,
        "location": squirrel.location,
    }


@app.put("/spot/{id}")
def spot_squirrel(name, location):
    global id
    id = str(int(id) + 1)
    squirrel = Squirrel(name, location)
    squirrels[id] = squirrel
    return {
        "name": squirrel.name,
        "location": squirrel.location,
    }
