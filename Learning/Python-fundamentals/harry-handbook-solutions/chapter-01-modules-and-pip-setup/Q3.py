# #Q3:- install an external module and use it to perform an operation of your interest

# To use pyttsx3, first install it using: pip install pyttsx3
'''ANSWER:-'''

#I have installed the pyttsx3 through pip install pyttsx3 which is an external module to convert text to speech.
import pyttsx3

'''engine= pyttsx3.init()
rate=engine.getProperty('rate') 

# # Function call to getProperty used here.  
# At this stage of learning, I’m exploring functions and will understand them better in upcoming chapters. 

print(rate)
engine.setProperty('rate', 125)
volume=engine.getProperty('volume') # from google 
print(volume) 
engine.setProperty('volume',100)

engine.say("hello how are you")
engine.runAndWait()
engine.say("have a great day")'''

# The following code uses advanced features of pyttsx3 (engine properties and queuing speech).
# I have commented it out for now, as I will study functions and object properties in future chapters.

pyttsx3.speak("see you tomorrow")

#pyttsx3.speak(): uses a separate function to speak the text directly without 
# initializing the engine or setting properties.
