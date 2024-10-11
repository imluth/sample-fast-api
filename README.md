# Start the API service
% uvicorn main:app --reload


# Verify if API serice is running
Open http://127.0.0.1:8000/ on browser

{
"example": "This is example",
"data": 999
}

Also can access FastApi Docs page from http://127.0.0.1:8000/docs


# Send request to API

http://127.0.0.1:8000/random

{
"number": 45,
"limit": 100
}


# Use below command to run the docker container
docker compose up --build
