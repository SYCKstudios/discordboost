import discord

tyep =  {discord.MessageType.default : 'normal', discord.MessageType.premium_guild_subscription : 'boost', discord.MessageType.premium_guild_tier_1 : 'level 1', discord.MessageType.premium_guild_tier_2 : 'level 2', discord.MessageType.premium_guild_tier_3 : 'level 3'}

def which(message):
    try:
        return tyep[message.type]
    except:
        return 'other'

class boost:
    def check(message):
        done = which(message)
        return done

    def name(message):
        return message.author
    
    def total(message):
        return message.guild.premium_subscription_count