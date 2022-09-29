# Blog Server

This is a simple blog server that uses a SQLlite database to store blog posts. It is intended to be used with the [blog client](https://github.com/sigltech/My_Portfolio.git).

## Usage

To use this server, you will neet to install pip and pipenv. Then, you can install the dependencies and run the server.

```
pip install pipenv
pipenv install
pipenv run dev
```

You will need to initialize the database if you do not have a database file. To do this, first delete any `.db` files in the `portfolio_blog_server` directory. Then, create a .env file with these lines included:

```
FLASK_APP= portfolio_blog_server
FLASK_ENV=development
PORT=5000
DATABASE_URL='sqlite:///blog-posts.db'
```

***PLEASE NOTE*** 
You **Will** get an error if you do not have a .env file with the above lines. When you run the server with `pipenv run dev`, you will get a warning about using flask_env. It is being deprecated but this is normal and you can safely ignore it. The app will run just fine.

One all that is done, run the following command:

```
pipenv run init_db
```

This will create a database file and populate it with the tables from the models. You can now run the server with `pipenv run dev` and it will be ready to use.

## API endpoints

The server has the following endpoints:

- `GET /posts` - Returns a list of all blog posts
- `GET /posts/<id>` - Returns a single blog post with the given id
- `POST /posts` - Creates a new blog post
- `PUT /posts/<id>` - Updates a blog post with the given id
- `DELETE /posts/<id>` - Deletes a blog post with the given id

While not being used by the client, the server also has the following endpoints:

- `GET /users` - Returns a list of all users
- `POST /register` - Creates a new user
- `POST /login` - Logs in a user



