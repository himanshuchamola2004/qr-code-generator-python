'''We are making qrcode from the url for that we will use python liabrary qrcode by the help of this we can easily make the qr code'''

import qrcode 
upi_id = "himanshuchamola663@oksbi"
url =input("Enter the URL: ")
filename = input("Filename you want to save it as: ")
if not filename.endswith(".png"):
    filename = filename +".png"



image = qrcode.make(url)
image.save(filename)

print("QR Code generated successfully")






