# gcCloudDetection
An object orientated python script to detect cloud from the satellite image, provided in Government of Canada's cloud forecast website. The script uses urllib package to download the image from GC website. Then uses OpenCV package to read the value of the 5x5 pixel and produces a percentage value of the cloud over a specific point.

Run the CloudDetection.py to download the image and process it for cloud detection. Image processing is done in ImageProcessing.py script.

The images are saved in \Images folder.
