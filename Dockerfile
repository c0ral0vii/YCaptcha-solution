FROM python:3.10.2
COPY . .
WORKDIR .
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "5.8.55.98"]