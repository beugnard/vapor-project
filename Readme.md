# Vapor Project
## AB

## Summary

Vapor project doing nothing, but it do right.

```
curl http://127.0.0.1:5000/sumit?a=1&b=2
3
curl http://127.0.0.1:5000
There is nothing here
```


## Tests

```
export PYTHONPATH=.
python setup.py test
```


## Running

Install requirements before running Vapor

```
pip install -r requirements.txt
export FLASK_APP=vapor
flask run
```
