from fastapi import HTTPException, status, Request


def check_user(request: Request):
    username = request.cookies.get("username")
    if username is None:
        raise HTTPException(status_code=status.HTTP_307_TEMPORARY_REDIRECT, headers={"Location": "/auth"})
    request.state.username = username


def get_current_user(request: Request):
    username = request.cookies.get("username")
    if username is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return username
