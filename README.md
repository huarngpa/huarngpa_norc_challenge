# NORC Challenge Application (Early Childhood Education)

This is an interview challenge application prepared for the NORC interview team. The focus of this project is to demonstrate technical skill in relevant web technologies (django, Vue.js, etc.). The particular theme for the application is to create a simple, survey web form for the Early Childhood Education research area.

Work with this challenge app is ongoing. See below for achieved and planned delivery objectives:

* <del>Deploy on AWS RDS (databases)</del>
* <del>Demonstrate understanding of django ORM/models</del>
* <del>Demonstrate understanding of django idioms for login/logout</del>
* <del>Demonstrate understanding of MVC pattern and django idioms for it</del>
* <del>Demonstrate understanding of how to use simple Vue.js directives</del>
* ...
* <del>Deploy basic django application on AWS EC2</del>
* <del>Configure deployment scripts and web servers (NGINX and Gunicorn)</del>
* <del>Demonstrate Facebook OAuth2 implementation</del>
* <del>Demonstrate understanding of django unit testing</del>
* Demonstrate understanding of django integration testing
* ...
* Demonstrate understanding of how to modify admin template and pages
* ...
* Demonstrate visualization integration with Chart.js or Highchart.js
* Convert from DjangoTemplates to Jinja2 template engine
* <del>Iterate and decouple, make a Node.js + Vue.js SPA frontend</del>
* <del>Demonstrate understanding of SASS/LESS compiled CSS framework</del>
* <del>Add state management capabilities to the frontend</del>
* <del>Build out make new surveys component feature</del>
* Connect the frontend to the backend by exposing an API
* Demonstrate both the JsonResponse and Rest framework approach
* Add authentication capabilities to the frontend
* Deploy the frontend to AWS infrastructure
* ...
* <del>Deploy Route53 and ELB so we can have prettier URL</del>
* <del>Figure out how to get certs so we can do SSL</del>
* <del>Resolve static file serving issues (understand reverse proxy)</del>
* Resolve Facebook production login issues
* ...
* Get an implementation with windows and Vagrant working
* Dockerize the application(s)
* Configure Kubernetes to cluster docker containers
* ...

## Built With

