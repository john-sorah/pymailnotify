#!/usr/bin/python
# -*- coding: utf-8 -*-

###################################################################
###	Unяead e-mail notification script by John Sorah 
###	<kwttj122[at]gmail.com>
###	Redistr. under GNU/GPL v2
###################################################################

#import libraries
import imaplib, email
import sys
import pynotify
import time

imap_svr = "" # put your imap server address here
login = ""    # put your imap server login here
passw = ""    # put your imap server password here

#	HINT:
#	nohup ./mailnotify.py 2>&1 >/dev/null &
#	will run this script in background mode

# the main loop
while 1==1:
	#trying to login to imap
	try:
		#initializing and logging in
		conn = imaplib.IMAP4_SSL(imap_svr)
		(retcode, capabilities) = conn.login(login, passw)
	except:
		#showing error message and exiting
		n = pynotify.Notification("Login error","Check your settings or internet connection","notification-message-im")
		n.show()
		sys.exit(1)
	# quering unread messages
	conn.select(readonly=1)
	(retcode, messages) = conn.search(None, '(UNSEEN)')
	try:
		#if we have unread messages - desplayin` notify
		if len(messages[0]) > 0:
			pynotify.init("icon-summary-body")
			n = pynotify.Notification("New message","You have a new message(s) on your "+login+" account!","notification-message-im")
			n.set_timeout(3000) 
			n.show()
			time.sleep(25) # additional delay
	except:
		# if no unread messages
		print("No unread e-mails here!") # just print this to stdour
	time.sleep(25)# delay
