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
* ...
* <del>Deploy Route53 and ELB so we can have prettier URL</del>
* <del>Figure out how to get certs so we can do SSL</del>
* Resolve static file serving issues (understand reverse proxy)
* Resolve Facebook production login issues
* Dockerize the application(s)
* Configure Kubernetes to cluster docker containers
* ...

## Built With

* [Amazon Web Services (AWS)](https://aws.amazon.com/) - Cloud infrastructure
* [Ubuntu 16.04 LTS](http://www.ubuntu.com/cloud/services) - Ubuntu's cloud instance
* [python3.6](https://www.python.org/) - Not to be confused with version 3.7, which does not work with django
* [pip3](https://pip.pypa.io/en/stable/) - Python dependency management
* [django](https://www.djangoproject.com/) - The web framework used
* [Vue.js](https://vuejs.org/) - Frontend JavaScript framework
* [Bulma](https://bulma.io/) - CSS framework based on Flexbox
* [Python Social Auth](https://python-social-auth.readthedocs.io/en/latest/) - Authentication and authorization

## Getting Started

You must provision a unix or linux-like environment. The installation and deployment instructions will assume that you are using an ubuntu machine on AWS to host the application and related web server technologies.

### For Frontend Systems

This part of the documentation assumes that you are working in the `frontend/survey-spa` and wish to install the dependencies for the frontend vue-cli system.

First download node on your Ubuntu system:

```sh
sudo apt-get install nodejs
cd frontend/survey-spa
npm install
```

### For Backend Systems

AWS Ubuntu 16.04 AMIs have `python3` pre-packaged. But you'll need to install pip by running `sudo apt install python3-pip` so we can download other dependencies.

Follow the deployment instructions below:

```sh
python3 pip install virtualenv
sudo apt-get install nginx
sudo service nginx start
```

Check if your webserver is receiving requests (that is go visit the public DNS). You may need to change AWS security groups to allow inbound HTTP and HTTPS traffic.

```sh
sudo service nginx stop
sudo vim /etc/nginx/nginx.conf
```

Modify the first line containing the user name to `user ubuntu ubuntu;`

```sh
cd /home/ubuntu/huarngpa_norc_challenge
python3 virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

These instructions create a virtual environment at the root-level of the project--our project will rely on this convention. Then we activate the virtual environment and install the requirements. Finally, we can run this in production mode by using the bash script:

```sh
cd /home/ubuntu/huarngpa_norc_challenge/backend
./start_gunicorn.sh
```

Or optionally, if working from your local machine you can run:

```sh
cd /home/ubuntu/huarngpa_norc_challenge/backend/surveybackend
python3.6 manage.py runserver
```

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

Explain what these tests test and why

```
Give an example
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
