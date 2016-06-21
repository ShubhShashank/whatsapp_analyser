'''1.1 Whatsapp Message Parsing Module'''

import csv
import string
import pandas


#conversation parser
def what_parse(messages_file,number_of_participants=0, output_option=2, dayfirst=True):
    '''Parses the whatsapp messages into a user choosen format
    
    Parameters:
    ------------
    
    messages_file : text file
        The messages_file downloaded from whatsapp (either in the form 'filename' or 'filename.txt'). 
        This assumes that this file is located in your working directory
        Also messages are assumed to be of the form:
            date, time - Name_of_sender: Message
            e.g:
            01/06/2015, 22:25 - Name_of_sender: Message
            Use the dayfirst option to change the day/month orderings
    
    number_of_participants : int
        Will check the number of participants in the conversation
        [Default : 0 (no check)]

    output_option : int
        How would you like the output?
            Options:
                1 : create a single csv file with messages in date-time order
                2 : create multiple csv files (one for each of the conversation participants) 
                    with messages in date_time order
            [Default : 2]
        
    dayfirst : True or False
        True : Dates are of the form day/month/year
        False : Dates are of the form month/day/year
        
    '''
    
    #Checking inputs
                    
    if number_of_participants<0:
        assert False, 'Please choose a positive integer or zero number of participants'
    
    if output_option!=1 and output_option!=2:
        assert False, 'Options are:\n1 : display as single csv file with messages in date-time order\n2 : display as multiple csv files (one for each of the conversation participants) \nwith messages in date_time order'
           
    if dayfirst!=True and dayfirst!=False:
        assert False, 'dayfirst options can only be True or False'
        
    #function
        
    whatsapp_to_csv(messages_file)
    df=whatsapp_csv_to_pandas(dayfirst=dayfirst)
    
    if output_option==2:
        csv_splitter(df)
    else: pass
    
    if number_of_participants!=0:
        if number_of_participants!=len(names_of_participants(df)):
            assert False, 'Participants number check failed'
            
    names=names_of_participants(df)
    print('Message parsing is finished\n')
    print('A total of %g messages have been parsed between %g people\n' %(len(df), len(names)))
    print('Names of participants:\n')
    for x in names:
        print('%s'%x)
    
    return df
    
    
    
def whatsapp_to_csv(messages_file):
    '''Turns whatsapp to a csv file called output_ALL
    
     Parameters:
    ------------
    
    messages_file : text file
        The messages_file downloaded from whatsapp (either in the form 'filename' or 'filename.txt'). 
        This assumes that this file is located in your working directory
        Also messages are assumed to be of the form:
            date, time - Name_of_sender: Message
            '''
    
    try : messages=open(messages_file)
    except : 
        try : messages=open(messages_file+'.txt')
        except : print("No such file or directory: '%s'. \n Please make sure it is located in your working directory or make sure the path is correct."\
                        %messages_file)
    
    with open("output_ALL.csv","wb") as output_ALL:
        out_ALL=csv.writer(output_ALL, delimiter=',',quoting=csv.QUOTE_ALL)
        out_ALL.writerow(["Date","Time","Name of Sender","Message"])
        
        l=messages.readline()
        while l:
            if "," and "-" in l:
                try:
                    temp = l.split(",",1)
                    temp2=temp[1].split("-",1)
                    temp3=temp2[1].split(":",1)
                    temp[1]=temp2[0].replace(' ', '')
                    x=temp3[1]
                    temp3[1]= filter(lambda k: k in string.printable, x)
                    temp.append(' '.join(temp3[0].split()))
                    if "\n" in temp3[1]:
                        temp.append(temp3[1].split("\n",1)[0])
                    else:
                        temp.append(temp3[1])
                    if len(temp[0])==10 and len(temp[1])==5:
                        out_ALL.writerow(temp)
                    else: pass
                except:
                    pass
                        
            else: pass
    
                
            l=messages.readline()
        
    output_ALL.close()
    messages.close()
    return 0
    
def whatsapp_csv_to_pandas(output_of_whatsapp_to_csv='output_ALL.csv',dayfirst=True):
    '''Turns our whatsapp csv into a pandas dataframe (format must be as in whatsapp_to_csv)
    
    Parameters:
    ------------
     dayfirst : True or False
        True : Dates are of the form day/month/year
        False : Dates are of the form month/day/year
    '''
    
    df = pandas.read_csv(output_of_whatsapp_to_csv,parse_dates=[['Date','Time']],  dayfirst=dayfirst)
    pandas.to_datetime(df.Date_Time)
    df.index=df.Date_Time
    df2=df.index
    df["Hour"]=df2.hour
    df["Date"]=df2.date
    df["DayofWeek"]=df2.weekday
    df["Week"]=df2.week
    df["Month"]=df2.month
    df["Year"]=df2.year
    return df
        
        
def names_of_participants(pandas_dataframe):
    '''Finds the names of participants: assumes use of function above to create a csv which is in a useful location'''
    df=pandas_dataframe
    return list(df['Name of Sender'].unique())
    
def csv_splitter(pandas_dataframe):
    '''This function creates multiple csvs each containing the messages of a single
        conversation participant'''
    df=pandas_dataframe    
    names=names_of_participants(df)
    for x in names:
        f=df[(df['Name of Sender']==x)]
        with open("output_%s.csv"%x,"wb") as output:
            f=f.drop('Name of Sender', 1)
            f.to_csv(output)
        output.close()
    return 0
            

        
    

    

    
    
        
    
        
        
    
                    
    
        
    
          

   
    
    
    