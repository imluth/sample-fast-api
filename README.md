#Start the API service

looth@ITDPGHC9DB3:/mnt/e/Projects/FastApi_v1$ uvicorn main:app --reload 
INFO:     Will watch for changes in these directories: ['/mnt/e/Projects/FastApi_v1']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [90] using WatchFiles
INFO:     Started server process [92]
INFO:     Waiting for application startup.
INFO:     Application startup complete.


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