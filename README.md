# excellent ![Python 3](https://img.shields.io/badge/python-3-blue.svg)

excel third-party python program
* Read excel file and configuration file.
* To classify the matched data in setting conditions.
* Extern integration - notify email

## Install
### Requirements:
* `python` >= 3.5 and `git`
* `openpyxl` : for excel data read
* `pyYAML` : for configuration


download and pip
* git clone https://github.com/[USER]/excellent.git
* pip3 install -r excellent/requirements.txt
* pip3 install -e git+https://github.com/[USER]/excellent.git#egg=excellent


## Usage
```
Usage: excellent -c [file] -f [file]

 -c     yaml style configure file.
 -f     xls or xlsx file.
 -V     show version.

Example:
 excellent -c configure.yml -f target.xlsx
 excellent -V
```

### Configuration
sample
```
config_version: 0.1
analyzer:
    - group_a:
        - test1:
            column_name: f
            column_type: date
            row_startline: 9
            condition: days_ago
            value: 3
    - group_b:
        - test2:
            column_name: f
            column_type: date
            row_startline: 9
            condition: days_later
            value: 5
action:
    type: email
    email_config:
        subject: please read!!
        from: t_account@hotmail.com
        to: to@test.com
        smtp: smtp.live.com:587
        smtp_account: t_account@hotmail.com
        smtp_password : ThisIsPassword
        msg: |
            hello
            expired time ...
            $import_data
            thank you
```
