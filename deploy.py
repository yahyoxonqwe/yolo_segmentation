import cv2
from ultralytics import YOLO
from PIL import Image, ImageDraw
import numpy as np

model = YOLO('/home/airi/yolo/runs/segment/train9/weights/best.pt')
cap = cv2.VideoCapture("video.mp4")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    img = Image.fromarray(frame)
    draw = ImageDraw.Draw(img, "RGBA")
    results = model.predict(source=img, stream=True, verbose=False)

    for result in results:
        try:
            masks = result.masks.cpu()
            boxes = result.boxes.cpu().xyxy.numpy().astype(np.int32)
            for mask in range(len(masks)):
                draw.polygon(list(map(lambda x: tuple(x), masks[mask].xy[0].astype(np.int32))), fill=(0,255,0,125))
                draw.rectangle([tuple(boxes[mask][:2]), tuple(boxes[mask][2:])], outline=(255, 0, 0))
                draw.text((boxes[mask][0]+10, boxes[mask][1]+10), "Window", fill=(255, 0, 0))
        except:
            pass
    cv2.imshow("video", np.array(img))
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

