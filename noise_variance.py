import os
import cv2
from matplotlib import pyplot

VIDEO = ['A','B','C','D','E']

for video in VIDEO:
    img_filename_list = []
    img_array = []
    ave_array = []
    var_array = []

    img_filename_list = os.listdir(video)
    img_num = len(img_filename_list)

    #Read the Pixel Value
    for img_name in img_filename_list:
        img_path = os.path.join(video, img_name)
        img = cv2.imread(img_path,-1)
        img = img.astype(float)/255
        img_array.append(img)
    
    height = img_array[0].shape[0]
    width = img_array[0].shape[1]

    for j in range(height):
        for k in range(width):
            sum = 0
            var = 0

            #Time Average
            for i in range(img_num):
                sum += img_array[i][j][k]
            ave = sum/img_num
            ave_array.append(ave)
            
            #Noise Variance
            for i in range(img_num):
                var += pow(img_array[i][j][k] - ave,2)
            var = var/img_num
            var_array.append(var)

    #Plot
    #Vertical Axis Range: Automatically Axis
    pyplot.scatter(ave_array,var_array,c="black",marker="+")
    pyplot.ticklabel_format(style='plain')
    pyplot.title(video)
    pyplot.xlim([0.0,1.0])
    pyplot.xlabel("Pixel Value ("+ video +")")
    pyplot.ylabel("Noise Variance ("+ video +")")
    pyplot.savefig(video +"_full range.png")
    pyplot.close()
    #Vertical Axis Range: 0 to 0.0003
    pyplot.scatter(ave_array,var_array,c="black",marker="+")
    pyplot.title(video)
    pyplot.xlim([0.0,1.0])
    pyplot.xlabel("Pixel Value ("+ video +")")
    pyplot.ylim([0,0.0003])
    pyplot.ylabel("Noise Variance ("+ video +")")
    pyplot.savefig(video +".png")
    pyplot.close()

    print(1)
    print(2)

    

