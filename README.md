# emotions_api

Author: [Anush Krishna](github.com/anushkrishnav)
Submitted to : https://thehacktrical-2.devpost.com/

This is a simple API that returns a analysis of the emotions in a veideo
This api supports the prescreenting of our Hactor app
Deployed to Azure using Docker 

## We use the following Technologies 

- Flask 
- OpenCV
- Azure web apps
- Azure Container Registry 
- Docker 
We can provide the Docker image on demand ( but you can always build it from the dockerfile here )

# installation 

- Open a terminal and run the following commands 

```bash
git clone
cd emotions_api
python3 -m venv venv
source venv/bin/activate
docker build -t emotions_api .
docker run -p 5000:5000 emotions_api
```

- Open a browser and go to http://localhost:5000
You should see a message saying "Hello World"

# Usage
Endpoint: /score
Method: POST
JSON Body: 
{
    "link": "mp4 link to the video you want to analyze",
    "user": "user id"
}

# Response
{
    "anger": 0.0,
    "contempt": 0.0,
    "disgust": 0.0,
    "fear": 0.0,
    "happiness": 0.0,
    "neutral": 0.0,
    "sadness": 0.0,
    "surprise": 0.0,
    "user": "user id"
}

Project Submission link: https://devpost.com/software/hactor


