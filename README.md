Whatsapp_analyser
==========

## Dependencies

Python version 2.*

For Python 3.* version: click on [this link](https://github.com/wsqsc735/whatsapp_analyser3)

## Installation

Easy way:  

	pip install whatsapp_analyser

Of course it can be done manually as well if required.

For Python 3.* version: click on [this link](https://github.com/wsqsc735/whatsapp_analyser3)

## How to find whatsapp messages

In your whatsapp app on your phone

* Click on a particular chat
* Click on the three dots
* Click on more
* Click email chat 
* Email to yourself (do not need to attach media files)
* download and place text file into a folder and remember the path
* if you can change the python working directory to the folder containing the text file then you only need to types its name below

##Examples:

Quick use:

	from  whatsapp_analyser import quick_visual as q
	q.quick()
	
More in depth:

	from  whatsapp_analyser import whatsapp_parser as wp
	from  whatsapp_analyser import visual as v
	
	df=wp.what_parse('C:\Users\Username\Documents\Some folder\messages.txt') #replace with your path

It is worth noting that you might need to use two backslashs if you have a file or folder with a command in
it e.g. Some folder\\n.txt  [\n gives new line by itself].
	
	v.visual(df,'month').plot()

Can replace 'month' with many of the pandas index attributes e.g. 'week', 'dayofweek', 'year', 'quarter', 'minute',
'dayofyear'. However, some might get a bit squashed in the graphs!

Finally, there is an alternate plot which splits everything into separate years and then does the plotting:

	v.visual(df,'month').plot_split_year()

This is particually useful when you have over a years worth of messages.


##Modules

#Whatsapp_parser.py:

The main function here is what_parse(args)

	what_parse(messages_file,number_of_participants=0, output_option=2, dayfirst=True)

    '''This Parses the whatsapp messages into a user choosen format
    
    Parameters:
    ------------
    
    messages_file : text file
        The messages_file downloaded from whatsapp (either in the form 'filename' or 'filename.txt'). 
        This assumes that this file is located in your working directory (otherwise need full path)
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

#visual.py

This is for visualising the messages


 Example: 
 
 Let df be a dataframe which has daily events from March 2015 till June 2016 and we want to
 investigate the frequency by month. We note that by ignoring year and just looking at the month
 some months occur twice so this might skew our data
                
 Let 
		  
	t=visual(df,'month')
 Now:
 
    t.counts(False)=([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 12])
    t.counts(True)=([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5], [[3, 12], [1, 5]])
	
 Giving months 3-12 are in the previous year of months 1-5
				
 t also has the attributes:
 
	t.df #Gives the dataframe
	t.attr #picks out the attr from the dataframe in this example it would return a list of the month in
			#which each message was sent
	t.attrstring #returns the attrstring here 'month'
	t.names #the names of the participants of the conversation
	t.years #the years in which messages occor
	t.plot() #Plots a given dataframe attribute
			 #e.g. t=visual(df,'hour').plot()
			 #plots a graph of events the number of events in each hour'''
	t.plot_split_year() #Plots a given dataframe attribute like above but splits into different year
						#Going back to the t=visual(df,'month') example above, if you have more than twelwe months it
						#would probably be sensible to split into different years and not just add everything together which occurs
						#in a given month (however, if you have many years of data then maybe you might prefer not to)'


				





## Licensing

The MIT License (MIT)

Copyright (c) 2016 wsqsc735

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
