#ch 7 ex 2
import math


def isQueuefull():
	global SIZE, queue, front, rear
	if ((rear+1) % SIZE == front):
		return True
	else:
		return False

def isQueueEmpty():
	global SIZE, queue, front, rear
	if (front == rear):
		return True
	else:
		return False
def enQueue(data):
	global SIZE, queue, front, rear
	if (isQueuefull() == True):
		print("대기콜이 꽉 찼습니다")
		return
	rear = (rear+1) % SIZE
	queue[rear] = data

def deQueue():
	global SIZE, queue, front, rear

	if (isQueueEmpty() == True):
		print("대기콜이 비었습니다")
		return None
	front = (front+1) % SIZE
	data = queue[front]
	queue[front] = None
	return data

def calctime():
	global SIZE, queue, front, rear
	time = 0
	for i in range((front+1)%SIZE, (rear+1)%SIZE):
		time += queue[i][1]
	return time

#전역 변수
SIZE = 6
queue = [None for _ in range(SIZE)]
front = rear = 0


#메인 함수
if __name__ == "__main__":
	waitcall = [('사용',9),('고장',3),('환불',4),('환불',4),('고장',3)]
	for call in waitcall:
		print(f'귀하의 예상 대기시간은 {calctime()}분입니다.')
		print(f'현재 대기 콜-->{queue}')
		enQueue(call)
		print()

	print("최종 대기 콜 --> ",queue)
	print("프로그램 종료!")
