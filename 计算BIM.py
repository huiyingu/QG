weight = float(input('请输入体重(kg)：'))
high = float(input('请输入身高(m)：'))
BIM = weight / high / high
print(BIM)
if BIM < 18.5:
    print('体重过轻')
elif BIM > 24:
    print('体重超重')
else:
    print('刚刚好')
