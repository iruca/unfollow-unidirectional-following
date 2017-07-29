#!/usr/bin/python
#-*- coding:utf-8 -*-

from requests_oauthlib import OAuth1Session
import json
import traceback

def find_users_not_following_me(oauth_client):
    """
    using twitter following API, find a following user who is not following back me.
    Args:
      oauth_client: OAuth1Session object which is initiated with OAuth1Session(ConsumeKey, ConsumerSecret, AccessTokne, AccessTokenSecret)
    Returns:
      user_id list of the users which are not following me but I'm following
    """

    # following (otherwise known as their friends)
    following_api_url = "https://api.twitter.com/1.1/friends/ids.json"
    follower_api_url = "https://api.twitter.com/1.1/followers/ids.json"

    user_ids =[]
    try:
        # API call to get following/follower users 
        following_api_response = oauth_client.get(following_api_url)
        follower_api_response = oauth_client.get(follower_api_url)
        if following_api_response.status_code == 200 and follower_api_response.status_code == 200:
            # parse JSON
            following_user_ids = json.loads( following_api_response.text )["ids"]
            follower_user_ids = json.loads( follower_api_response.text )["ids"]
            
        else:
            # status code is not 200 OK
            raise IOError("couldn't get following/follower users by twitter's  API.")
    except:
        raise IOError("unexpected error occurred while consuming twitter's following/follower API. stacktrace="+ traceback.format_exc())
 
    # return the diff of the following users and follower users   
    return list( set( following_user_ids ) - set( follower_user_ids ) )

def unfollow( oauth_client, user_id ):
    """
    unfollow user
    """
    target_url = "https://api.twitter.com/1.1/friendships/destroy.json"
    params = { "user_id" : user_id }

    try:
        response = oauth_client.post(target_url, params=params )
        
        if response.status_code != 200:
            raise IOError("couldn't unfollow user. user_id="+ str(user_id) +", API response = "+ response.text )
        
        return True
    except:
        raise IOError("couldn't unfollow user. user_id="+ str(user_id) +", stack trace="+ traceback.format_exc() )


def show_user( oauth_client, user_id ):
    """
    show specific user's information
    Returns:
      user information dictionary object
    """
    target_url = "https://api.twitter.com/1.1/users/show.json?user_id="+ str(user_id)

    try:
        response = oauth_client.get(target_url )
        
        if response.status_code != 200:
            raise IOError("couldn't get user information. user_id="+ str(user_id) +", API response = "+ response.text )
        
        return json.loads( response.text )
    except:
        raise IOError("couldn't unfollow user. user_id="+ str(user_id) +", stack trace="+ traceback.format_exc() )



# simple test by running this script
if __name__ == "__main__":
    import sys

    CK = sys.argv[1]
    CS = sys.argv[2]
    AT = sys.argv[3]
    AS = sys.argv[4]

    twitter_client = OAuth1Session(CK, CS, AT, AS)
    
    # target_users = find_users_not_following_me(twitter_client )
    print show_user(twitter_client, 756491757760622593)["screen_name"]

    print unfollow( twitter_client, 756491757760622593 )
