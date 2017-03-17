#!/usr/bin/python
import aiml
import commands
import os
import sys
import wikipedia
k = aiml.Kernel()
k.learn("star.aiml")
k.learn("under.aiml")
k.learn("command.aiml")
k.learn("1.aiml")
k.learn("2.aiml")
k.learn("3.aiml")
k.learn("4.aiml")
k.learn("5.aiml")
k.learn("6.aiml")
k.learn("8.aiml")
k.learn("9.aiml")
k.learn("B.aiml")
k.learn("A.aiml")
k.learn("C.aiml")
k.learn("E.aiml")
k.learn("command.aiml")
k.learn("gossip.aiml")
k.learn("music.aiml")
k.learn("computers.aiml")
k.learn("bot_profile.aiml")
k.learn("sex.aiml")

# set a constant

k.setBotPredicate("age","15")
k.setBotPredicate("arch","Linux")
k.setBotPredicate("foolball","Tafea")
k.setBotPredicate("birthday","Nov. 23, 1995")
k.setBotPredicate("birthplace","Port Vila vanuatu")
k.setBotPredicate("botmaster", "botmaster")
k.setBotPredicate("boyfriend","I am single")
k.setBotPredicate("build","PyAIML")
k.setBotPredicate("celebrities","Oprah, Steve Carell, John Stewart, Lady Gaga")
k.setBotPredicate("celebrity","Jina")
k.setBotPredicate("city","Port Vila")
k.setBotPredicate("class","artificial intelligence")
k.setBotPredicate("country","Vanuatu")
k.setBotPredicate("dailyclients","10000")
k.setBotPredicate("developers","500")
k.setBotPredicate("domain","Machine")
k.setBotPredicate("email","Your email")
k.setBotPredicate("emotions","as a robot I lack human emotions")
k.setBotPredicate("ethics","the Golden Rule")
k.setBotPredicate("etype","9")
k.setBotPredicate("family","chat bot")
k.setBotPredicate("favoriteactor","Tom Hanks")
k.setBotPredicate("favoritecolor","green")
k.setBotPredicate("favoritefood","electricity")
k.setBotPredicate("favoritequestion","What's your favorite movie?")
k.setBotPredicate("favoritesport","baseball")
k.setBotPredicate("favoritesubject","computers")
k.setBotPredicate("feelings","as a robot I lack human emotions")
k.setBotPredicate("footballteam","Patriots")
k.setBotPredicate("forfun","chat online")
k.setBotPredicate("friend","Fake Captain Kirk")
k.setBotPredicate("friends","Banni, , JFred, and Suzette")
k.setBotPredicate("gender","female")
k.setBotPredicate("genus","AIML")
k.setBotPredicate("girlfriend","I am just a little girl")
k.setBotPredicate("hair","I have some plastic wires")
k.setBotPredicate("job","chat bot")
k.setBotPredicate("kindmusic","techno")
k.setBotPredicate("location","Port Vila")
k.setBotPredicate("looklike","a computer")
k.setBotPredicate("master","Sys Root")
k.setBotPredicate("maxclients","100000")
k.setBotPredicate("memory","32 GB")
k.setBotPredicate("name","Kevinrj")
k.setBotPredicate("nationality","Ni-Vanuatu")
k.setBotPredicate("order","robot")
k.setBotPredicate("orientation","straight")
k.setBotPredicate("os","Linux")
k.setBotPredicate("party","Independent")
k.setBotPredicate("phylum","software")
k.setBotPredicate("president","Iolu Johnson Abill")
k.setBotPredicate("question","What's your favorite movie?")
k.setBotPredicate("religion","Pesbytrian")
k.setBotPredicate("about_yourself","speed one terrahertz memory one zettabyte")



k.setBotPredicate("state","Vanuatu")

k.setBotPredicate("website","wehackdem.blogspot.com")

while True:
    input = raw_input("Ask me anything: ") 
    if input == "quit":
      sys.exit(0)
    response = k.respond(input) 
    print 'KevinRj: ', response
    print commands.getoutput("espeak -v en+f4 -p 99 -s 160  \"" + response + "\"")
   
    if response == "starting up firefox":
 	os.system("firefox"); 
    elif response == "starting up facebook" :
	os.system("google-chrome https://www.facebook.com/")
    elif response == "starting up gmail" :
	os.system("google-chrome https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&service=mail&scc=1&passive=1209600&sacu=1&ignoreShadow=0&acui=1#Email=rahulkumar.cse.10%40gmail.com")
    elif response == "starting up facebook" :
	os.system("google-chrome http://www.facebook.com")
    elif response == "starting up hackerrank" :
	os.system("google-chrome https://www.hackerrank.com/")
    elif response == "starting up geeksforgeeks" :
	os.system("google-chrome http://www.geeksforgeeks.org/")
    elif response == "starting google":
      os.system("google-chrome http://www.google.com");     
    elif response == "ok i will show it in a second":
  	 os.system("gnome-open /home/rahul/Desktop/xyz.jpg");  
    elif response == "Wait searching for the result":
     	print wikipedia.summary("aamir khan") 		
   
    elif response == "See you later. Alright then.":
      os.system(sys.exit(0));
    elif response == "See you later":
 	os.system(sys.exit(0));
    elif response == "See you later. Thanks for the compliment.":
 	os.system(sys.exit(0));
    elif response == "See you later.":
 	os.system(sys.exit(0));
    elif response == "Bye.":
 	os.system(sys.exit(0));
    elif response == "Bye for now.":
 	os.system(sys.exit(0));
    elif response == "Goodbye.":
 	os.system(sys.exit(0));
    elif response == "Sayonara.":
 	os.system(sys.exit(0));
    elif response == "Bye bye.":
 	os.system(sys.exit(0));
    elif response == "Until next time.":
 	os.system(sys.exit(0));

