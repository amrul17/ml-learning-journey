# Industrial Defect Semantic Segmentation with U-Net

---

## Business Problem

Manual visual inspection is slow, inconsistent, and prone to human error, especially at high production volumes. A missed defect can damage customer trust and lead to product returns or complaints, while inconsistent manual grading can make quality control difficult to standardize across production shifts.

The client wants to automatically localize defective areas on products to support more consistent quality inspection and improve overall production efficiency.

---

## Objective

- Build a pixel-wise semantic segmentation model to localize defect regions using a U-Net trained from scratch.
- Implement a proper train/validation split and quantitative evaluation using Dice Score and IoU.
- Run the trained model on a real-time webcam feed and provide batch-processing options for video files and image folders.

---

## Dataset

The custom dataset was obtained from Roboflow (project `defect-segmentation-with-u-net`, COCO segmentation export) and consists of **36 images** with polygon annotations for defect regions.

- COCO polygon annotations were converted into binary masks using `pycocotools`.
- Defect pixels are represented as white (`255`), while the background is represented as black (`0`).
- The dataset was split into **29 training images and 7 validation images (80/20)** using a fixed random seed for reproducibility.
- Because all annotated defect polygons are combined into a single binary mask, this project performs **binary semantic segmentation (defect vs. background)**.

Testing was also performed using a real-time webcam feed, video files, and folders of images.

### Dataset Characteristics

The current experiment uses a single-camera setup as a proof of concept. For future production deployment, other camera sources would require separate validation, including:

- Machine-mounted cameras
- Robotic cameras
- CCTV cameras

---

## Exploratory Data Analysis (EDA)

### Key Insights

- The same camera, lighting conditions, and object setup were used during data collection and testing. This controlled environment can produce reasonable results but does not guarantee generalization to unseen production conditions.
- Defect pixels occupy a relatively small portion of each image compared with the background, creating significant foreground-background class imbalance.
- Polygon annotations allow the model to localize the spatial region of a defect at the pixel level rather than only predicting a bounding box.

---

## Preprocessing

- Resized images and corresponding binary masks to **256 × 256** and converted them into tensors.
- Re-binarized masks after resizing using `mask > 0.5` to prevent soft edge values caused by interpolation.
- Used an **80/20 train-validation split** with `torch.manual_seed(42)` for reproducibility.
- Applied the same resize and tensor preprocessing pipeline to webcam, video, and image-folder inference to maintain consistency between training and inference.

---

## Modeling

### Architecture Used

Segmentation was performed using a custom **U-Net built from scratch in PyTorch**, without a pretrained backbone.

- **Encoder:** Three convolutional blocks with 64 → 128 → 256 channels. Each block consists of two `Conv2d → BatchNorm2d → ReLU` layers followed by max-pooling.
- **Bottleneck:** Convolutional block with 512 channels.
- **Decoder:** Three transposed-convolution upsampling stages with skip connections from the corresponding encoder stages.
- **Output:** A single-channel `1 × 1` convolution producing raw segmentation logits.

### Loss Function

- `BCEWithLogitsLoss` with automatically calculated `pos_weight` to address defect/background class imbalance.
- Dice Loss calculated from the sigmoid output.
- Total loss = **BCE Loss + Dice Loss**.

### Training

- Optimizer: Adam
- Learning Rate: `1e-4`
- Epochs: 50
- Batch Size: 8
- Best-model checkpointing based on validation loss.

Training loss decreased from **2.10 to 1.23**, while the best validation loss reached **1.2326 at epoch 49**.

---

## Evaluation Metric

- **Dice Score:** Measures the overlap between the predicted defect mask and the ground-truth mask.
- **IoU (Intersection over Union):** Measures the intersection between predicted and ground-truth regions relative to their union and provides a stricter overlap measurement than Dice.

---

## Model Result

The following metrics were calculated on **one sampled validation image**:

| Metric Score | |
|---|---:|
| Best Validation Loss (BCE + Dice) | 1.2326 |
| Dice Score | 0.7083 |
| IoU | 0.5484 |

The predicted probability map showed spatial variation across the image, indicating that the model learned non-uniform defect-related representations rather than producing a uniform output.

