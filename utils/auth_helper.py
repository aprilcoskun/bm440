from fastapi import HTTPException, status, Request
from db import db_conn, Employee


def check_user(request: Request):
    tc = request.cookies.get("tc")
    if tc is None:
        raise HTTPException(status_code=status.HTTP_307_TEMPORARY_REDIRECT, headers={"Location": "/auth"})
    request.state.tc = tc


def get_current_user(request: Request) -> Employee:
    tc = request.cookies.get("tc")
    if tc is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    if tc == "Admin":
        return Employee(tc="Admin", name="Admin", password="Admin", title="Admin")
    return db_conn.get_employee(tc)
