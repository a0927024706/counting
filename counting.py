data = ['珍珠奶茶 3', '鹹酥雞 2', '珍珠奶茶 4', '綠茶 3', '蛋糕 1']
product = {}
for d in data:
	name, count = d.split(' ')
	count = int(count)
	if name in product:
		product[name] += count
	else:
		product[name] = count
print(product)
