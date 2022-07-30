from http import HTTPStatus

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response

app = FastAPI()


class ContentTypeValidator:
    TYPES = {'json': 'application/json'}

    def __init__(self, request: Request):
        self.content_type = request.headers.get('content-type')

    def validate(self, expected):
        if self.content_type == self.TYPES[expected]:
            return True
        return HTTPStatus.BAD_REQUEST


class Car(BaseModel):
    id: int
    seats: int


@app.get("/status")
async def status():
    return {"status": "OK"}


@app.put('/cars')
async def load_cars(request: Request = None):
    content_type_validation = ContentTypeValidator(request).validate('json')
    if ContentTypeValidator(request).validate('json') != True:
        return Response(status_code=content_type_validation)

    cars = await request.json()
    return {"status": "OK"}
