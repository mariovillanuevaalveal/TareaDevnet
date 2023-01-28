#!/bin/bash
echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY ./tempdir/templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY app.py /home/myapp" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/app.py" >> tempdir/Dockerfile
cd tempdir
docker build -t app . 
docker run -t -d -p 8888:8888 --name mvillanueva app
docker ps -app

