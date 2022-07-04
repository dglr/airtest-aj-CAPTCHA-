import cv2
import numpy as np
import sys

# for i in range(1,51):
#	 name = str(i) + "screen.jpg"
#	 img = cv2.imread(name)
#	 img1_background=img[566:748,39:684]
#	 cv2.imwrite("real_background"+str(i)+".jpg",img1_background)


# pic1= "background/real_background42.jpg"
# pic2= "background/real_background50.jpg"
#
# img1 = cv2.imread(pic1)
# img2 = cv2.imread(pic2)
#
# print(img1)
# img1_=img1[0:70,0:]
# img2_=img2[70:,0:]
#
# img=cv2.vconcat([img1_,img2_])
#
animal = ["background/bee.jpg", "background/butterfly.jpg", "background/carrot.jpg", "background/cat.jpg",
          "background/monkey.jpg", "background/squirrel.jpg"]


def isEqual(img1, img2):
    if img1 is not None:
        result = cv2.addWeighted(img1, 1, img2, -1, 0)
        result2 = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
        return result2
    else:
        return None


def getResult(img):
    _max = sys.maxsize
    answer = np.empty_like(img)
    for name in animal:
        img_bg = cv2.imread(name)
        result = isEqual(img, img_bg)
        new_result = normalize(result)
        max = new_result.sum()
        if max < _max:
            answer = new_result
            _max = max
    return answer


def normalize(img):
    shape = img.shape
    new_img = np.zeros_like(img)
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            if img[i, j] > 10:
                new_img[i, j] = 255
    return new_img


def find_lens(img):
    start = False
    zero = False
    line = img.max(axis=0)
    lens = 0
    s_lens = 0
    for i in range(0, len(line)):
        if not start:
            if line[i] > 0 and i < len(line) - 1 and line[i + 1] > 0:
                start = True
            else:
                s_lens += 1

        elif start and not zero:
            if line[i] == 0 and i < len(line) - 1 and line[i + 1] == 0:
                zero = True
            lens += 1
        elif start and zero:
            if line[i] > 0 and i < len(line) - 1 and line[i + 1] > 0:
                return s_lens, lens
            lens += 1

    assert("here is an error, can not find 2 blocks")
    return s_lens, -1

def get_lens(name):
    img = cv2.imread(name)
    result = getResult(img)
    cv2.imshow("answer!", result)
    cv2.waitKey()
    s_lens, lens = find_lens(result)
    return s_lens, lens

# name "data/real_backgroud1.jpg"
name = ""
start_lens, lens = get_lens(name)

