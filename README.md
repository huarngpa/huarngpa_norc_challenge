# NORC Challenge Application (Early Childhood Education)

This is an interview challenge application prepared for the NORC interview team. The focus of this project is to demonstrate technical skill in relevant web technologies (django, Vue.js, etc.). The particular theme for the application is to create a simple, survey web form for the Early Childhood Education research area.

Work with this challenge app is ongoing. See below for achieved and planned delivery objectives:

* <del>Deploy on AWS RDS (databases)</del>
* <del>Demonstrate understanding of django ORM/models</del>
* <del>Demonstrate understanding of django idioms for login/logout</del>
* Demonstrate understanding of MVC pattern and django idioms for it
* Demonstrate understanding of how to use simple Vue.js directives
* ...
* Deploy basic django application on AWS EC2
* <del>Demonstrate Facebook OAuth2 implementation</del>
* Demonstrate understanding of django unit testing
* Demonstrate understanding of django integration testing
* ...
* Demonstrate understanding of how to modify admin template and pages
* ...
* Demonstrate visualization integration with Chart.js or Highchart.js
* Convert from DjangoTemplates to Jinja2 template engine
* Iterate and decouple, make a Node.js + Vue.js SPA frontend
* Demonstrate understanding of SASS/LESS compiled CSS framework
* ...
* Deploy Route53 DNS to have prettier URL
* Dockerize the application(s)
* Configure Kubernetes to cluster docker containers
* ...

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

### Deploying Frontend Systems

### Deploying Backend Systems

On the target (linux) machine, you need to define the following environment variables:

```
export NORC_CHALLENGE_APP_SECRET_KEY="app secret"
export NORC_CHALLENGE_APP_NAME="database name"
export NORC_CHALLENGE_APP_USER="master database user"
export NORC_CHALLENGE_APP_PASS="master database user password"
export NORC_CHALLENGE_APP_HOST="host endpoint of the database"
```

Add additional notes about how to deploy this on a live system

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
