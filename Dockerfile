FROM python:3.11-alpine3.18

WORKDIR /studentQuiz

COPY ./requirements.txt .

RUN pip install -r requirements.txt 

COPY ./*.py /studentQuiz/
COPY ./*.db /studentQuiz/
COPY ./Dockerfile /studentQuiz/

COPY ./Templates/* /studentQuiz/templates/

EXPOSE 5000
ENV FLASK_APP=main.py

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]