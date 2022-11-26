FROM python:2.7-slim


RUN mkdir /app
WORKDIR /app
ADD . /app

# upgrade pip
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# uninstall opencv-python and install opencv-python-headless
RUN pip uninstall -y opencv-python
RUN pip install opencv-python-headless
EXPOSE 8000

CMD gunicorn -w 4 -b :8000 app:app