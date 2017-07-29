#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
Unfollow one of the users who are not following me.
target user is randomly chosen.

Usage:
python unfollow_user.py [consumer key] [consumer secret] [access token] [access_token_secret]
"""
__author__ = "iruca21"

import sys
import twitter_util
from datetime import datetime
import random
random.seed()

from requests_oauthlib import OAuth1Session

#-------------------------

if len( sys.argv ) != 5:
    print "Usage:"
    print "python unfollow_user.py [consumer key] [consumer secret] [access token] [access_token_secret]"
    sys.exit(1)

CK = sys.argv[1]
CS = sys.argv[2]
AT = sys.argv[3]
AS = sys.argv[4]

twitter_client = OAuth1Session(CK, CS, AT, AS)

# seek  following users who are not following me
target_user_ids = twitter_util.find_users_not_following_me(twitter_client)

# randomly choose a user
target_user_id = random.choice( target_user_ids )

# get user information and unfollow
user_info = twitter_util.show_user( twitter_client,  target_user_id )
unfollow_succeeded = twitter_util.unfollow( twitter_client, target_user_id )

if unfollow_succeeded:
    print "[%s] successfully unfollow a user. user_id=%s, screen_name=%s" % (str(datetime.now()), target_user_id, user_info["screen_name"] )
else:
    print "[%s] failed to unfollow a user. user_id=%s" % (str(datetime.now()), target_user_id)

