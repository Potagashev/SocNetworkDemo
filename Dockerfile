FROM python:3.10

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "./SocialNetworkDemo/manage.py", "runserver", "127.0.0.1:8000"]