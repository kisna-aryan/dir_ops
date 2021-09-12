import glob, os, torch
import shutil
import tqdm

data = f"K:\\DL_git\\YOLO\\dataset_ADAS\\Udacity_self_driving"

source_jpg = f'{data}\\export\\images\\*.jpg'
source_txt = f'{data}\export\labels'

full_dataset = glob.glob(source_jpg)

train_size = int(0.8 * len(full_dataset))
val_size = len(full_dataset) - train_size
train_dataset, val_dataset = torch.utils.data.random_split(full_dataset, [train_size, val_size])
print(len(train_dataset))
print(len(val_dataset))

train_dir = os.path.join(data, "train")
val_dir = os.path.join(data, "val")

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

for f in tqdm.tqdm(train_dataset):
    shutil.copy(f, train_dir_img)
    filename_txt = os.path.join(source_txt, os.path.splitext(os.path.basename(f))[0] + '.txt')
    shutil.copy(filename_txt, train_dir_txt)

    # print(filename_txt)
    # break

for f in tqdm.tqdm(val_dataset):
    shutil.copy(f, val_dir_img)
    filename_txt = os.path.join(source_txt, os.path.splitext(os.path.basename(f))[0] + '.txt')
    shutil.copy(filename_txt, val_dir_txt)

    # print(filename_txt)
    # break