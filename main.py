from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/calculate")
def calculate(a: float, b: float, op: str):
    if op == "add":
        return {"result": a + b}
    elif op == "sub":
        return {"result": a - b}
    elif op == "mul":
        return {"result": a * b}
    elif op == "div":
        if b == 0:
            return {"error": "Division by zero!"}
        return {"result": a / b}
    else:
        return {"error": "Invalid operation"}
