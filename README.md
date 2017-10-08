# babyshortener
Simple URL shortener implemented using Flask

[![Build Status](https://travis-ci.org/mnowotka/babyshortener.svg?branch=master)](https://travis-ci.org/mnowotka/babyshortener)

Persistence layer provided by SQLAlchemy (`flask_sqlalchemy`). API Resource class provided by `flask-restful`

## How to install?

Run:

```
git clone git@github.com:mnowotka/babyshortener.git
cd babyshortener
pip install .
pip install -r requirements.txt
```

Or:

```
pip install git+https://github.com/mnowotka/babyshortener.git
```

## How to test?

Run:

```
python tests/test_shortener.py
```

## How to run development server?

If installed by cloning `GitHub` repo, add project root directory to `PYTHONPATH` and run:

```
python babyshortener/run_shortener.py
```

If installed via `pip`, the `run_shortener` command should be available

## How to make request using `curl`?

To shorten:

```
curl -H "Content-Type: application/json" -X POST -d '{"url": "www.google.com"}' http://localhost:5000/shorten_url
```

To redirect:

```
curl http://localhost:5000/1VV
```

## How to configure to scale?

1. Provide your own settings file and configure `SQLALCHEMY_DATABASE_URI` to point to the production database

2. Deploy behind gunicorn & NGINX (https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04)

```
export BABYSHORTENER_SETTINGS=/path/to/settings.cfg
gunicorn --bind localhost:8080 --workers 4 'babyshortener.run_shortener:main'

```

3. Deploy on multiple machines behind a load balancer

4. Add a cache layer