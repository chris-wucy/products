products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	# p = []
	# p.append(name)
	# p.append(price)
	# 簡易法
	products.append([name, price])
print(products)

# 第一個[0]代表大清單的第1格，
# 第2個[0]代表大清單的第1格裡面的小清單的第1格
# products[0][0]

for p in products:
	print(p[0], '的價格是', p[1])

# 字串合併用加法 'abc' + '123' = 'abc123'
# 字串也可以乘法 'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w', encoding = 'utf-8') as f: # 打開檔案, f.write寫入csv檔
	f.write('商品,價格\n') # 先寫入欄位，並於上方加入encoding = 'utf-8' 解決中文亂碼問題
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # \n :換行
