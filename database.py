import urllib
import os
import cv2
#cur directory using os.getcwd()
path= "IIT-DATABASE"
cur_dir= os.getcwd()
if not os.path.exists(path):
    os.makedirs(path)
branches=['EE-120','CS-56','ME-147','CE-97','CH-90','AE-58','ED-58','NA-55','MM-50','PH-10','BE-34','BS-35']
for i in branches:
    os.chdir(cur_dir)
    format= '.jpg'
    no_of_students= int(i[3:len(i)])
    branch= i[0:2]
    year= '2014'
    year_code=year[2:4]
    link_format= 'http://photos.iitm.ac.in/byroll.php?roll='
    if not os.path.exists(path+'/'+branch) :
        os.makedirs(path+'/'+branch)
    for i in range(1,no_of_students+1) :
        if i<10:
            roll_np= branch+year_code+'B'+'00'+str(i)
        if i<100 and i>9:
            roll_np= branch+year_code+'B'+'0'+str(i)
        if i>99:
            roll_np= branch+year_code+'B'+str(i)
        filename= roll_np+format
        print filename
        os.chdir(cur_dir+"/"+path+"/"+branch)
        f=open(filename,'wb')
        studentid= link_format+roll_np
        f.write(urllib.urlopen(studentid).read())
        f.close()
        image= cv2.imread(filename,1)
        height, width = image.shape[:2]
        if width==144 and height==180 :
            os.remove(filename)
        else :
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image,roll_np,(int(.24*width),int(0.92875*height)), font, 1,(0,0,0),2,cv2.CV_AA)
            cv2.imwrite(filename,image)


 


