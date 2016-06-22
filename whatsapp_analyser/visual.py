'''1.2.1 Whatsapp Visualisation Module'''

import numpy as np
import matplotlib.pyplot as plt
import pandas
import whatsapp_parser as wp
    
class visual:
    '''Visualisation class'''
    
    def __init__(self,dataframe,attr):
        
        self.df=dataframe
        self.attrstring=attr
        self.attr=getattr(dataframe.index,attr)
        self.names=wp.names_of_participants(dataframe)
        self.N=len(self.counts()[0])
        self.ind=np.arange(self.N)
        self.width=0.7/len(self.names)
        self.colours=['b','g','r','c','m','y','k']
        self.years=list(dataframe['Year'].unique())
        

    def counts(self,byyear=False):
        '''For a given attribute e.g. hour; it records the unique entries
        
        Parameter
        -----------
        
        byyear : boolean
            byyear=False :finds all the unique elements and then finds the min and max 
                          and returns a list of all elements between the min and max inclusive
                          and the min and max as a separate list
                          
            byyear=True :Much the same as above however, it is split by year (e.g. different years
                        have different mins and maxs
                        
                        
        Example: Let df be a dataframe which has daily events from March 2015 till June 2016 and we want to
                investigate the frequency by month.
                We note that by ignoring year and just looking at the month some months occur twice so this might
                skew our data
                
                Let t=visual(df,'month')
                Now:
                    t.counts(False)=([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 12])
                    t.counts(True)=([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5], [[3, 12], [1, 5]])
                giving months 3-12 are in the previous year of months 1-5

'''
        if byyear==True:
            out=[]
            out2=[]
            for year in self.years:
                dftemp=self.df[(self.df['Year']==year)]
                u=visual(dftemp,self.attrstring)
                t=np.unique(u.attr)
                mint=min(t)
                maxt=max(t)
                out.append(range(mint,maxt+1))
                out2.append([mint,maxt])
            return [i for j in out for i in j],out2
        else:
            t=np.unique(self.attr)
            mint=min(t)
            maxt=max(t)
            return range(mint,maxt+1), [mint, maxt]      

        
    def plot(self):
        '''Plots a given dataframe attribute
        e.g. t=visual(df,'hour').plot()
        plots a graph of events the number of events in each hour'''
        fig, ax = plt.subplots()
        n=0
        ax2=range(len(self.names))
        for x in self.names:
            temp=self.df[(self.df['Name of Sender']==x)]
            tempcount=pandas.value_counts(getattr(temp.index,self.attrstring),sort=False)
            tempplt=np.zeros(self.N)
            for i in self.counts()[0]:
                    try: tempplt[i-min(self.counts()[0])]=tempcount[i]
                    except: tempplt[i-min(self.counts()[0])]=0         
            ax2[n]=ax.bar((self.ind+n*self.width), tempplt, self.width, color=self.colours[n%7])
            n=n+1
        ax.set_ylabel('Total number of messages sent per %s'%self.attrstring)
        ax.set_title('Graph showing number of messages sent on each %s'%self.attrstring)
        ax.set_xticks(self.ind + (len(self.names)/2.0)*self.width)
        ax.set_xticklabels([str(i) for i in self.counts()[0]]) 
        ax.tick_params(axis=u'both', which=u'both',length=0)
        ax.set_xlabel('%s'%self.attrstring.upper())
        ax.legend([ax2[i][0] for i in range(len(self.names))], self.names,fancybox=True).get_frame().set_alpha(0.5)
        plt.plot()
        plt.show()
        
    
    def plot_split_year(self):
        '''Plots a given dataframe attribute like above but splits into different year
        Going back to the t=visual(df,'month') example above, if you have more than twelwe months it
        would probably be sensible to split into different years and not just add everything together which occurs
        in a given month (however, if you have many years of data then maybe you might prefer not to)'''
        fig, ax = plt.subplots()
        n=0
        ax2=range(len(self.names))
        y=0
        extra=0
        labels=[]
        N=len(self.counts(True)[0])
        ind=np.arange(N)
        for x in self.names:
            tempplt=np.zeros(N)
            for year in self.years:
                    dftemp=self.df[(self.df['Year']==year)]
                    temp=dftemp[(dftemp['Name of Sender']==x)]
                    tempcount=pandas.value_counts(getattr(temp.index,self.attrstring),sort=False)
                    j1=self.counts(True)[1][y][0]
                    j2=self.counts(True)[1][y][1]
                    jr=range(j1,j2+1)
                    if self.attrstring=='year':
                        labels=labels+['%g'%i for i in jr]
                    elif N>24:
                        labels=labels+['%g\n%g'%(i,year-2000) for i in jr]
                    else: labels=labels+['%g\n%g'%(i,year) for i in jr]
                    for i in jr:
                            try: tempplt[i-j1+extra]=tempcount[i]
                            except: tempplt[i-j1+extra]=0 
                    y=y+1  
                    extra=extra+len(jr)      
            ax2[n]=ax.bar((ind+n*self.width), tempplt, self.width, color=self.colours[n%7])
            n=n+1
            y=0
            extra=0
        ax.set_ylabel('Total number of messages sent per %s'%self.attrstring)
        ax.set_title('Graph showing number of messages sent on each %s'%self.attrstring)
        ax.set_xticks(ind + (len(self.names)/2.0)*self.width)
        ax.set_xticklabels(labels) 
        ax.tick_params(axis=u'both', which=u'both',length=0)
        if self.attrstring=='year': ax.set_xlabel('%s'%self.attrstring.upper())
        else: ax.set_xlabel('%s\nyear'%self.attrstring.upper())
        ax.legend([ax2[i][0] for i in range(len(self.names))], self.names,fancybox=True).get_frame().set_alpha(0.5)
        
        plt.plot()
        plt.show()
        
                    
        
        
            

            

        
            
    
    
    

    
    
    
    
    
    




