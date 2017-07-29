# unfollow-unidirectional-following
unfollow a user which is not following me but I'm following

# Usage
Firstly, you need to create new application and get consumer_key, consumer_secret, access_token and  access_token_secret to consume Twitter API...

https://apps.twitter.com/

then, 
```
pythhon unfollow_user.py [consumer_key] [consumer_secret] [access_token] [access_token_secret]
```

This will unfollow a randomly chosen user that is not following you but you were following.

Output will be as follows:

```
[2017-07-29 07:52:03.107100] successfully unfollow a user. user_id=2835089755, screen_name=infokikoku
```
