# -*- coding:utf-8 -*-
# __author__:yinpanqiang
import time
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
def func(a,b,c,x):
	return a*x**2+b*x+c
def func_d(a,b,x):
	return 2*a*x+b
def main(a,b,c):
	tick_start = time.time()
	#print(tick_start)
	q = 1e-06
	if (4*a*c-b**2)>0:
		print("此方程无解")
	else:
		t1,t = 820338753-b/2,-b/2
		#print(t1,t)
		while (abs(t1-t)>q):
			t = t1
			t1=t-func(a,b,c,t)/func_d(a,b,t)

		t2,t = -820338753-b/2,-b/2
		while (abs(t2-t)>q):
			t = t2
			t2=t-func(a,b,c,t)/func_d(a,b,t)
		if (t1-t2)>q:
			print("方程解为{:.2f}和{:.2f}".format(t1,t2))
		else:
			print("方程有一个解为{:.2f}".format(t1))
	tick_end = time.time()
	#print(tick_end)
	print("执行时间为：{:.4f}us".format((tick_end-tick_start)*1e6))
	return t1,t2
def func_draw(a,b,c):
	mpl.rcParams['xtick.labelsize'] = 10
	mpl.rcParams['ytick.labelsize'] = 10
	(x1,x2)=main(a,b,c)
	#t = round(-b/(2*a))
	t1 = round(x1)
	t2 = round(x2)
	x = np.linspace(t2-5,t1+5,100)
	y = func(a,b,c,x)
	z = [0]*len(x)
	plt.figure("equation draw")
	plt.plot(x,y,'r')
	plt.plot(x,z,'r')
	#print(x1)
	plt.axvline(x1,color='green',linestyle = "--")
	plt.annotate("{:.2f}".format(x1),xy=(x1+0.5,2),color="r",size=10)
	plt.axvline(x2,color='red',linestyle = "--")
	plt.annotate("{:.2f}".format(x2),xy=(x2+0.5,2),color="r",size=10)
	#plt.axvline('20171103', color='green', lw=5)
	plt.show()


if __name__ == '__main__':
	print("输入3个参数a,b,c(用空格分隔)：")
	a,b,c = input().split()
	a,b,c = eval(a),eval(b),eval(c)
	#(x1,x2)=main(a,b,c)
	func_draw(a,b,c)
