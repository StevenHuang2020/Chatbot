#chatbot
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer 
  
def createBot():
    # Give a name to the chatbot
    chatbot=ChatBot('Steven bot')
    
    # Create a new trainer for the chatbot 
    trainer = ChatterBotCorpusTrainer(chatbot) 
    
    # Now let us train our bot with multipple corpus 
    trainer.train("chatterbot.corpus.english.greetings", 
                "chatterbot.corpus.english.conversations")
    return  chatbot

def getResponse(bot,text):
    return bot.get_response(text)

def main():
    chatbot = createBot()
    print(getResponse(chatbot,'Hello')) 
    print(getResponse(chatbot,'who are you?')) 
    
if __name__=='__main__':
    main()