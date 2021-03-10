from pyzbar import pyzbar
import cv2
import numpy as np

# from skimage import io

class BarcodeManager:

    def camera():
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Test")
        img_counter = 0
        img = ""
        returnmessage = ""
        while img_counter == 0:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            frame = BarcodeManager.processImage(frame)
            cv2.imshow("Test", frame)

            returnmessage = BarcodeManager.decode(frame)
            if (len(returnmessage)>0) :
                img_counter += 1
                

            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                returnmessage='none'
                break
            elif k%256 == 32:
                # SPACE pressed 
                # img_name = "opencv_frame_{}.png".format(img_counter)
                # cv2.imwrite(img_name, frame)
                # print("{} written!".format(img_name))
                img_counter += 1
                returnmessage='none'
        cam.release()
        cv2.destroyAllWindows()
        return returnmessage
    def processImage(image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (1, 21)))
        
        # Stats
        dens = np.sum(image, axis=0)
        mean = np.mean(dens)

        #Threshold
        thresh = image.copy()
        for idx, val in enumerate(dens):
            if val< 10800:
                thresh[:,idx] = 0

        (_, image) = cv2.threshold(thresh, 128, 255, cv2.THRESH_BINARY)

        return image 
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