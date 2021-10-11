# Demo Library App

## Links to Essential Documents

- [Technical Document](../..)

---

## Assumption Made

- I havent added any authentication or authorisation to apis

- Added some commented code to just indicate that what to do for authorisations

- Used django filter or custome filtering operations.

- Added check in-check out operations but we can improve it to have other filters link check in/out dates, books, libraries etc.

- Used Momy scripts with rest test cases to create dmmy objects

- Havent added any type of violations

## Enhancements

- To add authorisation and authentications

- Add max limit for book access

- Change modelling structure to user "django through" modeling structure

- Add additional table to maintain user profile details

## URLs

- `http://127.0.0.1:8001/library/libraries`
- `http://127.0.0.1:8001/library/books`
- `http://127.0.0.1:8001/library/library-activity`
- `http://127.0.0.1:8001/library/library-activity/<user_id>/`
- `http://127.0.0.1:8001/library/library-activity?user_activity=check_out` -`http://127.0.0.1:8001/library/library-activity?user_activity=check_in` -`http://127.0.0.1:8001/library/library-activity/<user_id/?user_activity=check_out` -`http://127.0.0.1:8001/library/library-activity/<user_id/?user_activity=check_in`

--

## API Execution

- One can use python requests for api execeution

```python
    import requests
    requests.GET(url, header)
    requests.POST(url, payload, header)
```

- Curl command can also be used

```
 curl --location --request POST '<URL>' \

--header 'Content-Type: application/json' \
--header 'Cookie: multidb_pin_writes=y' \
--data-raw '<Raw data>'
```

- Using django rest api UI:
  Just run the local server and open urls, it will automatically render Django rest UI to test callbacs

---

## Build Project

- Clone code from my repo

- Create a virtual environment

- navigate to the project folder and run command

```bash
    pip install -r requirements.txt
```

- Run Migrations

```
Python manage.py migrate
```

- Run local server

```
python manage.py runserver
```

- open localserver url in browser.
