from difflib import SequenceMatcher

def GetStringsSimilarityRatio(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    sm = SequenceMatcher(None, s1, s2)

    #print(s1, s2, sm.ratio())

    return sm.ratio()