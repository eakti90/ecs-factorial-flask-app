FROM python:3.8

ENV FLASK_APP app.py

COPY app.py gunicorn-cfg.py requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 80
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "app:app"]
