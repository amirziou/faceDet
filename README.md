# Discription
MASK AND DISTANCE DETECTOR WITH JETSON NANO
SEE THE DEMONSTRATION VIDEOS FIRST 
lien des videos: https://mask-and-distanciation-detector.blogspot.com/2021/09/blog-post_15.html


The most essential protections against the spread of the COVID-19 virus are wearing a mask and physical distancing with others. this project aims to distinguish people who do not respect the precautions and sanitary measures.
The main goal is to implement this system in schools, airports, hospitals, companies and any place where the chances of the spread of COVID-19 are relatively high. The data of students or employees will be captured in the system, if a person is detected without mask or the distance between two people is less than one meter; their names with their photo will be sent to a website in live to the authorities so they can take actions.
![1915edb9-98b9-4a8b-9227-acebdb638d55](https://user-images.githubusercontent.com/90786657/133489923-97a969bb-928c-4318-8875-a4e621adcd41.jpg)





![98b963d5-20fa-4c90-84ba-58214502c401](https://user-images.githubusercontent.com/90786657/133483857-32f79dda-0fc3-449a-97e0-4533d4ec517a.jpg)



Iam using here NVIDIA jetson nano 4GB version B01 (2GB will work same) with raspberry pi camera v2 (raspberry pi camera v1 do not work with jetson nano!) and a wifi adapter (you can use any other wifi source like ethernet); 
And Iam using my jetson with a monitor, keyboard and mouse (the code must work with headless mode too)


![79f587a9-452d-4e39-8360-3f3cdbdb71d6](https://user-images.githubusercontent.com/90786657/133485544-7612a092-a029-4346-bbd9-899b03f3b456.jpg)





1.First you have to install libraries on python found on 'libraries'

2.You have to creat a folder of known persons (that you will recognize if detected not wearing mask), and rename each photo with the name of the person. Then go to 'trainSave.py' and run the code on python (you will find some explenation with the code)

3.Then you will be ready to run the whole code (you can find it on 'pythonCode.py')



Any questions leave them on comments and I will be glad to answer you.
