Localization of Django & MySQL Application using Docker (Bonus: PHPMyAdmin)
===========================================================================
[DEMO](screenshot/localization.png)

### Prerequisite
* Ensure that you already installed Docker in your machine. To learn more about installation: [follow this gist](https://gist.github.com/arsho/6249e3f0fc1d966d115c34718e1a8a0a#file-docker_installation_ubuntu_16-04-md)
* Ensure that you already installed Docker Compose in your machine. To learn more about installation: [follow this gist](https://gist.github.com/arsho/6249e3f0fc1d966d115c34718e1a8a0a#file-docker_compose_ubuntu_16-04-md)

### Environment

* <b> Operating System</b> : Ubuntu 16.04 LTS (64-bit)
* <b> Python (Docker)</b> : 2.7 (64-bit)

### Running Django app with MySQL database inside Docker
The following steps showed the step by step guideline. 

#### Create Project Directory

For separating the application from other projects let's first create a directory and move to that:
```
mkdir docker_django_localization
cd docker_django_localization
```

#### Create Dockerfile

Create a `Dockerfile` inside the project directory

#### Create requirements.txt

Create a `requirements.txt` file inside the project directory

#### Create Docker Compose Configuration File

Create a `docker-compose.yml` inside the project directory


#### Build Docker Compose
In this step we are going to build docker compose:
```
docker-compose build
```
The execution of the command will take some time based on internet connection speed.
If you failed to build everything succesfully retry several times as network connection sometimes cause the error.

Check if the instances are running:
```
docker-compose up -d
```
Press `CTRL-C` to stop the instances for now.

Run the project:

```
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose run web python manage.py runserver
```

#### Access the web app

Open [http://0.0.0.0:8000/](http://0.0.0.0:8000/) and see the running web application

#### (Bonus) Access the phpmyadmin

Open [http://0.0.0.0:8082/](http://0.0.0.0:8082/) and see the running `PHPMyAdmin`.
Use 
```
User: root
Password: mypassword
```
and keep the host empty.

#### Referencese

* [Start Django project with Docker](http://mmorejon.github.io/en/blog/start-django-project-with-docker/)
