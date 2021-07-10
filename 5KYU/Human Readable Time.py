"""
Write a function to covert seconds into human readable format as HH:MM:SS
"""

def make_readable(seconds):

    hours = int(seconds/3600)
    minutes = int(seconds%3600/60)
    secs = seconds%3600%60

    return f'{hours:02}:{minutes:02}:{secs:02}'
