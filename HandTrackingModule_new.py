import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.8,trackCon=0.5):
        self.mode = mode 
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon 

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,
                                        self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils 

    def findHands(self,img,draw = True):
        # đổi BGR sang RGB do cv2.read() trả về BGR
        # cách 1
        # img[:,:,::-1]
        # cách 2 
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # đổi BGR sang RGB
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self, img, handNo=0, draw=True):
        # xList = []
        # yList = []
        # bbox = []
        # self.lmList = []
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # xList.append(cx)
                # yList.append(cy)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
            # xmin, xmax = min(xList), max(xList)
            # ymin, ymax = min(yList), max(yList)
            # bbox = xmin, ymin, xmax, ymax

            # if draw:
            #     cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
            # (bbox[2] + 20, bbox[3] + 20), (0, 255, 0), 2)
        
        return lmList#, bbox
def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success,img = cap.read()
        img = detector.findHands(img)
        lmList  = detector.findPosition(img)
        if len(lmList) !=0:
            print(lmList[4])


        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)


        cv2.imshow('img',img)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()