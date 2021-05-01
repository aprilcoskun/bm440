from fastapi import APIRouter, Depends, Request
from utils import auth_helper
from fastapi.responses import HTMLResponse
from utils.templates import templates

router = APIRouter(dependencies=[Depends(auth_helper.check_user)])


@router.get("/", response_class=HTMLResponse)
def get_all(request: Request, user=Depends(auth_helper.get_current_user)):
    return templates.TemplateResponse('index.html', {"request": request, "page": "dashboard", "user": user})
