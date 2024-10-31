import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 1
'''This function inputs 2 points and returns a Rectangle. This function checks which which point
has the greatest x and y values and assigns that point to be the bottomRight and topLeft points
of the new Rectangle respectively. It then returns this new Rectangle.
'''
def create_rectangle(pt1:data.Point, pt2:data.Point) -> data.Rectangle:
    if pt1.y > pt2.y:
        topLeft = pt1
    else:
        topLeft = pt2
    if pt1.x > pt1.x:
        bottomRight = pt1
    else:
        bottomRight = pt2
    return data.Rectangle(topLeft, bottomRight)

# Part 2
'''This function inputs 2 durations and outputs a boolean. This function checks the length of the 
first Duration against the length of the second and returns True if the first Duration is shorter
than the second, and False if the second Duration is shorter. 
'''
def shorter_duration_than(dur1:data.Duration, dur2:data.Duration) -> bool:
    if (dur1.minutes * 60) + dur1.seconds < (dur2.minutes * 60) + dur2.seconds:
        return True
    else:
        return False

# Part 3
'''This function inputs a list of Songs and a Duration and outputs a list of Songs. This function
inputs the list of Songs and checks the length of each Song against the length of the provided 
Duration. It adds any Songs of a length less than the provided Duration and adds them to a new
list. The function then returns that new list. 
'''
def song_shorter_than(vals:list[data.Song],dur:data.Duration) -> list[data.Song]:
    newList = []
    for i in range(len(vals)):
        if  shorter_duration_than(vals[i].duration, dur):
            newList.append(vals[i])
    return newList

# Part 4
'''This function inputs a list of Songs and a list of ints and outputs a Duration. This function
takes the elements of the list of songs that correlate to each number in the list of ints 
(treating each int as an index) and adds the duration of each of these marked songs to some new,
total duration. The function makes sure the duration doesn't have an improper amount of seconds,
then returns the duration. 
'''
def running_time(vals:list[data.Song], idx:list[int]) -> data.Duration:
    playlist = []
    dur = data.Duration(0,0)
    for i in range(len(vals)):
        if i in idx:
            playlist.append(vals[i])
    for j in range(len(playlist)):
        dur.minutes += playlist[j].duration.minutes
        dur.seconds += playlist[j].duration.seconds
    while dur.seconds > 59:
        dur.minutes += 1
        dur.seconds -= 60
    return dur

# Part 5
'''This function inputs a list of list of strings and a list of strings and outputs a boolean.
This function takes the input list of list of strings (which must always be two strings long) and
uses them as a guide. The route, or the input list of strings, checks each string pair against
the guide. If each string pair is in the guide, the function returns True. Otherwise, it returns
False. 
'''
def validate_route(paths:list[list[str]], route:list[str]) -> bool:
    broken_route = []
    check = 0
    for i in range(len(route) - 1):
        broken_route.append([route[i], route[i+1]])
    for j in range(len(broken_route)):
        if broken_route[j] in paths or broken_route[j] in [paths[1], paths[0]]:
            check += 1
    if check == len(broken_route):
        return True
    else:
        return False

# Part 6
def longest_repetition(input:list[int]) -> Optional[int]:
    if len(input) < 1:
        return None
    longest_rep = 0
    longest_rep_ttl = 0
    current_len = 1
    current_idx = 0
    for i in range(len(input) - 1):
        if list[i] == list[i+1]:
            current_len += 1
        else:
            if current_len > longest_rep:
                longest_rep = current_idx
            current_length = 1
            current_idx = i + 1
        if current_len > longest_rep:
            longest_rep_ttl = current_idx
    return longest_rep_ttl

