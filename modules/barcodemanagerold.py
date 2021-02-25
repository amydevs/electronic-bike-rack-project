from pyzbar import pyzbar
import cv2
import numpy as np

# from skimage import io

class BarcodeManager:
    def __init__(initthing):
        self.initthing=initthing

    def camera():
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Test")
        img_counter = 0
        img = ""
        while img_counter == 0:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("Test", frame)

            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed 
                # img_name = "opencv_frame_{}.png".format(img_counter)
                # cv2.imwrite(img_name, frame)
                # print("{} written!".format(img_name))
                img = frame
                img_counter += 1
        cam.release()
        cv2.destroyAllWindows()
        return img
    def decode(image):
    # decodes all barcodes from an image

        # image = cv2.cvtColor(imgimport, cv2.COLOR_RGB2GRAY)
        # _, image_thr = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
        # row_nz = np.count_nonzero(image_thr, axis=0)
        # idx = np.argwhere(row_nz > 100)
        # # Generate new image, draw lines at found indices
        # image_new = np.ones_like(image_thr) * 255
        # image_new[35:175, idx] = 0
        # image = io.imread('https://i1.wp.com/techtutorialsx.com/wp-content/uploads/2020/01/barcode.png?w=788&ssl=1')
        # mask = cv2.inRange(image,(0,0,0),(200,200,200))
        # thresholded = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
        # image = 255-thresholded # black-in-white
        # cv2.imshow('image_thr', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        decoded_objects = pyzbar.decode(image)
        # for obj in decoded_objects:
        #     # draw the barcode
        #     print("detected barcode:", obj)
        #     # image = draw_barcode(obj, image)
        #     # print barcode type & data
        #     print("Type:", obj.type)
        #     print("Data:", obj.data)
        #     print()
        return decoded_objects
    def draw_barcode(decoded, image):
        # n_points = len(decoded.polygon)
        # for i in range(n_points):
        #     image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
        # uncomment above and comment below if you want to draw a polygon and not a rectangle
        image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
            color=(0, 255, 0),
            thickness=5)
        return image