> **Important:** The Dice and IoU values above were calculated from a single validation image (`val_dataset[0]`), not the entire 7-image validation set. Therefore, they should be treated as an early proof-of-concept result rather than a robust estimate of overall model performance.

### Screenshot of the Result

[U-Net Real-Time Segmentation](assets/output.jpg)

### Video of the Result

[U-Net Real-Time Segmentation](assets/output_video.gif)

---

## Key Findings

- Training and validation loss decreased steadily over 50 epochs, indicating that the model successfully learned a non-trivial segmentation task.
- On the sampled validation image, the model achieved a Dice Score of approximately **0.71** and an IoU of approximately **0.55**, indicating that the defect region was generally localized but the predicted boundaries were only moderately precise.
- Training stability improved after introducing **BatchNorm**, `BCEWithLogitsLoss` with `pos_weight`, Dice Loss, and best-validation-loss checkpointing.
- The results demonstrate that a small U-Net trained from scratch can learn meaningful defect segmentation, although the current dataset is too small to support strong generalization claims.

---

## Business Insight

- At an IoU of approximately **0.55** on the sampled validation image, the predicted mask shows moderate overlap with the true defect region. For automated quality inspection, this means the model is currently better suited to flagging products for human review than to making fully automated accept/reject decisions. Both false positives and false negatives matter: false positives can cause good products to be rejected, while false negatives can allow defective products to pass inspection.
- The current results demonstrate the potential of pixel-level defect localization, but the small dataset and single-image evaluation mean that the model is not yet ready for production deployment.
- Camera quality, lighting, object positioning, and background conditions should be controlled or represented in the training data to improve robustness.
- The real-time inference pipeline can automatically capture frames when a defect is detected, providing a potential foundation for defect logging and downstream quality-control systems.

---

## Final Decision

### Recommended Architecture: U-Net

### Reasons

- Successfully learned pixel-level defect localization from a small custom dataset.
- Achieved a Dice Score of **0.7083** and IoU of **0.5484** on the sampled validation image.
- Supports real-time webcam inference as a proof of concept.
- The architecture provides a practical foundation for further improvements using data augmentation and pretrained encoders.

> **Decision:** The model is promising for further experimentation but requires a larger and more diverse dataset and full validation-set evaluation before production deployment.

---

## Limitations

- The dataset contains only **36 images**, with 29 used for training and 7 for validation.
- Dice and IoU were calculated on only **one validation image**, so the reported scores may not represent overall model performance.
- The model was trained and tested under similar camera, lighting, and object conditions and has not been evaluated across diverse environments.
- The binary mask combines all defect annotations into a single class, so the model cannot distinguish between different defect types or separate individual defect instances.
- The U-Net was trained from scratch without a pretrained encoder, which can be challenging with such a small dataset.
- No data augmentation was applied in the current training pipeline.
- The model has not yet been validated under high-speed production conditions.

---

## Future Improvements

- Calculate Dice and IoU across the entire validation set and introduce a separate held-out test set.
- Add data augmentation such as rotation, blur, brightness, and saturation changes.
- Experiment with a pretrained encoder, such as ResNet, to improve feature extraction with limited training data.
- Expand the dataset with more defect examples and greater variation in backgrounds, lighting, camera angles, and object positions.
- Extend the binary segmentation task to multi-class segmentation if different defect types need to be identified separately.
- Evaluate inference speed and latency under realistic production conditions.
- Test the model with fast-moving and overlapping objects.
- Add object counting and line-crossing logic for moving production-line applications.

---

## Tech Stack

- matplotlib==3.11.1
- numpy==2.5.2
- opencv_python==5.0.0.93
- Pillow==12.3.0
- pycocotools==2.0.11
- roboflow==1.4.1
- torch==2.6.0+cu124
- torchvision==0.21.0+cu124

---

## What I Learned (1% Improvement)

- Learned how to handle severe foreground-background class imbalance using `pos_weight` with `BCEWithLogitsLoss` and Dice Loss.
- Learned how BatchNorm can improve training stability in a U-Net trained from scratch.
- Learned how to convert polygon annotations into binary segmentation masks using `pycocotools`.
- Learned how Dice Score and IoU evaluate pixel-level segmentation performance.
- Learned the importance of evaluating models on unseen data rather than relying only on training loss.
- Learned that a small and controlled dataset can produce promising results while still having limited generalization to real-world conditions.