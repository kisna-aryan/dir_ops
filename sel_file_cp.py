import shutil
import glob, os


source_jpg_1 = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Vilnius\\2019-12-20_22.35.27_done_b\\annotations\\*.jpg'
source_txt_1 = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Vilnius\\2019-12-20_22.35.27_done_b\\annotations\\*.txt'

source_jpg_2 = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Vilnius\\2019-12-20_22.43.45_done_b\\annotations\\*.jpg'
source_txt_2 = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Vilnius\\2019-12-20_22.43.45_done_b\\annotations\\*.txt'

source_jpg_3 = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Vilnius\\2019-12-20_22.53.32_done_b\\annotations\\*.jpg'
source_txt_3 = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Vilnius\\2019-12-20_22.53.32_done_b\\annotations\\*.txt'

source_jpg_4 = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Vilnius\\2019-12-28_15.46.42_done_b\\annotations\\*.jpg'
source_txt_4 = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Vilnius\\2019-12-28_15.46.42_done_b\\annotations\\*.txt'

source_jpg_5 = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Vilnius\\2019-12-28_16.04.15_done_b\\annotations\\*.jpg'
source_txt_5 = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Vilnius\\2019-12-28_16.04.15_done_b\\annotations\\*.txt'


dest_images = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Lithuania_8_bit\images'
dest_labels = f'K:\DL_git\YOLO\dataset_ADAS_thermal\Lithuania\Lithuania_8_bit\labels'

# ######################11111111111111#############
files_jpg = glob.glob(source_jpg_1)
files_txt = glob.glob(source_txt_1)

print(len(files_jpg))
print(len(files_txt))

for f in files_jpg:
    shutil.copy(f, dest_images)


for f in files_txt:
    shutil.copy(f, dest_labels)



# ##########2222222222222##############
files_jpg = glob.glob(source_jpg_2)
files_txt = glob.glob(source_txt_2)

print(len(files_jpg))
print(len(files_txt))

for f in files_jpg:
    shutil.copy(f, dest_images)


for f in files_txt:
    shutil.copy(f, dest_labels)

# #################33333333333333#############
files_jpg = glob.glob(source_jpg_3)
files_txt = glob.glob(source_txt_3)

print(len(files_jpg))
print(len(files_txt))

for f in files_jpg:
    shutil.copy(f, dest_images)


for f in files_txt:
    shutil.copy(f, dest_labels)

# ################44444444444444444###########
files_jpg = glob.glob(source_jpg_4)
files_txt = glob.glob(source_txt_4)

print(len(files_jpg))
print(len(files_txt))

for f in files_jpg:
    shutil.copy(f, dest_images)


for f in files_txt:
    shutil.copy(f, dest_labels)

# ################5555555555555555#############
files_jpg = glob.glob(source_jpg_5)
files_txt = glob.glob(source_txt_5)

print(len(files_jpg))
print(len(files_txt))

for f in files_jpg:
    shutil.copy(f, dest_images)


for f in files_txt:
    shutil.copy(f, dest_labels)