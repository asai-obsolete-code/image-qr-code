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

    import imageio
    im = imageio.imread(picture)
    im = im[:,:,:3]
    im_black = numpy.clip(im,0,100)
    im_white = numpy.clip(im,130,255)
    print(im.shape)
    
    from skimage.color import rgb2gray
    # im = rgb2gray(im)
    print(im.shape)
    
    print(im.min(),im.max())
    # im = (im / 2)
    # print(im.min(),im.max())

    from skimage.transform import resize
    im_black = resize(im_black, tuple(qr.shape)+(3,), preserve_range=True)
    im_white = resize(im_white, tuple(qr.shape)+(3,), preserve_range=True)
    print(im_black.shape)

    imageio.imwrite("black.png", im_black)
    imageio.imwrite("white.png", im_white)

    result = ((1-qr) * im_black) + qr * im_white
    print(result.shape)
    imageio.imwrite(output, result)

import sys
main(*sys.argv[1:])

# test
# main("hellooooooooooooooooooooooooo","lenna.png","out.png")
