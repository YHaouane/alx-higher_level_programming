#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)

    if (len_s == 0):
        multi_r = (len_s, None)
    else:
        multi_r = (len_s, sentence[0])
    return (multi_r)
