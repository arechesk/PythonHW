import base64
import requests
import os


def image_compare(source,target):
    with open(source, "rb") as f:
        response = requests.post('https://postman-echo.com/post', files={'image': base64.b64encode(f.read())}).json().\
            get('files').get('image')

    with open(target, "wb") as output:
        output.write(base64.b64decode(response))
        return os.path.getsize(target)


if __name__ == '__main__':
    print(image_compare("./img/lena1.png", "./img/lena2.png"))


