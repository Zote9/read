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