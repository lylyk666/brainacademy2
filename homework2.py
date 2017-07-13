#! /usr/bin/python
# -*- coding: utf8 -*-

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n",'--name', type=str)

parser.add_argument("-a", '--age', type=int)

args = parser.parse_args()

name = args.name
age = args.age
count=0



if __name__ == '__main__':
    print ('Welcome %s your age is %s' %(name, age))
print("Рівень 1")
print("Питання 1\n"
	  "Столиця України Київ?(так або ні)")
answer=str(input())
if answer=="так":
	count+=1
	print("Правильна відповідь! Кількість балів - %s" %count)
else:
	print("Відповідь неправильна, кількість балів %s" %count)	
	input ()	;
	exit()
print("Питання 2\n"
		  "2+2=4?(так або ні)")
answer=str(input())
if answer=="так":
	count+=1
	print("Правильна відповідь! Кількість балів - %s" %count)
else:
	print("Відповідь неправильна, кількість балів %s" %count)	
	input()
	exit()   
print("Питання 3\n"
	  "Україна стала незалежною в 1990?(так або ні)")
answer=str(input())
if answer=="ні":
	count+=1
	print("Правильна відповідь! Кількість балів - %s і ви переходите на 2 рівень" %count)
else:
	print("Відповідь неправильна, кількість балів %s" %count)	
	input()
	exit() 
print("Рівень 2")    
print("Питання 4\n"
	  "Porshe марка країни Німеччина?(так або ні)")
answer=str(input())
if answer=="так":
	count+=1
	print("Правильна відповідь! Кількість балів - %s" %count)
else:
	print("Відповідь неправильна, кількість балів %s" %count)	
	input()
	exit()
print("Питання 5\n"
	  "Число пі рівне 3.14?(так або ні)")
answer=str(input())
if answer=="так":
	count+=1
	print("Правильна відповідь! Кількість балів - %s" %count)
else:
	print("Відповідь неправильна, кількість балів %s" %count)	
	input()
	exit()   
print("Питання 6\n"
	  "Python був розроблений в 1998?(так або ні)")
answer=str(input())
if answer=="ні":
	count+=1
	print("Правильна відповідь! Кількість балів - %s і ви переходите на 3 рівень" %count)
else:
	print("Відповідь неправильна, кількість балів %s" %count)	
	input()
	exit() 
print("Рівень 3")    
print("Питання 7\n"
	  "Першим президентом України був Кучма?(так або ні)")
answer=str(input())
if answer=="ні":
	count+=1
	print("Правильна відповідь! Кількість балів - %s" %count)
else:
	print("Відповідь неправильна, кількість балів %s" %count)	
	input()
	exit()
print("Питання 8\n"
	  "Якщо в людини 47 хромосом то це погано?(так або ні)")
answer=str(input())
if answer=="так":
	count+=1
	print("Правильна відповідь! Кількість балів - %s" %count)
else:
	print("Відповідь неправильна, кількість балів %s" %count)	
	input()
	exit()   
print("Питання 9\n"
	  "У дорослої людини 32 зуба?(так або ні)")
answer=str(input())
if answer=="так":
	count+=1
	print("Правильна відповідь! Ви пройшли тест і набрали максимальну кількість балів - %s" %count)
else:
	print("Відповідь неправильна, кількість балів %s" %count)	
	input()
	exit()     
    
    
