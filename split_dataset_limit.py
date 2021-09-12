import glob, os, torch
import shutil
import tqdm

data = f"/media/kisna/nano_ti_data/DL_git/YOLO/dataset_ADAS/Udacity_self_driving/self_driving_dataset"


train_source_jpg = f'{data}/train/images/*.jpg'
train_source_txt = f'{data}/train/labels'

val_source_jpg = f'{data}/val/images/*.jpg'
val_source_txt = f'{data}/val/labels'


dest_dir = f'/media/kisna/nano_ti_data/DL_git/YOLO/dataset_ADAS/Udacity_self_driving_small'


train_dataset = glob.glob(train_source_jpg)
val_dataset = glob.glob(val_source_jpg)

print(len(train_dataset))
print(len(val_dataset))

train_dir = os.path.join(dest_dir, "train")
val_dir = os.path.join(dest_dir, "val")

train_dir_img = os.path.join(train_dir, "images")
train_dir_txt = os.path.join(train_dir, "labels")

val_dir_img = os.path.join(val_dir, "images")
val_dir_txt = os.path.join(val_dir, "labels")

################ make train directories ###############
if not os.path.exists(train_dir):
    os.makedirs(train_dir)

if not os.path.exists(train_dir_img):
    os.makedirs(train_dir_img)

if not os.path.exists(train_dir_txt):
    os.makedirs(train_dir_txt)

################ make val directories ##################
if not os.path.exists(val_dir):
    os.makedirs(val_dir)

if not os.path.exists(val_dir_img):
    os.makedirs(val_dir_img)

if not os.path.exists(val_dir_txt):
    os.makedirs(val_dir_txt)

################### split train & val ##################

train_images = 18000
val_images = 2000

for f in tqdm.tqdm(train_dataset[1:train_images]):
    shutil.copy(f, train_dir_img)
    filename_txt = os.path.join(train_source_txt, os.path.splitext(os.path.basename(f))[0] + '.txt')
    shutil.copy(filename_txt, train_dir_txt)

    # print(filename_txt)
    # break

for f in tqdm.tqdm(val_dataset[1:val_images]):
    shutil.copy(f, val_dir_img)
    filename_txt = os.path.join(val_source_txt, os.path.splitext(os.path.basename(f))[0] + '.txt')
    shutil.copy(filename_txt, val_dir_txt)

    # print(filename_txt)
    # break