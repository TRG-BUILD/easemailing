# Automatic timed mail reminder for EASE project

## Local installation

```sh
pip install -r requirements.txt
pip install -e .
```

## Security
Senders email and password are not exposed and stored in environmental variables `EMAIL_USER` and `EMAIL_PASS`.

```sh
export EMAIL_USER=user@mail.com
export EMAIL_PASS=strongpassword123
```

## Mailing example in local database and smtp debug server
Turn on smtp debug server:
```sh
./test/debug_server_up.sh
```
Create an `env` folder with local database. Specify following configuration file:
```json
{
    "email_subject": "Projekt EASE - din egen strategi",
    "email_server": "smtp.aau.dk",
    "email_type": "html",
    "email_template": "email_template.html",
    "email_template_dir": "email_templates",
    "email_in_debug_mode": true,
    "survey_db_url": "sqlite:///env/matching_testdb.sqlite3",
    "log_name": "job_log",
    "log_dir": "env"
}
```
_In order to send emails to real smtp servers switch `email_in_debug_mode` to `false`, and remeber to set up `EMAIL_USER`, `EMAIL_PASS`._

Run the job:

```sh
python job.py --config jobcfg.json
```
Check the `env/job_log.csv` for mailing status. Check `smtp.log` generated by `debug_server_up.sh` for the sent email content.



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

## Tests
Tests are rebuilding a database snapshot using `*.sql` files in `test/data` folder, therefore if database fields change tests will still pass. In this case, generate new `*.sql` files for db rebuild and test.

Tests for individual modules can be run with `pytest`
```
pytest -v
```

There is an integration test that is expected to pass if run against the debug server.
```sh
cd test
./debug_server_up.sh
python integration_test.py
```

The test verifies that all mails are sent, and log is filled. In addition, check the `smtp.log` file for the sent email.

Note: test databases can be manuallty re-built from `*.sql` files by for example using `sqlite3` command:
```sh
sqlite3 env/matchig_testdb_real_emails.sqlite3 < test/data/build_matching_testdb_real_emails.sql
```