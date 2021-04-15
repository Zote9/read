data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count +=1
        # if count % 1000 == 0:
            # print(len(data))
print('總共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
print('平均長度有', sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)

print('長度小於一百的資料總共有', len(new), '筆')

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('留言有提到 good 裡的資料總共有', len(good), '筆')
print(good[0])

# good = [d for d in data if 'good' in d]
# print(good)

bad = ['bad' in d for d in data]
print(len(bad))


# 文字計數
word_count = {}
for d in data:
    words = d.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1 # 新增key進進入 word_count 字典

for word in word_count:
    if word_count[word] > 1000000:
        print(word, word_count[word])
print(len(word_count))

while True:
    word = input('查詢關鍵字: ')
    if word == 'q':
        break
    if word in word_count:
    	print(word, '出現的次數為: ', word_count[word])
    else:
    	print('查無資料')
print('感謝使用')


