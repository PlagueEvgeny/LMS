from fastapi import FastAPI
from fastapi import HTTPException
from math import sqrt 

app = FastAPI(title="LMS Mashinarium")

@app.get("/")
def get_course():
    return "Python programming"


@app.get("/{name}")
def get_coures_name(name: str):
    return name

@app.get("/square/{number}")
def get_square(number:int):
    return {"number": number, "square": number**2 }


@app.get("/power/{a}/{b}")
async def get_power(a:int, b:int):
    if b < 0:
        raise HTTPException(status_code=400, detail="Отрицательная степень запрещена") 

    try:
        result = a ** b
        return { "a": a, "b": b, "result": result }
    except OverflowError:
        raise HTTPException(status_code=400, detail="Число слишком большое")


@app.get("/sqrt/{number}")
async def get_sqrt(number:int):
    if number < 0:
        raise HTTPException(status_code=400, detail="Квадратный корень из отрицательного цисла не возможен") 

    try:
        result = sqrt(number)
        return { "number": number,  "result": result }
    except OverflowError:
        raise HTTPException(status_code=400, detail="Число слишком большое")
    

@app.get("/mod/{a}/{b}")
async def get_mod(a:int, b:int):
    if b == 0:
        raise HTTPException(status_code=400, detail="Деление на ноль запрещено") 

    try:
        result = a % b
        return { "a": a, "b": b, "result": result }
    except OverflowError:
        raise HTTPException(status_code=400, detail="Число слишком большое")