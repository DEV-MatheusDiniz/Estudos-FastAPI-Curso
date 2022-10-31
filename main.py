from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)



if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)



"""
TOKEN: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjY3ODQzNzU0LCJpYXQiOjE2NjcyMzg5NTQsInN1YiI6IjQifQ.1Nn3mtSuWBWAkdRdRLBj0ISj7Mu8XV0-aba3gucqK2U
TIPO: bearer

TOKEN: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjY3ODQ3NDMwLCJpYXQiOjE2NjcyNDI2MzAsInN1YiI6IjIifQ.y8jvx2jCnrfSf211o3Odt8GLi2ne2rRQA_7poxC9jQY
TIPO: bearer
"""