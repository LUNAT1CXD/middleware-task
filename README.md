
# Tech Task Middleware

#### Create a python virtual environment

- for windows
  - `python -m venv venv`

- for linux/mac
  - `python3 -m venv venv`

#### Activate virtual environment

- for windows
  - `venv\Scripts\Activate`

- for linux/mac
  - `source venv/bin/Activate`

#### To install dependancies

- `pip install -r requirements.txt`


#### make `.env` file with this variables

```
TEST_AWS_ACCESS_KEY_ID=
TEST_AWS_SECRET_ACCESS_KEY=
TEST_AWS_BUCKET_NAME=
```


#### run the project 

- `uvicorn app:app --reload`
