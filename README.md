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


## usage
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


## for Windows OS
Python 3.5 이상버전의 설치가 필요합니다. https://www.python.org/ 사이트에서 설치 파일을 다운로드 받고 설치를 합니다.

윈도우 터미널을 실행하고 `pip install exceltp` 또는 `pip3 install exceltp`을 명령 내려 exceltp를 설치합니다.

설정 파일을 생성하거나 수정시`노트패드` 또는 `워드패드`를 사용하면 한글 입력에 대한 문제가 발생할 수 있습니다.

자유로운 한글 입력을 위해서는  [NotePad++](https://notepad-plus-plus.org/) 툴을 설치하여 사용하길 권장합니다.

스크립트를 반복적으로 실행하고 싶다면 윈도우에서 지원하는 "예약 작업" 또는 "작업 스케쥴러"를 활용합니다.
