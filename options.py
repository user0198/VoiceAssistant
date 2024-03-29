# voice commands 
class Options(object):
    
    # dict of voice commands   
    options = {
        "alias": ('гена', 'геннадий', 'юрий', 'юра', 'ген', 'генчик'),
        "remove": ('сколько', 'скажи', 'покажи', 'расскажи', 'произнеси', 'открой'),
        "cmds": {
            "ctime": ('который час', 'сколько времени', 'подскажи время', 'время', 'какое время'),
            "hello": ('привет', 'здравствуй'),
            "bye": ('пока', 'до свидания', 'увидимся'),
            "whatsup": ('как дела', 'как оно'),
            "joke": ('анекдот', 'рассмеши меня', 'пошути', 'скажи что-нибудь смешное'),
            "name": ('как тебя зовут', 'твоё имя', 'назови себя'),
            "fact": ('расскажи что-нибудь интересное', 'интересный факт'),
            "youtube": ('youtube'),
            "google": ('гугл', 'поиск гугл'),
            "thankyou": ('спасибо')
        }
    }
   
    # prints voice commands on screen
    def showOptions(self):
        print(self.options["cmds"].values())