* [Amazon Web Services (AWS)](https://aws.amazon.com/) - Cloud infrastructure
* [Ubuntu 16.04 LTS](http://www.ubuntu.com/cloud/services) - Ubuntu's cloud instance
* [python3.6](https://www.python.org/) - Not to be confused with version 3.7, which does not work with django
* [pip3](https://pip.pypa.io/en/stable/) - Python dependency management
* [django](https://www.djangoproject.com/) - The web framework used
* [Django REST framework](https://www.django-rest-framework.org/) - Framework for backend API
* [Vue.js](https://vuejs.org/) - Frontend JavaScript framework
* [Vuex](https://vuex.vuejs.org/) - State management pattern and library for Vue.js reactive apps
* [Bulma](https://bulma.io/) - CSS framework based on Flexbox
* [Python Social Auth](https://python-social-auth.readthedocs.io/en/latest/) - Authentication and authorization

## Deployment Documentation

You must provision a unix or linux-like environment. The installation and deployment instructions will assume that you are using an ubuntu machine on AWS to host the application and related web server technologies.

### For Frontend Systems

This part of the documentation assumes that you are working in the `frontend/survey-spa` and wish to install the dependencies for the frontend vue-cli system.

First download node on your Ubuntu system:

```sh
sudo apt-get install nodejs
cd frontend/survey-spa
npm install
npm run dev  # serve with hot reload at localhost:8080
npm run build  # build for production with minification
npm run build --report  # production and bundle analyzer report
```

### For Backend Systems

AWS Ubuntu 16.04 AMIs have `python3` pre-packaged. But you'll need to install pip by running `sudo apt install python3-pip` so we can download other dependencies.

Follow the deployment instructions below:

```sh
sudo apt-get install python3-pip
sudo apt-get install nginx
pip3 install virtualenv
cd /home/ubuntu
git clone https://github.com/huarngpa/huarngpa_norc_challenge.git
```

The instructions above downloads some initial, critical web technologies. We then continue by downloading python requirements.

```sh
cd huarngpa_norc_challenge
python3 -m virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
pip3 install psycopg2
```

Then we'll run commands and scripts to set up the web server and web-server gateway:

```sh
python3 manage.py collectstatic
sudo ufw allow 8000
python manage.py runserver 0.0.0.0:8000
```

At this point, you should go to your ec2 console and change inbound traffic rules to allow 'All traffic' with source 0.0.0.0/0 (temporarily). The goal is to ensure that we are getting a response from the server at port 8000. If successful at this stage, close the runserver command and we'll configure the WSGI server.

```sh
cd /home/ubuntu/huarngpa_norc_challenge/backend/surveybackend
gunicorn --bind 0.0.0.0:8000 surveybackend.wsgi
```

Run the same check on port 8000 to ensure the WSGI is working.

```sh
sudo vim /etc/systemd/system/gunicorn.service
```

Make the following edits to the daemon configuration. Don't use quotes or double quotes in the environment variable configuraitons.

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/huarngpa_norc_challenge/backend/surveybackend
Environment=NORC_CHALLENGE_APP_SECRET_KEY=REPLACE
Environment=NORC_CHALLENGE_APP_NAME=REPLACE
Environment=NORC_CHALLENGE_APP_USER=REPLACE
Environment=NORC_CHALLENGE_APP_PASS=REPLACE
Environment=NORC_CHALLENGE_APP_HOST=REPLACE
Environment=NORC_CHALLENGE_APP_FACEBOOK_KEY=REPLACE
Environment=NORC_CHALLENGE_APP_FACEBOOK_SECRET=REPLACE
ExecStart=/home/ubuntu/huarngpa_norc_challenge/env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/huarngpa_norc_challenge/backend/surveybackend/surveybackend.sock surveybackend.wsgi:application

[Install]
WantedBy=multi-user.target
```

And then start the gunicorn daemon:

```sh
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
```

The status should indicate that the daemon is working correctly and a unix `.sock` file should be created, which we'll use for the web server reverse proxy.

```sh
sudo journalctl -u gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo vim /etc/nginx/sites-available/surveybackend
```

We'll edit the nginx configuration file as follows (use regex to catch all 80 requests to the server, we don't really know how the elb is routing behind the scenes):

```
server {
    listen 80;
    server_name ~^(.+)$;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/huarngpa_norc_challenge/backend/surveybackend;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/huarngpa_norc_challenge/backend/surveybackend/surveybackend.sock;
    }
}

```

Then we can link the nginx configuration files from sites-available to sites-enabled:

```sh
sudo ln -s /etc/nginx/sites-available/surveybackend /etc/nginx/sites-enabled
sudo nginx -t
```

If all goes well the tests should pass and the nginx service will need to be restarted:

```sh
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
```

The commands here clean up the firewall rules and adds rules for the nginx web server. At this point you should clean up the inbound rules for your ec2 instance and only allow ssh (port 22) and http (port 80) traffic.

## Other Deployment Information

### Deploying Frontend Systems

### Deploying Backend Systems

On the target (linux) machine, you need to define the following environment variables:

```
export NORC_CHALLENGE_APP_SECRET_KEY="app secret"
export NORC_CHALLENGE_APP_NAME="database name"
export NORC_CHALLENGE_APP_USER="master database user"
export NORC_CHALLENGE_APP_PASS="master database user password"
export NORC_CHALLENGE_APP_HOST="host endpoint of the database"
export NORC_CHALLENGE_APP_FACEBOOK_KEY="facebook app key"
export NORC_CHALLENGE_APP_FACEBOOK_SECRET="facebook app secret"
```

Add additional notes about how to deploy this on a live system

## Running the tests

Currently this section only contains information on how to run automated testing on the djangopart of the system. But the hope is that as I continue to build out the system I'll find out how to test the Vue.js components (NOTE: ask Ryan about how this is done at NORC).

### JavaScript Testing (Vue.js)

Explain what these tests test and why

```
Give an example
```

### Django Testing

The testing framework in Django allows us to write application-specific unit and integration files in `test.py` files.As an example, see `backend/surveybackend/djangobasic/tests.py` for how tests can be written.

To run these tests, run:

```
python3.6 manage.py test djangobasic
```

## Contributing

Please follow standard github workflows and issue a pull request for contributing to the codebase.

## Versioning

Not available.

## Authors

* **Patrick Huarng** - *Initial work* - [GitHub](https://github.com/huarngpa/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
