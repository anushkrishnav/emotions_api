FROM python:3.10-slim


RUN mkdir /app
WORKDIR /app
ADD . /app
RUN ls 
#create a director for data/videos


# upgrade pip
RUN pip install --upgrade pip
# # RUN apt-get install -y python3-opencv
# RUN apt install libgl1-mesa-glx -y
# RUN apt-get install libgomp1 -y

# RUN apt-get update && apt-get install -y python3-opencv


RUN apt-get update

RUN apt-get update && apt-get install -y --no-install-recommends \
        libsm6\
        libxext6\
        libfontconfig1\
        libxrender1\
        libgl1\
        libglib2.0-0  

# RUN apt-get install -y libsm6 libxext6
# RUN apt-get install -y libfontconfig1 libxrender1
# RUN apt-get install -y libgl1 libglib2.0-0   
RUN pip3 install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000


CMD ["flask", "run", "--host", "0.0.0.0"]
