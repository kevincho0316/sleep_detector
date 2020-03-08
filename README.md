sleep_detector
 ===============
 ### 위 문서들은 조재준에의해 만들어졌으며 인용시 출처를 반드시 밝혀주시기 바랍니다. 
 ### These documents have been made by JaJun-Cho. So if you will use or Quotation you must identify the source
  -------------
# Goal
device based on OpenCV and Dlib that capture that you are sleeping or not
# sleepdetector.py
## LIBRARY
the library that I had used is OpenCV and a Dlib to capture 64 dots on the face
and additionally, there are some of the libraries that don't need for computer vision 
including keyboard,speak_recongizing, and Playsound these only for additional test this the library that can be deleted and modified 
## Math
there is no big deal in the math section you need to just know about EAR
>### __EAR__
>ear is standing for eye aspect ratio 
>EAR uses 6dots for each eye to calculate a relationship between the width and the height of these coordinates.
>you can learn more in the article 
>* article pdf link: <http://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf>

## how to use the desktop or laptop (python3)
The step is simple what you just need to do is install some library (this is based on window platform)
* __CATION__ IF YOU WANT TO FOLLOW THIS STEP YOU SHOULD USE PYTHON 3.5 OR YOU WILL HAVE A PROBLEM INSTALLING DLIB WITH A WHEEL FILE
### pip ###
- Once you’ve confirmed that Python is correctly installed, you can proceed with installing Pip.
- Download get-pip.py to a folder on your computer.
-  * you can download at <https://bootstrap.pypa.io/get-pip.py>
- Open a command prompt and navigate to the folder containing get-pip.py.
- Run the following command on cmd:
```b
python get-pip.py
```


### installing __OPENCV__
- you can install OpenCV with a pip command 
```b
 pip install opencv-python
 ```
### installing Dlib 
- you can follow the youtube video that I found 
- *<https://youtu.be/HqjcqpCNiZg>
### other libraries
- #### keyboard library
- Hook and simulate keyboard events on Windows and Linux
```b
pip install keyboard
```
* More information at the link <https://pypi.org/project/keyboard/>


- #### SpeechRecognition library
- Library for performing speech recognition, with support for several engines and APIs, online and offline.
```
pip install SpeechRecognition
```
* More information at the link <https://pypi.org/project/SpeechRecognition/>


- #### playsound library
- Pure Python, cross-platform, single function module with no dependencies for playing sounds.
```
pip install playsound
```
* More information at the link <https://pypi.org/project/playsound/>

- #### install Scipy
-Scientific Library for Python
```
pip install scipy
```
* More information at the link <https://pypi.org/project/scipy/>

- #### install Imutils
-Flexible utility for displaying images
```
pip install imutils
```
* More information at the link <https://pypi.org/project/imutil/>


## how to use the raspberry pi (python3)
except for dlib and small edit on the code is needed everything will be the same
### library
you can download scipy, imutils, keyboard, playsound, SpeechRecognition in the same way
__BUT OPENCV AND DLIB IS DIFRENT__
#### OpenCV
recently raspberry pi os had had a slight change so many raspberry pi OpenCV installing course 
would not work for you :(
I found a nice blog but it is a Korean language version so you can use a website translator to follow 
the course sorry about that ^^
*web site<https://make.e4ds.com/make/learn_guide_view.asp?idx=116>(made by 주피터)
#### dlib 
you can follow the youtube video but __at the middle of the video he edits the memory split. you should remember your pi's memory split before you edit(mine was 128) I recommend you to write some were__
### slite change for pi
at the middle of the code, there is 

```python3
VideoStream(src=0)
```
you should change value 0 to -1
it would seem like this

```python3
VideoStream(src=-1)
```

___thank you for reading___ 
-Email: <kevincho9029@gmail.com>
```
 _______  _______  _______           _      
(  ____ |(  ____/ (  ___  )| |    /|( |        
| (    ||| (      | (   ) || )   ( || (        
| (_____ | (__    | |   | || |   | || |        
(_____  )|  __)   | |   | || |   | || |        
      ) || (      | |   | || |   | || |        
 _____) || (______| (___) || (___) || (____/|
\_______)(_______/(_______)(_______)(_______/ 
```
