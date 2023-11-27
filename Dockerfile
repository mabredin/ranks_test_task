FROM python:3.10-slim
WORKDIR /app/src
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./src ./
RUN chmod +x setadmin.sh 
ENTRYPOINT ["python", "manage.py", "migrate", "&&", "./setadmin.sh", "&&", "python", "manage.py", "runserver"]