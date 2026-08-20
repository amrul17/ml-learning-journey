import cv2
from collections import Counter
from ultralytics import YOLO



MODEL_PATH = r'D:/Amr/Portfolio/All time project/ready to publish/CV/Project 3/runs/mlflow/654454162695301159/df65671d894a4dfeba460a73146bb811/artifacts/weights/best.pt'
VIDEO_SOURCE = 0   
CONF_THRES = 0.5
PREVIEW_PATH = "output.jpg"

model = YOLO(MODEL_PATH)
class_names = model.names          # {0: 'poco_f1', 1: 'poco_f7'}

total_counts = Counter()           # sum of detections across all frames
frame_idx = 0
preview_saved = False

# stream=True keeps memory usage low for video/realtime inference
results = model.predict(source=VIDEO_SOURCE, stream=True, conf=CONF_THRES)

for r in results:
    frame_idx += 1

    # count detections in this frame
    labels = [class_names[int(c)] for c in r.boxes.cls]
    total_counts.update(labels)

    annotated = r.plot()  # frame with boxes drawn

    # save one preview image (first frame that has at least one detection)
    if not preview_saved and len(labels) > 0:
        cv2.imwrite(PREVIEW_PATH, annotated)
        preview_saved = True

    cv2.imshow("Realtime Detection", annotated)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

# Summary
print(f"/nProcessed {frame_idx} frames")
print("Total detections per class:")
for cls, count in total_counts.items():
    print(f"  {cls}: {count}")
print(f"Preview image saved to: {PREVIEW_PATH}")
