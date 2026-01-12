FROM python:3.11-slim

WORKDIR /app

COPY requirements/ ./requirements/
RUN pip install --no-cache-dir -r requirements/prod.txt

COPY . . 

CMD ["uvicorn","src.main:app","--host","0.0.0.0","--port","8000","--reload"]
