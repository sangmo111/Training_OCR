# Purpose: Train tesseract for a new font 

Folder structure 

langdata: contains language data for bod from github 

tesstrain: git clone the tesstrain & holds the ground truth output which contains all the training data 
-- data 
------notoground truth

tesseract: clone using the below & make sure to add training file
git clone https://github.com/tesseract-ocr/tesseract.git

get the bod.trained_data file by git cloning tessdata best & then put it inside the tesseract/tessdata folder:
git clone https://github.com/tesseract-ocr/tessdata_best.git

Steps 
1. Run the get_training_text.py to create the data with the new font and the data 

2. Run the following  which will make training from tessdata

TESSDATA_PREFIX=../tesseract/tessdata gmake training MODEL_NAME=Noto_Serif_Tibetan START_MODEL=bod TESSDATA=../tesseract/tessdata MAX_ITERATIONS=100

Make sure 
1. the tessdata contains bod.traineddata
2. run this command in tesstrain folder

gmake clean
gmake training MODEL_NAME=Noto_Serif_Tibetan START_MODEL=bod TESSDATA=../tesseract/tessdata MAX_ITERATIONS=100


Summary: Percent improvement time=100, best error was 100 @ 0
At iteration 100/100/100, mean rms=1.500%, delta=7.183%, BCER train=12.441%, BWER train=36.875%, skip ratio=0.000%, New best BCER = 12.441 wrote best model:data/Noto_Serif_Tibetan/checkpoints/Noto_Serif_Tibetan_12.441_100_100.checkpoint wrote checkpoint.
Finished! Selected model with minimal training error rate (BCER) = 12.441

The training session completed successfully after 100 iterations.
The model’s performance improved, reducing the Character Error Rate (BCER) to 12.441%.
The best model was saved at the end of the training process for future use.

______

After running a 1000 iterations: 
At iteration 995/1000/1000, mean rms=2.356%, delta=16.583%, BCER train=29.964%, BWER train=52.102%, skip ratio=0.000%, New worst BCER = 29.964 wrote checkpoint.
Finished! Selected model with minimal training error rate (BCER) = 9.897

At iteration 495/500/500, mean rms=1.359%, delta=6.184%, BCER train=9.897%, BWER train=27.562%, skip ratio=0.000%, New best BCER = 9.897 Transitioned to stage 1 wrote checkpoint.


___

to check with image 

Use the Tesseract command to run OCR on your new image using the trained model. Here’s how you do it:
tesseract path/to/your/image.tif output_file_name --oem 1 --psm 3 -l Noto_Serif_Tibetan
/Users/jinpa/Desktop

* Replace path/to/your/image.tif with the path to the image you want to process.
* output_file_name is the name of the file where the OCR result will be saved (without the extension).
* The -l Noto_Serif_Tibetan option tells Tesseract to use your trained model.