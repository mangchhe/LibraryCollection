from openpyxl import load_workbook

while True:

    excelFileName = input('엑셀 파일 입력하세요 : ')

    try:
        wb = load_workbook(excelFileName + '.xlsx', data_only= True)
    except FileNotFoundError as err:
        print('맞지 않는 파일 이름')
        continue

    days = input('일차 입력 : ')

    try:
        ws = wb[days + '일차']
    except KeyError as err:
        print('맞지 않는 일차')
        continue

    for row in ws.rows:
        print(type(row[0].value))
        print(row[1].value)