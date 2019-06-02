FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /employee-manager
WORKDIR /employee-manager
COPY requirements.txt /employee-manager/
RUN pip install -r requirements.txt
COPY . /employee-manager/
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "localhost:8080"]