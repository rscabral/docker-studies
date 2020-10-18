FROM python:3.6
LABEL maintainer 'Rafael Cabral'

# This variable is just to see all messages from python in sync way
ENV PYTHONUNBUFFERED 1
RUN pip install redis==2.10.5

ENTRYPOINT ["/usr/local/bin/python"]
    