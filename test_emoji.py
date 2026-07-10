import unicodedata
import os

animals = ["panda", "koala", "lion", "tiger", "bear", "fox", "dog", "cat", "rabbit", "monkey", "frog", "elephant", "penguin", "pig", "owl", "deer", "wolf", "sheep", "cow", "horse", "chicken", "duck", "turtle", "snake", "lizard", "shark", "whale", "dolphin", "octopus", "crab", "spider", "bee", "butterfly", "bat", "squirrel", "raccoon", "beaver", "kangaroo", "zebra", "giraffe", "hippo", "rhino", "cheetah", "eagle", "parrot", "gorilla", "sloth", "otter", "skunk", "badger", "flamingo", "peacock", "swan", "dove", "turkey", "rooster", "hatching_chick", "bug", "ant", "snail", "scorpion", "mosquito", "cricket", "microbe", "t-rex", "sauropod"]

for a in animals:
    try:
        # Try a few common emoji name patterns
        char = None
        for suffix in ["", " FACE", " HEAD"]:
            try:
                char = unicodedata.lookup(a.replace("_", " ").upper() + suffix)
                break
            except KeyError:
                continue
        if char:
            h = hex(ord(char))[2:]
            print(f"{a}: {h}")
        else:
            print(f"{a}: NOT FOUND")
    except Exception as e:
        pass
