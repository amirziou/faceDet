#######################HERE WE SAVE A TRAINING FOR A FOLDER OF IMAGES IN A PICKLE FILE####################

import face_recognition as fc
import cv2
import os
import pickle
print(cv2.__version__)

image_dir= '/home/amir/Desktop/pyPro/FaceRecognizer/demoImages/known'  #copy the path of the folder

Encodings=[]
Names=[] 

for root, dirs, files in os.walk(image_dir):    
    print(files)         
    for file in files:
        path=os.path.join(root,file)
        print(path)
        name=os.path.splitext(file)[0]
        print(name)
        person=fc.load_image_file(path)
        encoding=fc.face_encodings(person)[0]
        Encodings.append(encoding)
        Names.append(name)
print (Names)

with open('train.pkl','wb') as f:    # write this training in a file named train.pkl so i can use this training without compiling every time
    pickle.dump(Names,f)
    pickle.dump(Encodings,f)