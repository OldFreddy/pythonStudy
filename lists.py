bicucles = ['bike', 'cannondale', 'redline', 'specialized']
print(bicucles)
print(bicucles[0])
print(bicucles[1])
print(bicucles[2])
print(bicucles[3])

bicucles.append('123')
print(bicucles)

bicucles.insert(0, '55555')
print(bicucles)

del bicucles[0]
print(bicucles)
poppet_bicucle = bicucles.pop()
print(bicucles)
print(poppet_bicucle)