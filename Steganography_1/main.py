import PIL.Image
import io


def encodeText():
    with open('1.jpg', 'ab') as f:
        f.write(b"Hello World")  # encoding byte hello world in img

def decodeText():
    with open('1.jpg', 'rb') as f:
        content = f.read()  # decoding
        offset = content.index(bytes.fromhex('FFD9'))  # searching FFD9 and converting hex to text

        f.seek(offset + 2)
        print(f.read())

def encodePNG():
    img = PIL.Image.open('photo.png')
    byte_arr = io.BytesIO()
    img.save(byte_arr, format='PNG')

    with open('3.jpg','ab') as f:
        f.write(byte_arr.getvalue())

def decodePNG():
    with open('3.jpg','rb') as f:
        content = f.read()  # decoding
        offset = content.index(bytes.fromhex('FFD9'))  # searching FFD9 and converting hex to text
        f.seek(offset + 2)
        dataBytesIO = io.BytesIO(f.read())
        newImg = PIL.Image.open(dataBytesIO)
        newImg.save('result.png')

def encodeEXE():
    with open('4.jpg','ab') as f, open('file.exe','rb') as e:
        f.write(e.read())

def decodeEXE():
    with open('4.jpg','rb') as f:
        content = f.read()  # decoding
        offset = content.index(bytes.fromhex('FFD9'))  # searching FFD9 and converting hex to text
        f.seek(offset + 2)

        with open('newFile.exe','wb') as e:
            e.write(f.read())
