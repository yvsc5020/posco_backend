import pickle

data = {
    'ㄱ': 1, 'ㄲ': 2, 'ㄴ': 3, 'ㄷ': 4, 'ㄸ': 5, 'ㄹ': 6, 'ㅁ': 7,
    'ㅂ': 8, 'ㅃ': 9, 'ㅅ': 10, 'ㅆ': 11, 'ㅇ': 12, 'ㅈ': 13,
    'ㅉ': 14, 'ㅊ': 15, 'ㅋ': 16, 'ㅌ': 17, 'ㅍ': 18, 'ㅎ': 19,
    'ㅏ': 20, 'ㅐ': 21, 'ㅑ': 22, 'ㅒ': 23, 'ㅓ': 24, 'ㅔ': 25,
    'ㅕ': 26, 'ㅖ': 27, 'ㅗ': 28, 'ㅘ': 29, 'ㅙ': 30, 'ㅚ': 31,
    'ㅛ': 32, 'ㅜ': 33, 'ㅝ': 34, 'ㅞ': 35, 'ㅟ': 36, 'ㅠ': 37,
    'ㅡ': 38, 'ㅢ': 39, 'ㅣ': 40, '': 0, ' ': 99
}

path = 'domain/separate/c2i.pickle'

with open(path, 'wb') as fw:
    pickle.dump(data, fw)