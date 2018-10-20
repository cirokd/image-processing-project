### Setup local environment

Requirements: basically python3 only, but install anything that pops up while doing these steps

1. Clone this repository
1. Create a virtual environment: `python3 -m venv venv`
1. Activate the virtual environment: `source venv/bin/activate`
1. Install the dependencies: `pip install -r requirements.txt` (if you add new dependencies please run `pip freeze > requirements.txt` to update the dependencies file)
1. Run the application: `python main.py`
1. Deactivate the virtual environment when you finished working with it: `deactivate`

#### Running from the command line

`process_img.py` can be run directly from the command line. In this case the image path is given as a command line argument:
```bash
python process_img.py ./images/sample.png
```
In order to terminate the script (== close all windows opened by OpenCV), press any key while an OpenCV window is focused.

### Image processing resources (update this list when you find something useful):
* [OpenCV documentation](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)
* [Python + OpenCV: OCR Image Segmentation](https://stackoverflow.com/questions/40443988/python-opencv-ocr-image-segmentation)
