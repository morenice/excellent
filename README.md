# excellent ![Python 3](https://img.shields.io/badge/python-3-blue.svg)

excellent is excel third-party program

![Alt text](/images/excellent.png?raw=true "Sample Xlsx Title")

* Read excel file and configuration file.
* To classify the matched data in setting conditions.
* Extern integration : notify email, slack, ...


**Use it when you want to be notified about expiration dates.**

## Install
### Requirements:
* `python` >= 3.5
* `openpyxl` : for excel data read(not support xls format)
* `pyYAML` : for configuration


### pypi
`pip3 install exceltp`


## Usage
```
excellent is microsoft excel third party program.
compare and analyze the data in the excel file. notifies the user.

Available commands:

 -c yaml style configure file.
 -f xls or xlsx file.
 -V show version.

Usage:
	exceltp.py -c [file] -f [file]
	exceltp.py -V

Example:
 exceltp.py -c config.yml -f sample.xlsx
```

* Warning: not suppport xls format


## Configure

### analyzer
See sample/sample.yaml file

* condition in group processed as 'and' logic operation
* groups processed as 'or' logic operation
* support date column type
* date type condition
 * today_equal
 * toay_range_in
 * toay_range_over


### action
Email Sender
* See sample/sample.yaml file
* type is email
* smpt server and account setting is required
* $import_data keyword of msg setting contains analyzed data
* import_data setting can include the excel column


Slack webhook
* See sample/sample_slack.yaml
* type is slack_webhook
* webhook url setting is required
* $import_data keyword of msg setting contains analyzed data
* import_data setting can include the excel column


## Quick start for Windows OS
### Install
Required python 3.5
* visit https://www.python.org/
* download and install

Install exceltp
* open windows terminal(cmd)
* execute command `pip install exceltp` or `pip3 install exceltp`


### Sample file
![Alt text](/images/sample_xlsx.png?raw=true "Sample Xlsx Title")


### Confiuration
Write configure file

```
config_version: 0.1
analyzer:
    - group_a:
        - test1:
            column_name: f
            column_type: date
            row_startline: 9
            condition: today_equal
            value: -3
    - group_b:
        - test2:
            column_name: f
            column_type: date
            row_startline: 9
            condition: today_equal
            value: -5
action:
    type: email
    email_config:
        subject: Book 구매 확인 메일입니다.
        from: t_account@hotmail.com
        to: to@test.com,to2@test.com
        cc: to3@test.com
        smtp: smtp.live.com:587
        smtp_account: t_account@hotmail.com
        smtp_password : ThisIsPassword
        import_data: [d, e, f]
        msg: |
            안녕하세요. 알림메일입니다.
            아래 내용을 참고하세요.
            $import_data
            감사합니다.
```


### Execute

```
exceltp -c sample/sample.yml -f sample/sample.xlsx
* 'sample/sample.yml' config file
* 'sample/sample.xlsx' excel file
* read config file ...
* prepare analyze and action ...
* validation excel file ...
/usr/local/lib/python3.5/site-packages/openpyxl/reader/worksheet.py:322: UserWarning: Unknown extension is not supported and will be removed
  warn(msg)
* process analyze ...
  process 1/1 sheet name 'MA List'
* do action ...
send: 'mail FROM:<t_account@hotmail.com> size=440\r\n'
reply: b'250 2.1.0 t_account@hotmail.com....Sender OK\r\n'
reply: retcode (250); Msg: b'2.1.0 test@hotmail.com....Sender OK'
.
.
.
```

Will be recevie email that contains analyzed data

### Tips
If you want to periodically analyze files and receive notifications, use Job Scheduling

