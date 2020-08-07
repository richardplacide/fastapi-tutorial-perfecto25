from tutorial.main import app, templates
from fastapi import Request


@app.get("/next")
async def next(request: Request):
    #return {"message":"What's next ?"}
    content = "What is next my good sir"
    return templates.TemplateResponse("home.html", {"request": request, "content": content})