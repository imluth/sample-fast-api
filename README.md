# Sample FastAPI application

This demo FastAPI application I have created just to learn how API works and basic python. This API service will include endpoint "http://127.0.0.1:8000/random" which will send back a random numbers between 1 to 100.


## Installation

Use the docker compose to run it.

```bash
docker compose up --build
```

## Output

```
$ docker compose up --build
[+] Building 11.2s (11/11) FINISHED                                                                                                                            docker:desktop-linux
 => [web internal] load build definition from Dockerfile                                                                                                                       0.0s
 => => transferring dockerfile: 163B                                                                                                                                           0.0s
 => [web internal] load metadata for docker.io/library/python:3.8.10-slim                                                                                                      2.2s
 => [web auth] library/python:pull token for registry-1.docker.io                                                                                                              0.0s
 => [web internal] load .dockerignore                                                                                                                                          0.0s
 => => transferring context: 71B                                                                                                                                               0.0s
 => [web 1/4] FROM docker.io/library/python:3.8.10-slim@sha256:6c0b171f6e4cbd880a972a36b77f18ccb03c3f32a6385e3306e289e9ddbfbcfe                                                0.0s
 => [web internal] load build context                                                                                                                                          0.1s
 => => transferring context: 278.32kB                                                                                                                                          0.1s
 => CACHED [web 2/4] WORKDIR /app                                                                                                                                              0.0s
 => [web 3/4] COPY . /app                                                                                                                                                      0.1s
 => [web 4/4] RUN pip install -r requirements.txt                                                                                                                              8.6s
 => [web] exporting to image                                                                                                                                                   0.1s
 => => exporting layers                                                                                                                                                        0.1s
 => => writing image sha256:88bb2f8a3d2ca5f5e0da730632228fc6e103e9eaab6490660ac660ae191695d9                                                                                   0.0s
 => => naming to docker.io/library/fastapi_v1-web                                                                                                                              0.0s
 => [web] resolving provenance for metadata file                                                                                                                               0.0s 
[+] Running 1/0                                                                                                                                                                     
 ✔ Container fastapi_v1-web-1  Recreated                                                                                                                                       0.0s 
Attaching to web-1
web-1  | INFO:     Will watch for changes in these directories: ['/app']
web-1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
web-1  | INFO:     Started reloader process [1] using StatReload
web-1  | INFO:     Started server process [8]
web-1  | INFO:     Waiting for application startup.
web-1  | INFO:     Application startup complete.
web-1  | INFO:     192.168.65.1:22796 - "GET / HTTP/1.1" 200 OK
web-1  | INFO:     192.168.65.1:57472 - "GET / HTTP/1.1" 200 OK
web-1  | INFO:     192.168.65.1:57472 - "GET / HTTP/1.1" 200 OK
web-1  | INFO:     192.168.65.1:57472 - "GET /random HTTP/1.1" 200 OK
```

## Usage

Send request to API.

http://127.0.0.1:8000/random

```bash
{
"number": 45,
"limit": 100
}
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Currently not under any license.
