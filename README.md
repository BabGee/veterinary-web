
# veterinary web application

**veterinary web** is a web application written in Python 3 and using Django framework.
It allows Veterinary officers to take veterinary related records like artificial insemination, breeding record, calf registration, clinical approach, consultation, death approach, deworming, livestock inventory, pregnancy diagnosis, sick approach and vaccination.
It allows Farmers to keep track of their livestock including their treatment history; they can contact veterinary officers and book appointment.
It allows students to access veterinary related books and resources.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See installing instructions for notes on how to deploy the project on a live system.



### Prerequisites
You will find hereafter what I use to develop and to run the project
* Python 3.9
* Django 3.1
* pipenv (not mandatory but highly recommended)

### Installing
Get a local copy of the project directory by cloning "veterinary_web" from github. `git clone git@github.com:BabGee/veterinary-web.git`
N/B: I used SSH clone

I use pipenv for developing this project so I recommend you to create a virtual environment and activate it, `python -m pipenv shell`  and to install the requirements `python -m pip install -r requirements.txt`.

Then follow these steps:
1. Move to root folder `cd vetWeb/soin`
2. Create a `.env` file in the root folder, provide the required database information  to the `.env` file (.env.example file is provided to help set this information)
3. Create the tables with the django command line `python manage.py makemigrations` then `python manage.py migrate`
4. Create your admin log in credentials `python manage.py createsuperuser`
5. Finally, run the django server `python manage.py runserver `


## Built With

* [Python 3](https://www.python.org/downloads/) - Programming language
* [Django](https://www.djangoproject.com/) - Web framework 


## Versioning
I use exclusively Github

## License

This is an open source project not under any particular license.
However framework, packages and libraries used are on their own licenses. Be aware of this if you intend to use part of this project for your own project.
