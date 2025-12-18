from fastapi import APIRouter, Request
from functions.arethmatic import Arethmatic
import math
import re
import traceback

router = APIRouter(prefix="/api", tags=["calculator"]) 

arith = Arethmatic()
arithSwitcher = {
        "+": arith.add,
        "-": arith.subtract,
        "*": arith.multiply,
        "/": arith.divide,
        "^": arith.power,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log10,
        "ln": math.log,
        "sqrt": math.sqrt,
        "π": math.pi
    }

@router.post("/calc") 
async def list_users(request: Request): 
    data = await request.json() 
    expression = data["expr"] 
    
    expression = re.sub(r'(\d)(π)', r'\1*\2', expression) 
    expression = re.sub(r'(π)(\d)', r'\1*\2', expression) 
    expression = re.sub(r'(\d)(sin|cos|tan|log|ln|sqrt)', r'\1*\2', expression) 
    expression = re.sub(r'\)(\d)', r')*\1', expression) 
    expression = re.sub(r'(\d)\(', r'\1*(', expression)
    

    if not re.match(r'^[0-9+\-*/()., e^a-zA-Zπ]*$', expression): 
        return {"result": "ERR"} 
    try: 
        result = eval(expression, {"__builtins__": None}, arithSwitcher) 

    except Exception as ex: 
        print("❌ Exception occurred while evaluating expression:") 
        traceback.print_exc()
        return {"result": "ERR"} 
    return {"result": result}