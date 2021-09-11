import shutil
import glob, os


source_jpg_1 = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Alytus-_Vilnius\\2019-12-20_21.49.15_done_b\\annotations\\*.jpg'
source_txt_1 = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Alytus-_Vilnius\\2019-12-20_21.49.15_done_b\\annotations\\*.txt'

dest_images = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Alytus_8_bit\images'
dest_labels = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Alytus_8_bit\labels'

# ######################11111111111111#############
files_jpg = glob.glob(source_jpg_1)
files_txt = glob.glob(source_txt_1)

print(len(files_jpg))
print(len(files_txt))

for f in files_jpg:
    shutil.copy(f, dest_images)


for f in files_txt:
    shutil.copy(f, dest_labels)
