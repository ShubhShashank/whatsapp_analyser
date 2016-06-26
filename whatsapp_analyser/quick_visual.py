'''1.2.2 Whatsapp Visualisation Module - Quick analysis!'''

import whatsapp_parser as wp
import visual as v

def quick():

    print('\nWelcome!\n')
    
    path=raw_input('Please type the path of the text file containing your whatsapp messages:\n')
    
    first=raw_input('What is the date format in your whatsapp text file? \nType day if day/month/year and month if month/day/year.\n')
    print('\n\n\n')
    if first=='month':
        f=False
    else:
        f=True
    
    df=wp.what_parse(path,dayfirst=f)
    t=v.visual(df,'hour')
    t.plot()
    t=v.visual(df,'month')
    t.plot_split_year()
    t=v.visual(df,'weekday')
    t.plot()
    t=v.visual(df,'week')
    t.plot()
    t=v.visual(df,'year')
    t.plot_split_year()
        
    

    




