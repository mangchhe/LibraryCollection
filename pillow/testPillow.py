from PIL import Image

img = Image.open('sample.PNG') # 이미지 파일 읽기

print(img.size) # 이미지 크기 GET

img.save('tmp.PNG') # 이미지 파일 저장

im2 = Image.new("RGB", (500,500), (200,200,200)) # 새로운 이미지 생성
im3 = Image.new("RGB", (200,200))                # 디폴트, 검정색

im2.paste(im3, (20,20,220,220)) # 이미지 붙이기

im2.save('tmp2.PNG')

#---------------------------------------------------- 서로 다른 색깔 찾기

image = Image.open('sample.PNG')

im4 = image.load() # 픽셀 값으로 접근하기 위해 필요

width, height = image.size

for i in range(0,width):
    if(im4[i,i] != (255,255,255,255)):
        color = im4[i,i]
        break

print(color)

for i in range(0,width):
    for j in range(0,height):
        if(im4[i,j] != (255,255,255,255) and im4[i,j] != color):
            im4[i,j] = (255-color[0],255-color[1],255-color[2])

image.save('result.png')