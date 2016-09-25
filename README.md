# excellent ![Python 3](https://img.shields.io/badge/python-3-blue.svg)

excellent is excel third-party program
* Read excel file and configuration file.
* To classify the matched data in setting conditions.
* Extern integration : notify email, slack, ...

## Install
### Requirements:
* `python` >= 3.5
* `openpyxl` : for excel data read(not support xls format)
* `pyYAML` : for configuration


### pypi
`pip3 install exceltp`


## Usage
```
Usage: exceltp -c [file] -f [file]

 -c     yaml style configure file.
 -f     xlsx file.
 -V     show version.

Example:
 exceltp -c config.yml -f data.xlsx
 exceltp -V
```
Warning: not suppport xls format


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
...


## for Windows OS
### 설치
Python 3.5 이상버전의 설치가 필요하다. https://www.python.org/ 사이트에서 설치 파일을 다운로드 받고 설치한다.

윈도우 터미널을 실행하고 `pip install exceltp` 또는 `pip3 install exceltp`을 명령 내려 exceltp를 설치한다.


### 설정 파일
설정 파일을 생성하거나 수정시`노트패드` 또는 `워드패드`를 사용하면 한글 입력에 대한 문제가 발생할 수 있다.

UTF-8 인코딩으로 파일을 저장하거나 [NotePad++](https://notepad-plus-plus.org/) 툴을 설치해서 사용한다.


### 실행

![Alt text](/images/sample_xlsx.png?raw=true "Sample Xlsx Title")



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
        to: to@test.com
        smtp: smtp.live.com:587
        smtp_account: t_account@hotmail.com
        smtp_password : ThisIsPassword
        import_data: [d, e, f]
        msg: |
            안녕하세요. 자동알림입니다.
            확인메일을 보내드립니다. 아래 내용을 참고하세요.
            $import_data
            감사합니다.
```

condition configure
* f열의 날짜 데이터를 조건으로 확인하기 위해 column_name의 값을 f로 column_type을 date로 설정한다.
* 엑셀 시트의 데이터 시작이 9번째 라인부터 시작하기 때문에 row_startline을 9로 설정한다.
* f열의 날짜데이터 값을 비교하여 오늘이 3일전 또는 5일전일 때 참으로 판단하기 위해 2개의 Group을 등록한다.


action configure
* 메일 전송에 사용할 smtp 서버주소와 계정 정보를 작성한다.
* subject와 msg에 전송할 메일의 제목과 내용을 작성한다.
* msg 내용에 $import_data 키워드를 포함시키면 메일 전송시 condition에 일치되는 match data로 변경하여 전송한다.
* import_data는 match data 중에서 필요한 열만 포함시킬 경우 작성한다.


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


### 예약 작업
스크립트를 반복적으로 실행하고 싶다면 윈도우에서 지원하는 "작업 스케쥴러"를 활용한다.

![Alt text](/images/windows_jobsche_run.png?raw=true "Windows Job Scheduling Running")

배치파일을 필요에 맞게 작성하고 해당 파일을 호출하는 작업을 만들어서 사용하는 것을 권장한다.

![Alt text](/images/windows_jobsche_newtask.png?raw=true "Windows Job Scheduling New Task")

