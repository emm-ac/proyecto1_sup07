FROM tiangolo/uvicorn-gunicorn-fastapi

EXPOSE 80

COPY ./app /app

run pip install pandas