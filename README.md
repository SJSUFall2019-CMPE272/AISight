Proposed Project Ideas:

1. Name - AIsight

Audience - People with Visual Impairment / Blindness

Problem Statement - How do you help your visually impaired friends see the world? We propose a solution - an Android App which acts as an all-time companion by describing the events happening in your surroundings.

Proposed Solution - How does AIsight work?
AIsight describes the ongoing events captured through camera. This will help visually impaired people know about their surroundings and better equip them with details.

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

2. ELISA 

Audience: Business

‘ELISA’ – NER based engine for Customer Support and Efficient Processing of Complaints via
1-	Emails

Problem Statement: 
While setting up a business, developing the product and getting people to use it once is usually the easiest part, what’s most important to keep the business running with a decent profit margin, is its customer base and their satisfaction with the products /service. 
Many a times, customers stop using the product, or opt out the service due to poor customer support (assistance, grievance, complaint resolution) which may eventually lead to something as critical as failure of the business.

But we know with so many complaints filling your mailbox on a daily basis, it’s difficult to reach customers to solve their complaints in a short duration.

We bring you a product, to better understand your complaints and redirect them to their resolution departments without support employees reading through them, assigning tickets, forwarding to respective department and then resolving it (i.e. without human assistance and dependence)

Product description: For every complaint mail that you receive, ELISA will identify relevant information like Customer Name, Product related to Complain, Location, Type of Issue and then redirect the complaint details to internal department which should be addressing this for faster resolution.

Proposed solution: How will ELISA do this?

ELISA is equipped with a Named Entity Recognition engine. NER is one task of information extraction which aims to identify details from unstructured data which eventually help us categorize relevant content (emails details in our case). 
Step 1: Fetch mails and input to ELISA,  
Step 2: ELISA will tag details and forward the mail to relevant department. 

Tech Stack:

WebApp: Flask, React, NodeJS
Libraries: NLTK, SpaCy, Stanford NER Tagger

3. Github Savvy

Audience: Developers

Proposed Solution: To enhance the development experience of the techies, the tool will act as a real time assistant to perform all tasks related to Github.

The tool will understand given commands using speech recognition.
And will convert the human language using natural language processing algorithms
Based on the result, it will perform given tasks.
1. It will push the files to the desired git location on the go.
2. It will pull the desired files.
3. It will commit the code the with the given description. The tool can be further enhanced to perform tasks related to data analysis, deployment on different platforms.
Tech Stack:
Speech Recognition: IBM Watson/ Amazon Polly/ GoogleSpeechToText
Natural language Processing: NLTK
Language: Python 


