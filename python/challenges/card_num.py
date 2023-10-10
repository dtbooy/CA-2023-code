card_num = "1234567890123456"
print(len(card_num) == 13 or 16)
print(len(card_num) == (13 or 16))
print(len(card_num) == 13 or len(card_num) == 16)