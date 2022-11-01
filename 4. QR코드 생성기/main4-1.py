import qrcode

qr_data = 'www.naver.com' # 문자열 바인딩
qr_img = qrcode.make(qr_data) 
# qrcode.make로 이미지를 만들어 qr_img 변수에 바인딩

save_path = '4. QR코드 생성기\\' + qr_data + '.png'
qr_img.save(save_path) # 이미지를 저장