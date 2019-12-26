import openpyxl

wb = openpyxl.Workbook() # 임시로 엑셀 파일(워크북 타입 값)을 하나 만들어서 돌려준다

# wb = openpyxl.load_workbook('test.xlsx') # 절대 위치에 있는 엑셀파일 불러오기

sheet = wb.active # 활성화 되어있는 시트를 불러올 수 있다

sheet.title = '첫번째 시트' # 시트 이름 바꾸기

sheet2 = wb.create_sheet('두번째 시트!') # 새로운 시트 생성하기

sheet2.title = '두번째 시트'

sheet3 = wb.create_sheet('세번째 시트')

# 첫번째 시트 적용

sheet['B2'] = '첫번째 시트입니다.' # 엑셀에서 사용하는 행-열 번호를 그대로 사용하여 셀을 조작하는 방식

for i in range(5):
    sheet.cell(row=3+i, column=2).value = 'hello' # 인덱스 값을 이용하여 셀의 값을 조작하는 방식

sheet.append([1,2,3,4,5]) # 마지막 행에 추가하는 방식

# 두번째 시트 적용

sheet2['B2'] = '두번째 시트입니다.'

for i in range(5):
    sheet2.cell(row=3 + i, column=2).value = 'hello'

sheet2.append([1, 2, 3, 4, 5])

# 세번째 시트 적용

sheet3['B2'] = '세번째 시트입니다.'

for i in range(5):
    sheet3.cell(row=3 + i, column=2).value = 'hello'

sheet3.append([1, 2, 3, 4, 5])

wb.save('testWriter.xlsx') # 엑셀파일을 저장한다