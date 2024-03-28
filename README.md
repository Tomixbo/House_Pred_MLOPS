# House sales : Price Prediction Website (MLOPS)

This is a personnal project : **"Creation of a website for house sales price prediction, using machine learning"**. </br>
In this repository, we can find :
- the notebook file and dataset for the model training and tuning
- Dockerfile and docker-compose file for image creation and containerization
- django application files with website templates
- python scripts for the API client (used to make prediction), and the dashboard (for model evaluation)

## Local Deployment
### Step 01 - Pulling docker image and run container with docker compose :
- docker pull mandatombo/django-pycaret:latest
- docker compose up -d

### Step 01 (alternative) - Building the docker image and run container with docker compose :
- docker build -t mandatombo/django-pycaret:latest .
- docker compose up -d

### Step 02 - Accessing the website :
- verify if all services started successfully :
    * docker compose ps
    * docker <container_name> logs
- tape the url on a navigator to access the website :
    * http://localhost:1236/

## Website previewing



https://github.com/Tomixbo/House_Pred_MLOPS/assets/95044551/5ebe282f-f25b-4674-837e-692758df507b



## Those who contributed to this project
- Ambinintsoa Manda
- Tombo H. ANDRIAMAHATANA
