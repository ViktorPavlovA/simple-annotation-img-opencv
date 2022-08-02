from cv2 import cv2
import os

def show_mouse_location(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 255, 0))
        img_view = img
        text = f"x:{x}, y:{y}"
        cv2.putText(img_view, text, (x + 5, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
        cv2.imshow("img_of_something", img_view)
        print(f"location x: {x}, location y: {y}")
        c_x.append(x)
        c_y.append(y)



def add_rectangle(img,c_x,c_y):
    cv2.rectangle(img, (c_x[0], c_y[0]), (c_x[1], c_y[1]), (255, 0, 0), 2)
    return img
def save_img_and_param(*args):
    dir_name = "imges_annotation"
    if not os.path.exists("imges_annotation"):
        os.makedirs("imges_annotation")

    img_resized =args[0]
    img_with_rectangle =args[1]
    cv2.imwrite(dir_name+"/resize_img.jpg",img_resized)
    cv2.imwrite(dir_name + "/img_with_rectangle.jpg", img_with_rectangle)
    c_x = args[2]
    c_y = args[3]
    w = c_x[1] - c_x[0]
    h = c_y[1] - c_y[0]
    write_it = "{},{},{},{},{},{}".format(c_x[0],c_y[0],c_x[1],c_y[1],h,w)
    print(f"size:{w}x{h}")
    with open(r'imges_annotation/annotation.txt',"a+") as file:
        file.write(write_it)
        file.close()



if __name__ == '__main__':
    c_x =[]
    c_y =[]
    link = r"img/1.png"
    img =cv2.imread(link)
    h= 640
    w = 480
    img = cv2.resize(img,(w,h))
    img_resized = img.copy()
    cv2.imshow("img_of_something", img)
    cv2.setMouseCallback("img_of_something", show_mouse_location)
    cv2.waitKey(0)
    print(f"{c_x} \n{c_y}")
    img_with_rectangle = add_rectangle(img,c_x,c_y)
    cv2.imshow("img_of_something", img_with_rectangle)
    cv2.waitKey(0)
    save_img_and_param(img_resized,img_with_rectangle,c_x,c_y)


