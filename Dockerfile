FROM python:alpine
WORKDIR /app
COPY web .
# Installing and build python module
RUN pip install -r requirements.txt
# Delete build dependencies
EXPOSE 80
ENTRYPOINT ["python","app.py"]
