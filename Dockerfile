FROM python:3.9
ENV PROJECT_ROOT /project
WORKDIR $PROJECT_ROOT
COPY . $PROJECT_ROOT
RUN pip3 install --no-cache-dir -r requirements.txt