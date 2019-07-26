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

