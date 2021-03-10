import pytesseract
import cv2
import numpy as np

# from skimage import io

class OcrManager:

    def camera(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Test", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Test",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        img_counter = 0
        img = ""
        returnmessage = ""
        while img_counter == 0:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            frame = self.processImage(frame)
            cv2.imshow("Test", frame)

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
                returnmessage = self.decode(frame).split('\n')
                img_counter += 1
        cam.release()
        cv2.destroyAllWindows()
        return returnmessage
    def processImage(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
        # image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (1, 21)))
        
        # # Stats
        # dens = np.sum(image, axis=0)
        # mean = np.mean(dens)

        # #Threshold
        # thresh = image.copy()
        # for idx, val in enumerate(dens):
        #     if val< 10800:
        #         thresh[:,idx] = 0

        # (_, image) = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        return image 
    def decode(self, image):
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
        
        custom_config = r'--oem 3 --psm 6 outputbase digits'
        decoded_objects = pytesseract.image_to_string(image, config=custom_config)
        # for obj in decoded_objects:
        #     # draw the barcode
        #     print("detected barcode:", obj)
        #     # image = draw_barcode(obj, image)
        #     # print barcode type & data
        #     print("Type:", obj.type)
        #     print("Data:", obj.data)
        #     print()
        return decoded_objects