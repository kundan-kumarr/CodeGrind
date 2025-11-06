def canConstruct(ransomnote, magazine):
    mag_dict= {}

    for ch in magazine:
        mag_dict[ch] = mag_dict.get(ch, 0) + 1
        print("mag_dict",mag_dict)
            
    for ch in ransomnote:
        if ch not in mag_dict and mag_dict[ch]==0:
            # print(mag_dict)
            return False
        mag_dict[ch] -=1
        print(mag_dict)



    return True


print(canConstruct("aab","aaab"))
    