<!-- Introduction -->
## Basic Ollama LLM implementation using FastAPI 

This API was created with the idea of having an externally hosted process, that is vital for the functionality of our [product](https://github.com/CristianBabalauCSUM/event-suggestion-ai), that will follow the main principles of being: <br> 

<!-- Unordered List -->
* Robust
* Unremitting
* Reliable
* Power Efficient 

Since we did not want to relly on running our API locally on each testing machine, the final decision was to create a Docker Image, that would later be ran on a VPS, which we achieved. 

To review the functionality of this project, follow this link [195.133.28.162](http://195.133.28.162/)


## Usage

If you want to try and set it up, to check your skills of deploying an API remotely 

Pull the contents of the project

```
mkdir fastAPI_olama
cd fastAPI_olama
git init 
git remote add "origin" https://github.com/CristianBabalauCSUM/event-suggestion-ai.git
git pull
```

And then compose and run the container

```
docker compose up --build
```


### P.S.
The main role of this project was to refresh the knowledge of deploying a FastAPI app externally, using NGINX and Docker



