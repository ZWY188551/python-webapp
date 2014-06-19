#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading,time
'For Thread Test'
__author__='ZWY'

def loop():
	print 'Now running this thread: %s'%threading.current_thread().name
	n=0
	while n<=5:
		n=n+1
		print 'thread: %s>>>%s'%(threading.current_thread().name,n)
		time.sleep(1)
	print 'Thread is end %s'%threading.current_thread().name

print 'Now running this thread: %s'%threading.current_thread().name
t=threading.Thread(target=loop,name='loopThread')
t.start()
t.join()
print 'Thread is end %s'%threading.current_thread().name