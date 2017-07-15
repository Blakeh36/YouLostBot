import praw
import time
import re

r = praw.Reddit(user_agent='',
                  client_id='',
                  client_secret='',
                  username='',
                  password='')

words = ['i lost','i have lost',"i've lost", ]
unitCust = ['pound','lb','lbs','pounds']
unitMetric = ['kilo', 'kg']
repeats = []

abort = [',']
i = 0
def converterCust(weight):
    galMilk = round(weight / 8.33)
    if galMilk == 1:
        galMilk = str(galMilk)[:5] + " jug of milk"
    else:
        galMilk = str(galMilk)[:5] + " jugs of milk"
    records = round(weight / .2645)
    records = str(records)[:5] + " records"
    babies = round(weight / 7.7)
    if babies == 1:
        babies = str(babies)[:5] + " baby"
    else:
        babies = str(babies)[:5] + " babies"
    mugs = round(weight / .875)
    mugs = str(mugs)[:5] + " mugs"
    statement = "You lost the equivalent of about " + galMilk + ", " + records + ", " + mugs + ", " + " and " + babies + "!\n\nGreat work!"
    return statement
def converterMetric(weight):
    galMilk = round(weight / 8.33 * 1/0.453592)
    if galMilk == 1:
        galMilk = str(galMilk)[:5] + " jug of milk"
    else:
        galMilk = str(galMilk)[:5] + " jugs of milk"
    records = round(weight / .2645 * 1/0.453592)
    records = str(records)[:5] + " records"
    babies = round(weight / 7.7 * 1/0.453592)
    if babies == 1:
        babies = str(babies)[:5] + " baby"
    else:
        babies = str(babies)[:5] + " babies"
    mugs = round(weight / .875 * 1/0.453592)
    mugs = str(mugs)[:5] + " mugs"
    statement = "You lost the equivalent of about " + galMilk + ", " + records + ", " + mugs + ", " + " and " + babies + "! \n\nGreat work!"
    return statement

def run_bot(x):
    print("Grabbing  subs . . .")
    subreddit = r.subreddit(x)
    comments = subreddit.comments(limit = 3000)
    print("Grabbing comments. . .")
    for comment in comments:
        time.sleep(.01)
        comment_text = comment.body
        isMatch = any(string in comment_text.lower() for string in words)
        if isMatch and comment.id not in repeats:
            print("match found! Comment ID: " + comment.id)


            m = re.search(r'i\s+lost\s*([\d.,]+)', comment_text, re.IGNORECASE) or re.search(r'i\s+have\s+lost\s*([\d.,]+)', comment_text, re.IGNORECASE) or re.search(r"i've\s+lost\s*([\d.,]+)", comment_text, re.IGNORECASE)
            if m:
                if(any(string in comment_text for string in unitCust) and not any(string in comment_text for string in unitMetric) and not any(string in comment_text for string in abort)):
                    comment.reply(converterCust(int(m.group(1))))


                    print("SUCCESSFUL")
                elif(any(string in comment_text for string in unitMetric) and not any(string in comment_text for string in abort)):
                    comment.reply(converterMetric(int(m.group(1))))

                    print("SUCCESSFUL")
            print(comment_text)
            repeats.append(comment.id)

    print("Comments loop finished")



while True:
    print('***fitmeals***')
    run_bot('fitmeals')
    print('***1200isplenty***')
    run_bot('1200isplenty')
    print('***Fitness***')
    run_bot('Fitness')
    print('***bodyweightfitness***')
    run_bot('bodyweightfitness')
    print('***xxfitness***')
    run_bot('xxfitness')
    print('***keto***')
    run_bot('keto')
    print('***progresspics***')
    run_bot('progresspics')
    print('***fitmeals***')
    run_bot('fitmeals')
    print('***lostit***')
    '''run_bot('loseit')'''
    print('***weights***')
    run_bot('Weight')
    print('***caloriecount***')
    run_bot('caloriecount')
    print('***weightwatchers***')
    run_bot('weightwatchers')
    print('***HealthyWeightLoss***')
    run_bot('HealthyWeightLoss')
    print(repeats)
