def recursion(products, parent_name):
	for product in products:
		name = product['name']
		print(f'Текущий - {name}, Родитель - {parent_name}')
		sub_products = product.get('products', [])
		if sub_products:
			recursion(sub_products, name)

products = ['glj', '4rtr4t']
recursion(products, 'root')
# products - твой список со словарями, name - это как будет называться твой список, в примере я указал 'root', типа корневой элемент.

# key_diff = 'services'
# if key_diff in o_file:
#     print(key_diff)
# else:
#     print('Не нашел')
#
# if (o_file['data']['services']) != (n_file['data']['services']):
#     print('Вот искомое расхождение: ', n_file['data']['services'])