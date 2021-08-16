string="""Engineering
Computer Engineering
Civil Engineering
Mechanical Engineering
Electronics Engineering
Electrical Engineering
Doctors
Obstetrics
Gynaecology
Dentistry
Internal Medicines
Paediatrics
General Medicine (MBBS)
Sports
Basketball
Cricket
Hockey
Table Tennis
Badminton
Artists
Photography
Music
Painting
Dancing
Theatre and Film
Writing
Salsa Dancing
Zumba
Classical Dancing
Activism
Social Activism
Political Activism
Animal Welfare
Environment Activism
Lawn Tennis
Fitness
Gym
Running
Cycling
Yoga
Wrestling
Kizomba Dancing
Food and Nutrition
Bollywood
Belly Dancing
Football
Golf
Skating
Blockchain & Cryptocurrency
Travelling
Lawyer
Leisure
Trekking & Hiking
Business
Startup
Code Development
QA & testing
DevOps
Python
Wordpress
Designing
Parenting
UI Designing
Graphic Designing
Meditation
Self Healing
Computer Networking
Party
Cyber Security
Dermatology
Neurology
Ophthalmology
Psychiatry
Toxicology
Baseball
Volleyball
Rugby
Boxing
Motorsports
Cardiology
Orthopaedic
Endocrinology
Oncology
Anesthesia
Gardening
Infertility
Immigration
Makeup Artist
MBA
Human Resource
Finance
Marketing
Leadership
Financial Planning
Management
Containers
Accounts
Physics
Chemistry
Economics
Literature
Chartered Accountant
Linguistic and Languages
English Learning
Spanish Learning
Beer
Marijuana
Real Estate
Emerging Technologies
Data Analytics
Mental Peace
Sketching
Russian Language
German Language
Business Strategy
Wine
Linux
Business Networking
Artificial Intelligence
Game Developing
Internet Of Things
Aeronautical Engineering
Chemical Engineering
Fashion
Flight Attendant
Pilot
Robotic Engineering
Poetry
Philosophy
Architecture
Rowing
Virtual Reality
Biochemistry
Religion
Spirituality
Agriculture
Book Reading
History
Space
Pharmacy
Education
Entrance Exam
Musical Instrument
Lifestyle
Maths
French Language
Student
Chess
Guitar
Tabla
Piano
Violin
Flute
Drum
Saxophone
Cello
Keyboard
Harmonium
Mythology
Market Analysis
LGBT
Class 11
Class 10
Class 12
Teacher
Festival
Beauty
IIT JEE
Archaeology
Civilisation
Astronomy
Cooking
Trading
Movie Watching
Archery
Bowling
Curling
Karate
Weight Lifting
Shooting
Ballet
Kathak
Aerial
Tango
Cancan
Magic
Horse Riding
Self Defence
Swimming
Product Reviews
Massage
Mass media and Journalism
Dating
Database Administrator
Machine Learning
Personal Development
Career Counselling
Gaming
Construction
Urban Planning
Structural Engineering
Transportation Engineering
Geotechnical Engineering
Industrial Automation Engineering
Nanotechnology Engineering
Mechatronics Engineering
Industrial Engineering
Robotics Engineering
Pottery
Politics
Gender Issue
Humanity
DJ
Digital Marketing
Volunteering
Venture Capital
Hotel Management
Adventure
Bungee Jumping
Sky Diving
Ocean Diving
Canoeing
Camping
Inventors
Anthropology
Fine Arts
Freeflying
Scuba Diving
Wind Surfing
Homeless
mountain biking
Music Producers
Performing and visual arts
Operations
Driving
R&D
Evolution
ITI
Affiliate Marketing
Content Marketing
Email Marketing
Pay per Click Advertising
Search Engine Marketing
Social media marketing
ATG_INTERNAL
work
sales
analyst
singer"""

 
#quotes=nltk.word_tokenize(string2) 
import nltk
from nltk.corpus import wordnet
from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer


port=PorterStemmer()
#lst=LancasterStemmer() 
#snb=SnowballStemmer('english') 
word_lem=WordNetLemmatizer() 

#print(snb.stem("Designinternship"))
#print(word_lem.lemmatize("Designinternship"))


string2="Social Media Marketing Internship in Mumbai at Arcot Group (Arcot Media Private Limited)"
strn=string.replace("\n"," ")
string1=strn.split()
string1 = list(dict.fromkeys(string1))
string2=string2.split()
#string1=["visual","design"]
group=[]
for s2 in string2:
    st2=s2.lower()
    #st2=port.stem(st2)
    st2=word_lem.lemmatize(st2)
    for s1 in string1:
        st1=s1.lower()
        # st1=port.stem(st1)
        st1=word_lem.lemmatize(st1)
        # st2=lst.stem(st2)
        # print(st1)
        if  st1 in st2 :
            group.append(st2)
            
            # print(st1,st2)        
            #string2.remove(s2)
            #string1.remove(s1)
mylist = list( dict.fromkeys(group) )
listToStr = ' '.join(map(str,mylist))
print(listToStr)
           
 
# w1=wordnet.synset("car.n.01")
# w2=wordnet.synset("car.n.01")
# print(w1.wup_similarity(w2))
# x1=wordnet.synsets("good")
# x2=wordnet.synsets("bus")
# # print(x1.wup_similarity(x2))
# print(x1)
# print(x2)
# s="not same meaning" 
# # for x1 in w1:
# #     for x2 in w2:
# if x1 and x2:
#     print(x1[0].wup_similarity(x2[0]))
#     print(type(x1[0]))
    
# print(w1)
# print(w2)   


# from nltk.corpus import wordnet

# list1 = ['Compare', 'require']
# list2 = ['choose', 'copy', 'define', 'duplicate', 'find', 'how', 'identify', 'label', 'list', 'listen', 'locate', 'match', 'memorise', 'name', 'observe', 'omit', 'quote', 'read', 'recall', 'recite', 'recognise', 'record', 'relate', 'remember', 'repeat', 'reproduce', 'retell', 'select', 'show', 'spell', 'state', 'tell', 'trace', 'write']
# list1=['banking']
# list2=['manager']
# list = []

# for word1 in list1:
#     for word2 in list2:
#         wordFromList1 = wordnet.synsets(word1)
#         wordFromList2 = wordnet.synsets(word2)
#         if wordFromList1 and wordFromList2: #Thanks to @alexis' note
#             s = wordFromList1[0].wup_similarity(wordFromList2[0])
#             list.append(s)

# print(max(list))






































































































































































































































































































































































































































































































































































































































































































































































