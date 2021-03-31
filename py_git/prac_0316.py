####!------------------模块++++-------------------!
for x in range(1,11):
        print('{0:2d}{1:3d}{2:4d}'.format(x,x*x,x*x*x))

####!------------------模块++++-------------------!
import suport

suport.support(1)



####!------------------矩阵转置++++-------------------!
print('---------矩阵转置---------')

matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])
print('---------矩阵转置-方式2---------')

transposed=[]
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

####!------------------函数++++-------------------!

def log(pr):#将被装饰函数传入
    def wrapper():
        print("**********")      
        return pr()#执行被装饰的函数
    return wrapper#将装饰完之后的函数返回（返回的是函数名）
@log
def pr():
    print("我是小小洋")

pr()
print()

####!------------------函数-------------------!
def Foo(x):
    if (x==1):
        print('-----x= ',x)
        return 1
    else:
        print('x:',x,',Foo:',Foo(x-1))
        print('x+Foo(x-1)= ',x+Foo(x-1))
        print()
        return x+Foo(x-1)

print(Foo(4))

####!------------------iter 和next 循环-------------------!
print('---------iter 和next  循环---------')

list=[1,2,3,4]
it = iter(list)
for x in it:
	print (x,end=",  ")

its= iter(list)
for y in its :
	print(y,end =',  ')



print()

####!------------------for 和while 循环-------------------!
print('---------for 和while 循环---------')
sites=["python","java",'math','c++','dodo']
for site in sites:
	if site!='math':
		print('这科是：'+site)
	else:
		print('终于是'+site)

print()
site="python"
print('--')

while site in sites:
	print(iter(sites))
	if site=='math':
		print('今天无课,是' +site)
		
	else:
		print('今天是'+site)
		break
		
		
####!------------------整除-------------------!
a=2
b=3
print()
print("---------数字整除测试!---------")

gusess= int(input('请输入测试数字：'))
if gusess%a==0:
	if gusess%b== 0:
		print('输入的数字%d'%gusess +'能被2和3整除')
	else:
		print('输入的数字%d'%gusess +'只能被2整除')
else:
	if gusess%b== 0:
		print('输入的数字%d'%gusess +'只能被3整除')
	else:
		print('输入的数字%d'%gusess +'不能被2和3整除')
		
####!------------------猜数字游戏-------------------!
number =7
guess =-1
print()
print("---------数字猜谜游戏!---------")
while guess!=number:
	guess= int(input('请输入猜测的数字：'))
	if guess == number:
		print('数字：%d'%guess+' 猜对啦!')
	elif guess > number:
		print('数字：%d'%guess+' 猜大啦!')
	elif guess < number:
		print('数字：%d'%guess+' 猜小啦!')

