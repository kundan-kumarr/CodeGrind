""""
Given two lists of strings artists and set_times of length n, 
write a function lineup() that maps each artist to their set time.

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

Input : String and dateime

output : will be  print the mapping 

"""

def lineup(str1, str2):
    artist_time = dict(zip(str1,str2))

    return artist_time

str1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
str2 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]


print(lineup(str1,str2))


#def lineup(l1, l2):
   # artist = {}
   # for i l1:
   #     for j in l2:
   #         artist[i] = j
   #     j+=1
   # i+=1
   # return artist