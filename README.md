# Automatic timed mail reminder for EASE project

## Local installation

```sh
pip install -r requirements.txt
pip isntall -e .

```

## Running tests

```sh
pytest -v
```

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
- create logger with tags
 timestamp [EMAIL_FAIL][EMAIL_SUCCESS] with recipient_id, reminder [DB_FAIL]


## Creating templates
Currently 2 types of templates are tested: HTML template and plane text template. A special substring that follows a tag rule is searhed in those templates in order to substitute the content of survey situations, responses and additional text.

The default tags are:
```python
situation_tag: str = "situation_{}"
response_tag: str = "response_{}"
additional_tag: str = "additional_{}"
```
Where bracket represents an integer starting from 0

### Correct tag rules for HTML template
For the html files the element ids `id=situation_0` are searched with a tag rule for and the corresponding container text (`dummy` in this case) is substituted with the appropriate content of `SurveyResult` object.
```html
<table>
    <tbody>
        <tr>
            <td>&nbsp;<b>Hvis jeg bliver fristet til/kommer til at køre for hurtigt...</b></td>
            <td><b>Så vil jeg minde mig selv om...</b></td>
        </tr>
        <tr>
        <td id="situation_0">&nbsp;dummy</td>
        <td id="response_0">dummy </td>
        </tr>
        <tr>
        <td id="situation_1">&nbsp;dummy</td>
        <td id="response_1">dummy </td>
        </tr>
        <tr>
        <td id="situation_2">&nbsp;dummy</td>
        <td id="response_2">dummy </td>
        </tr>
    </tbody>
</table>
```
### Correct tag rules for the plane text files
For the plane text files the element prefixed with `$` as `$situation_0` or `${situation_0}` are searched with a tag rule for and substituted with the content of `SurveyResult` object.
```
Hvis jeg bliver fristet til/kommer til at køre for hurtigt...
Så vil jeg minde mig selv om...

| $situation_0 | $response_0 |
| $situation_1 | $response_1 |
| $situation_2 | $response_2 |
```