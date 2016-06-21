'''1.2.2 Whatsapp Visualisation Module - Quick analysis!'''

import whatsapp_parser as wp
import visual as v

def quick():

    print('Welcome to my Whatsapp parser and analysier!\n\n')
    print('Currently this works for android phones only! \n(other phones use a different syntax \nif you could let me know what that is, that would be useful and probably a trivial extension to the parser)\n')
    
    path=raw_input('Please type in the path of the text file containing your whatsapp messages\n')
    
    first=raw_input('What comes first day or month: type day if day/month/year and month if otherway round\n')
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
        
    

    




