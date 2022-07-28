# lorem-ipsum-ecommerce
An E-commerce website with both guest user and signed in user's functionalities like add to cart, check cart, add/remove items, checkout and make payment(still under construction).
![image](https://user-images.githubusercontent.com/83615173/151954597-4b0281ea-54a4-460d-9821-fdf97b50ff1c.png)
The webapp is deployed on heroku which is not supporting media files, the actual website looks like this with all the images!

## Set-Up
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/fatimareefat/lorem-ipsum-ecommerce.git
$ cd lorem-ipsum-ecommerce
```

Create a virtual environment to install dependencies in and activate it:

```sh
	virtualenv env -p python3
	source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh

(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
