FROM jjanzic/docker-python3-opencv
ADD . /python-flask
WORKDIR /python-flask
RUN python3 -m pip install -r requirements.txt
CMD ["python3","app.py"]