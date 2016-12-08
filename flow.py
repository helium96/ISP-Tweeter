#!/usr/bin/python
import os
import sys
from twython import Twython
 
def test():
        print 'Starting Speed Test'
        a = os.popen("speedtest-cli --simple").read()
        print 'Speed Test Complete'
        lines = a.split('\n')
        print a
        #if speedtest could not connect set the speeds to 0
        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
        #extract the values for ping down and up values
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]
        print date,p, d, u

        APP_KEY = ''  # Customer Key here
        APP_SECRET = ''  # Customer secret here
        OAUTH_TOKEN = ''  # Access Token here
        OAUTH_TOKEN_SECRET = ''  # Access Token Secret here

        twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
 
        #This fi when de crosses dem net naa wuk 
        if "Cannot" in a:
                try:
                        tweet="Hey @FLOWJamaica why is my internet down? I pay for 8down\\1up? #Fedup #PythonBot"
                        twitter.statuses.update(status=tweet)
                except:
                        pass
        elif eval(d)<8: #set de  speed yasso
                print "Attempting to Tweet FLOWJamaica"
                try:
                        tweet="Hey @FLOWJamaica. Why is my speed " + d + " mbps down and " + u + " mbps up when I pay for 8mbps/1mbps  #speedtest #PythonBot #FedUp @Garry4Flow "
                        twitter.update_status(status=tweet)
                        print tweet
                except Exception,e:
                        print str(e)
                        pass
        return
       
if __name__ == '__main__':
        test()
        print 'completed'
