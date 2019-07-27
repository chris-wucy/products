# refactor 重構，用function
import os # 載入作業系統，才有權限查看
# 讀取檔案
# 資料是長-> ramen,250
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 用continue跳過寫入'商品,價格'，繼續下一個迴圈
			name, price = line.strip().split(',') 
			# strip把換行符號 \n, 拿掉split用逗點當作切割字串的標準
			products.append([name, price])
	return products	


# 讓使用者輸入
def user_input(products):
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
	return products
# 第一個[0]代表大清單的第1格，
# 第2個[0]代表大清單的第1格裡面的小清單的第1格
# products[0][0]
# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])
# 字串合併用加法 'abc' + '123' = 'abc123'
# 字串也可以乘法 'abc' * 3 = 'abcabcabc'
# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f: # 打開檔案, f.write寫入csv檔
		f.write('商品,價格\n') # 先寫入欄位，並於上方加入encoding = 'utf-8' 解決中文亂碼問題
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') # \n :換行

# 主程式碼 main function
def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # # 先檢查檔案在不在電腦裡，以免crash, 用 isfile 功能檢查檔案在不在
		print('yeah! 找到檔案！')
		products = read_file(filename)
	else:
		print('找不到檔案....')

	products = user_input(products)
	print_products(products)
	write_file(filename, products)

main() # 呼叫main function才開始執行