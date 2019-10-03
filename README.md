Proposed Project Idea:

**AIsight**

Audience - People with Visual Impairment / Blindness

Problem Statement - How do you help your visually impaired friends see the world? We propose a solution - an Android App which acts as an all-time companion by describing the events happening in your surroundings.

Proposed Solution - How does AIsight work?
AIsight describes the ongoing events captured through camera. This will help visually impaired people know about their surroundings and better equip them with details.


IDEA DESCRIPTION AISIGHT-

AIsight app will work as a virtual companion which will describe blind people what is in front of them.

It acts a person, describing what objects are  in front of them and thereby giving him an idea/warning them of where they are and what is right ahead of them.

Basically it describes a live video or any video for that matter -

For eg.

A blind person is walking on a street, the app accessing the rear camera will process the live video and describe what is going on at that moment in front of him.

Scenario - 1 : On street
Cars are passing by or street is empty or people are walking in his direction, some animal is approaching or is in front of him.....

Scenario - 2 : Inside a building
Stairs in front of him, person is at the door, room is filled with people etc.


Focus of the project:
Real-time Video/Scene Understanding. ( We plan to achieve real time response/ reducing latency) 

kaggle competition link -
https://www.kaggle.com/c/youtube8m-2019

Logical Steps of Proposed solution:

Step 1: When the user scans the surroundings using camera, it is taken as an input.
Step 2: Image Captioning engine will then generate a caption for an image frame of the video after every few frames repeatedly.
Step 3: These multiple captions will be summarized by Text summarization engine.
Step 4: The obtained caption is converted to speech by TextToSpeech Engine.
Step 5: Eventually, it gives you a spoken description of surroundings.	


Tech Stack:

Android
Computer Vision for Image Captioning : Keras, OpenCV
Natural Language Processing for Text Summarization: NLTK, TensorFlow, Gensim
Text-to-speech generator (IBM Watson/GoogleTextToSpeechAPI/Amazon Polly)
