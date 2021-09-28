# Automatic timed mail reminder for EASE project

## Security
Senders email and password are not exposed and stored in environmental variables `EMAIL_USER` and `EMAIL_PASS`.

```sh
export EMAIL_USER=user@mail.com
export EMAIL_PASS=strongpassword123
```

How to organize config to store this and other DB credentials?

## Single mailing example
```sh
./debug_server_up.sh
python mailer.py
```
Check the `smtp.log` file for the sent email

## Mailing example from a local test sqlite3 db
If you have the test db `env/testdb.sqlite3`
```sh
./debug_server_up.sh
python job.py
```
Check the `smtp.log` file for the sent email content

## TODO
- When and how to log to catch unexpected errors in mailing and DB access?