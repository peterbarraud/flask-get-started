# Get started with Flask
## Install Flask
(Got this all from the [Flask Quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart))
1. Go to the command prompt and type `pip install Flask`
1. Create a file named `main.py` (_You can name it whatever you want but I've gone for boring_)
1. For your first (and super basic) `main.py` file, copy-paste the contents from [here](main.basic.py).
1. Now create the Flask app environment variable. In the command prompt: `set FLASK_APP=main.py`.
1. Again, in the command prompt, type: `flask run`

After some commands, you should see this: `Running on http://127.0.0.1:5000/`

If you do, go to the browser and type the link that came above `http://127.0.0.1:5000/`

If you see what you think you should, you're up and about. Else, let me know.

**Lession**: In all of what we've done about, the most important lesson is the way you created your `hello_world` function in the `main.py`.

Above the function is this strange `@app...`. To put it technically, that's a _function decorator_. But to put it simply, that's what we're going to use to create **Web APIs** next


## A little bit more
If you're up and about with Flask, let's do a little bit more than just a very basic (_which, you'll admit, is a bit too basic_).

And for that, we're going to use [this main,py](main.py)

## Serving HTML files
To serve HTML file, we're going to first have to create a folder inside the folder where we've put our `main.py`. And in that folder, let's put an HTML file: [index.html](index1.html).

Go ahead and copy the contents of that file and put it into a file called `index.html` that should be inside the `templates` folder that should be along side the main.py.

Which means we should be looking at a structure like this:

- <`parent folder that's got everything`>
    - `main.py`
    - `templates`
        - `index.html`


Next, copy the contents of the [main.py](main.py) into your `main.py`

Then, run flask again

(_and by the way, every time you make changes to the `main.py`, you're going to have to stop and start flask_)
`flask run`

And go to `http://127.0.0.1:5000/` in your browser. You should be pleasantly suprised :smiley:
