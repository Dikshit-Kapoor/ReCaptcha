from captcha.image import ImageCaptcha
#For generating the image captcha
image=ImageCaptcha()
data=image.generate('DI123')
image.write('DI123','captcha.jpg')


#For generating the audio captcha
from captcha.audio import AudioCaptcha

audio=AudioCaptcha()
data1=audio.generate("1223")
audio.write('1223','1.wav')
