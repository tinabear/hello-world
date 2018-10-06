FROM python:2.7-alpine
RUN pip install simplejson
COPY hello-world.py /hello-world.py
EXPOSE 80
CMD python /hello-world.py

