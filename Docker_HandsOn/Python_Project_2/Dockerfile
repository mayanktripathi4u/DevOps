FROM python:3.6
LABEL maintainer="Mayank Tripathi <john.doe@example.com>" \
      version="1.0" \
      description="This is an example Docker image"
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "app.py" ]