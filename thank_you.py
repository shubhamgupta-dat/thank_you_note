from __future__ import print_function
import sys
from time import sleep
#from colorama import init, Fore
#init()


def tprint(words,time=0.1):
    for char in words:
        sleep(time)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write('\n')
        
def add_red(string):
    return string

def add_magenta(string):
    return string

def add_green(string):
    return string

THANK_YOU = "   ___     ________             __     __  __            _  __     __     \n  / _ |   /_  __/ /  ___ ____  / /__   \\ \\/ /__  __ __  / |/ /__  / /____ \n / __ |    / / / _ \\/ _ `/ _ \\/  '_/    \\  / _ \\/ // / /    / _ \\/ __/ -_)\n/_/ |_|   /_/ /_//_/\\_,_/_//_/_/\\_\\     /_/\\___/\\_,_/ /_/|_/\\___/\\__/\\__/ \n                                                                          \n"

def add_name_line(long=False):
    if long:
        line_len = 50
    else:
        line_len = 30
    tprint(add_green("-"*line_len),time=0.001)

TIME_PARA = 0.02

TIME_TY = TIME_PARA/10

tprint(add_red(THANK_YOU),time=TIME_PARA/10)

tprint(add_red('='*75),time=TIME_PARA/2)

[tprint(line,time=TIME_PARA) for line in """
I am very thankful to Optum for last wonderful 6 years. 
It has been a privilige to work with so many talented colleagues and teams. 
And today with a heavy heart I am moving on for a new challenge in my career.
I would like to take a moment and thank everyone here who have helped me grow.

""".split('\n')]

tprint(add_magenta("Vineet"),time=TIME_PARA*3)
add_name_line()
tprint("""You have been a compass for me in this team. Fun and Learning never 
stops when you are around. Be it presentation or focusing on customer centric 
products or making a long last impression. I had a blast with you during 
office meetings or at dinner tables. You will be constant source of 
inspiration. I am so happy to work under your amazing leadership. Thank you 
for putting your trust in me. I will keep bothering you for advices in future. 
May be more in Friday's Weekly Connect :)
""",time=TIME_PARA)

tprint(add_magenta("Vamsi"),time=TIME_PARA*3)
add_name_line()
tprint("""I can never be more grateful than I am for giving this stats 
fanatic a chance with team. You have been very motivating and allowed me to 
experiment on my own. This liberty had made me a better developer. You have 
made me more compassionate and more patient towards my work. You softskills
are something everyone should learn and cherish. Thank you for managing me.
""",time=TIME_PARA)

tprint(add_magenta("Sriram"),time=TIME_PARA*3)
add_name_line()
tprint("""Sriram you are master of all trades. You are such a wonderful person
to work with. Your persona makes me feel really humble. It was always joyful 
to have discussion with you over coffee or in meetings or post office. I am
really grateful that I got a chance to work for you. You are truly a gem of
a person and a great leader. Thank you for putting your trust in me.
And I will keep looking for your guidance in future.
""",time=TIME_PARA)


tprint(add_magenta("Nilav aka `Dada`"),time=TIME_PARA*3)
add_name_line()
tprint("""`Dada`, words will be less for me to express gratitude towards you.
Your constant motivation and trust has accelerated my growth. You are the 
catalyst for growth as an engineer. Everytime I had a conversation, I always
felt elevated. There are so many random ideas and discussions we have in backlog
to improve team's performance. I hope team will help you out to complete them.
Thank you for being there.
""",time=TIME_PARA)

tprint(add_magenta("Raghav"),time=TIME_PARA*3)
add_name_line()
tprint("""Raghav, you are a perfectionist and State of the art Developer and Data
Scientist. You and Ravi helped me in learning from my mistakes. Your code for 
Customer Centricity made me realise that how much a good engineering practice is
important for any kind of developer. I wish we could have collaborated on more 
projects and met in person. But rest assured, I still have a pending treat. Woh
mein dekar rahunga. :)
""",time=TIME_PARA)

tprint(add_magenta("""Rajat, Gaurav Kandpal, Sourav, Chandan,
                   Atul, Indranil and Kishore"""),time=TIME_PARA*3)
add_name_line(long=True)
tprint("""I know we did only had one or two projects to collaborate on, but believe
me the learning was exponential. You all have such a warm nature and such great
innovative ideas, sometime I could barely keep up. The environment that you create
for nurturing TDPers or colleagues is commendable. I hope everyone gets amazing 
teammates like you.
""",time=TIME_PARA)

tprint(add_magenta("Harsha, Yeshwanth and Snigdha"),time=TIME_PARA*3)
add_name_line()
tprint("""There are so many conversations I had with you all that I can barely remember.
But in the end, I always had fun. You three are amazing at what you do and I have
been lucky to be in touch with you everyday. You three had been daily driver for 
me at so many places. Definitely, it would have been a bit difficult with out you 
guys.
""",time=TIME_PARA)

tprint(add_magenta("Kartik, Reeti, Anurag Das, Anudeep, Abhiroop, Sudeep, Arunjith "),time=TIME_PARA*3)
add_name_line(long=True)
tprint("""I was fortunate enough to work with you all. And I can claim you all are 
exceptionally talented to work with. With some of you I have spent some time but all of
you are amazingly proactive in your work. And I am glad you are not afraid to make
mistakes, admit and correct them. Keep doing the great work you are doing. You can make
anyone learn.
""",time=TIME_PARA)

tprint(add_magenta("For Other Team Members "),time=TIME_PARA*3)
add_name_line()
tprint("""I know with a lot of you I could spend only a limited amount of time. But all
I have are sweet memories. Like, chatting with all the Santosh in our team is such a
comfort. Learning about progress discussions and asking right questions from Manoj. 
Making silly jokes with Rohan.
""",time=TIME_PARA)

tprint(add_magenta("Phani and Rakesh"),time=TIME_PARA*3)
add_name_line()
tprint("""I can not be more thankful I am for you both. You helped me in making right 
decisions during right time of my career. I could not have ever thought about doors of
possibility with Data Science. You were the pillars of support for me in ACC and were 
always there for me States as well. I am really thankful for all your kind support and
learnings.
""",time=TIME_PARA)

tprint(add_magenta("""My friends, 
Varun, Rajeev, Malay, Sanjay, 
Shraddha, Anjali, Chetan, Shubham A,
Dinesh, Abhijeet, Mohanty
Dhiraj, Mahesh, Satish and Satish"""),time=TIME_PARA*3)
add_name_line(long=True)
tprint("""You all made my daily routine easier. I always had a blast around you all.
And the non-work conversations normalized my working appetite. Thank you for all
`essential` memories. 
""",time=TIME_PARA)


tprint(add_red("""
I was fortunate enough to get in touch with you all. And I am glad all I had were good
memories in the end.

Stay in Touch!

Shubham Gupta,
Ph: +91-91600-41155,
Mail: notify.shubham@gmail.com
LinkedIn: linkedin.com/in/hubhamgupta
"""),time=TIME_PARA*2)

BEST_WISHES = '___  ____ ____ ___    _ _ _ _ ____ _  _ ____ ____ \n|__] |___ [__   |     | | | | [__  |__| |___ [__  \n|__] |___ ___]  |     |_|_| | ___] |  | |___ ___] \n                                                  \n'

tprint(add_red(BEST_WISHES),time=TIME_PARA/10)