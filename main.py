import numpy

def main(text,picture,output):
    import qrcode
    qr = qrcode.make(text)
    qr = numpy.asarray(qr).astype(float)
    qr.flags.writeable = True
    qr = numpy.expand_dims(qr,3)
    print(type(qr))
    print(qr.shape)
    print(qr.min(),qr.max())
    qr2 = qr / 3
    qr3 = 1- qr

    import imageio
    im = imageio.imread(picture)
    print(im.shape)
    
    from skimage.color import rgb2gray
    # im = rgb2gray(im)
    print(im.shape)
    
    print(im.min(),im.max())
    # im = (im / 2)
    # print(im.min(),im.max())

    from skimage.transform import resize
    im = resize(im, tuple(qr.shape)+(3,), preserve_range=True)
    print(im.shape)

    imageio.imwrite("tmp.png", im)

    result = ((1-qr) * im) + qr*255
    print(result.shape)
    imageio.imwrite(output, result)

import sys
main(*sys.argv[1:])

# test
# main("hellooooooooooooooooooooooooo","lenna.png","out.png")
