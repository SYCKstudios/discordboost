# discord-boost

This is a very small and simple package to help beginner discord.py coders do something when someone boosts

to install it from pip, do:

```
pip install discord-boost
```


To install it from github, do:

```
$ git clone https://github.com/SYCKstudios/discordboost
$ cd discord-boost
$ python3 setup.py install
```

<h1> **Usage**

This is to be used under an `on_message` event.

```python
from boost import boost

#all the normal bot stuff

@bot.event
async def on_message(message):
    check = boost.check(message)

    if check == 'boost':
        # do your stuff
```


`boost.check(message)` - It checks if someone boosted or not when someone messages. It returns a `str` object.
<h4> outcomes of boost.check

 If no one boosted, then it returns `'normal'`
 If someone boosts, it returns `'boost'`
 If someone boosts the server to level 1, it returns `'level 1'`
 If someone boosts the server to level 2, it returns `'level 2'`
 If someone boosts the server to level 3, it returns `'level 3'`

 
 `boost.name(message)` - Returns the user who boosted the server. It gives a `discord.Member` object.

 `boost.total(message)` - Returns the total boosts a guild has. It gives an `int` object.