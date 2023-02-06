import random
import math

## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printStores(start) :
	current = start
	if current == None :
		return

	while current.link != head:
		current = current.link
		x, y = current.data[1:]
		print(current.data[0], '편의점, 거리:', math.sqrt(x*x + y*y))
	print()

def  StoreList(store) :
	global head, current, pre

	node = Node()
	node.data = store

	if head == None :
		head = node
		node.link = head
		return

	nodeX, nodeY = node.data[1:]
	nodeDistance = math.sqrt(nodeX*nodeX + nodeY*nodeY)
	headX, headY = head.data[1:]
	headDistance = math.sqrt(headX*headX + headY*headY)

	if headDistance > nodeDistance :
		node.link = head
		last = head
		while last.link != head :
			last = last.link
		last.link = node
		head = node
		return

	current = head
	while current.link != head :
		pre = current
		current = current.link
		currX, currY = current.data[1:]
		currDistance = math.sqrt(currX*currX + currY*currY)
		if currDistance > nodeDistance :
			pre.link = node
			node.link = current
			return

	current.link = node
	node.link = head

## 전역 변수
head, current, pre = None, None, None

## 메인 코드
if __name__ == "__main__" :

	storeArray = []
	storeName = 'A'
	for _ in range(10) :
		store = (storeName, random.randint(1, 100), random.randint(1, 100) )
		storeArray.append(store)
		storeName = chr(ord(storeName) + 1)

	for store in storeArray :
		StoreList(store)

	printStores(head)