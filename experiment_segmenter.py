import cnnlevelset.segmenter as s
import skimage.io as io


if __name__ == '__main__':
    img = io.imread('data/img/twoObj.bmp')
    s.levelset_segment(img)
