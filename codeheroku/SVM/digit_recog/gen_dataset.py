import glob
import cv2
import csv

file_out = open("csv/dataset.csv","a")
writer = csv.writer(file_out)
header=["label"]
for i in range(784):
    header.append("pixel_"+str(i))
writer.writerow(header)

labels = ["0","1","2","3"]

for label in labels:
    dirList= glob.glob("orig_images/"+label+"/*.png")
    for path in dirList:
        #read image using opencv
        img = cv2.imread(path, 0)
        #resize image
        img = cv2.resize(img,(28,28),interpolation=cv2.INTER_AREA)
        cv2.imshow("image",img)

        data = []
        data.append(label)

        row,col=img.shape

        for i in range(row):
            for j in range(col):
                value=img[i,j]
                if value > 100 :
                    value = 1
                else:
                    value = 0
                data.append(value)

        writer.writerow(data)
