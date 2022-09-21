import layoutparser as lp
import cv2
image = cv2.imread(r'C:\Users\NOY-L\ArmyProject\ocr_constractore\app\tests\data\doc.jpg')
image = image[..., ::-1]
    # Convert the image from BGR (cv2 default loading style)
    # to RGB
model = lp.Detectron2LayoutModel('lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config',
                                 extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8],
                                 label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"})