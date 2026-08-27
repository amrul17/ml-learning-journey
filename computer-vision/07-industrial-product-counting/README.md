# Industrial Product Counting

---

## Business Problem

Manual product counting is prone to human error and can be time-consuming, especially in high-volume production environments. The client wants to automate product counting on a conveyor belt to reduce counting errors and improve production and delivery efficiency.

---

## Objective

- Build an object detection and counting system for products moving on a conveyor belt.
- Compare two object detection architectures and identify the more suitable model for the use case.
- Evaluate model performance and resource requirements.
- Demonstrate the system in real-time using a webcam/video feed.

---

## Dataset

The custom dataset was obtained from Roboflow and consists of **40 images** of the target product.

Testing was also performed using a real-time webcam feed and video files.

The video source used for the training and testing experiment was obtained from a YouTube Shorts video by **@MNTechCrafts**.

### Dataset Characteristics

The current experiment uses a single-camera setup as a proof of concept. For future production deployment, other camera sources would require separate validation, including:

- Machine-mounted cameras
- Robotic cameras
- CCTV cameras

---

## Exploratory Data Analysis (EDA)

### Key Insights

- The difference between the training and testing object ranges had a significant impact on detection performance, especially given the small dataset size.
- The same camera, lighting conditions, and general object setup were used during data collection and testing. This controlled environment can produce good results but does not guarantee generalization to unseen production conditions.
- Object distance, scale, and camera angle are important factors for reliable detection when working with a small dataset.

---

## Preprocessing

- Resized images and corresponding annotations to **256 × 256** and converted them into the required training format.
- Applied data augmentation to increase dataset diversity, while avoiding aggressive color transformations that could significantly alter the product appearance.
- Applied a consistent preprocessing pipeline to webcam, video, and image-folder inference to maintain consistency between training and inference.
- Prepared the input data and inference pipeline so the same trained model could be reused for different video and camera sources.

---

## Modeling

### Architecture Used

- **YOLOv8n** was selected based on previous experiments as the best-performing YOLO variant for this use case.
- **RT-DETR** was included as an alternative architecture for comparison, particularly to evaluate its computational requirements against YOLOv8n.
- Both models were trained and evaluated using the same custom dataset and experimental setup.

---

## Evaluation Metric

The following standard object detection metrics were used:

- Precision
- Recall
- mAP50
- mAP50-95

In addition to detection metrics, the experiment also compared:

- Training time
- GPU memory usage
- Real-time detection and counting performance

---

## Model Result

The following results were obtained from the validation experiment:

| Model | Precision (P) | Recall (R) | mAP50 | mAP50-95 |
| :--- | :---: | :---: | :---: | :---: |
| **YOLOv8n** | **0.988** | **1.000** | **0.995** | **0.995** |
| **RT-DETR** | 0.857 | 0.980 | 0.898 | 0.898 |

### Metric Result

[YOLOv8n](assets/output_yolo.png)

[RT-DETR](assets/output_rtdetr.png)

### Video of the Result

[YOLOv8n Video](assets/output_yolo.gif)

[RT-DETR Video](assets/output_rtdetr.gif)

### Video Experiment: Different Object Range Between Training and Testing

[Range Experiment](assets/experiment.gif)

---

## Key Findings

- The range and scale of objects between the training and testing data had a significant impact on detection performance. This effect was particularly noticeable because of the small dataset size.
- **YOLOv8n outperformed RT-DETR in this experiment across all measured detection metrics.**
- YOLOv8n also required substantially less training time and GPU memory than RT-DETR in this experiment:
  - YOLOv8n: approximately **0.005 hours** for 49 epochs and **0.643 GB** peak GPU memory usage.
  - RT-DETR: approximately **0.037 hours** for 39 epochs and **7.14 GB** peak GPU memory usage.
- Both models successfully detected and counted all **17 products** that passed through the test line.
- The experiment demonstrates that model selection should consider not only detection performance, but also computational resources and deployment requirements.

---

## Business Insight

- YOLOv8n is a strong candidate for production-line product counting because it achieved higher detection metrics while requiring substantially fewer computational resources in this experiment.
- The system successfully counted products during relatively fast movement in the test video, demonstrating potential for conveyor-belt monitoring.
- The detection system could be integrated with production machinery or robotic systems to automate counting and reduce human counting errors.
- For production deployment, additional validation is required using data collected directly from the actual factory environment.

---

## Final Decision

### Recommended Architecture: YOLOv8n

### Reasons

- Achieved higher Precision, Recall, mAP50, and mAP50-95 than RT-DETR in this experiment.
- Successfully detected and counted all **17 products** in the test video.
- Required significantly less GPU memory than RT-DETR.
- Had substantially shorter training time in this experiment.
- Supports real-time webcam and video inference.

---

## Limitations

- The custom dataset is relatively small, containing only **40 images**.
- Training and testing conditions were relatively similar, particularly in terms of camera setup, lighting, and object appearance.
- The model was trained to detect and count only one product class.
- The system has not yet been evaluated across multiple camera angles, distances, lighting conditions, or factory environments.
- The video used for testing was sourced externally and may not fully represent actual production-line conditions.
- Although the system performed well with relatively fast object movement in the test video, more systematic testing with different conveyor speeds is still required.
- The current experiment relies heavily on data augmentation because of the limited dataset size.

---

## Future Improvements

- Expand the custom dataset with more images covering different object distances, angles, backgrounds, and lighting conditions.
- Collect data directly from the actual production environment.
- Extend the model to detect and count multiple product classes.
- Test the system at different conveyor speeds and camera configurations.
- Integrate the counting system with production machinery or robotic systems for automated control.
- Add object tracking and line-crossing logic to improve counting reliability and prevent duplicate counting.

---

## Tech Stack

- ultralytics==8.4.115
- opencv-python==5.0.0.93
- roboflow==1.4.1

---

## What I Learned (1% Improvement)

- Learned angle and range is very important in CV.
- Learned limit for 8Gb vram is 16 batch for training rt-detr.
- Learned how make counter line.
