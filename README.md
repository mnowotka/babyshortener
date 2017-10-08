# babyshortener
Simple URL shortener implemented using Flask

[![Build Status](https://travis-ci.org/mnowotka/babyshortener.svg?branch=master)](https://travis-ci.org/mnowotka/babyshortener)

Persistence layer provided by SQLAlchemy (flask_sqlalchemy). API Resource class provided by flask-restful

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

If installed by cloning GitHub repo, add project root directory to PYTHONAPTH and run:

```
python babyshortener/run_shortener.py
```

If installed via pip, the `run_shortener` command should be available

## How to make request using curl?

To shorten:

```
curl -H "Content-Type: application/json" -X POST -d '{"url": "www.google.com"}' http://localhost:5000/shorten_url
```

To redirect:

```
curl http://localhost:5000/1VV
```