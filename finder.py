import os
entries = os.listdir('imgs')
entry = os.listdir('masks_filled')
images = []
masks = []
not_present=[]

for i in entries:
    images += [i.split('.')[0]]

for i in entry:
    masks += [i.split('.')[0]]

for i,j in zip(images, masks):
    if i not in masks or j not in images:
        not_present += [i]

# print(not_present)
# for i in range(len(not_present)):
#     os.remove("D:\KJSIEIT\Skin-Lesion-Segmentation-in-TensorFlow-2.0\imgs\\"+not_present[i]+'.jpeg')

for i,j in zip(images,masks):
    print(i,j,int(i)-int(j))