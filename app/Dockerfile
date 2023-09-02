FROM python:slim
ADD requirements.txt .
ADD main.py .
RUN pip install -r requirements.txt
CMD flask --app main run --host=0.0.0.0