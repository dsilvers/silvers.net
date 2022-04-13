# silvers.net Website

## Local development and deployment

```
direnv allow
pip install -r requirements.txt

flask run

zappa status
zappa update
```

That's it... really.

## AWS Setup

```
Cloudfront 
  |        \
  v         > Static files on S3 (/static)
Lambda
  |
  v
Flask
  ```

  Only environment varilable that may need to be set on Lambda is `FLASK_APP=webapp`.

  The rest of the settings live in `zappa_settings.json`.

