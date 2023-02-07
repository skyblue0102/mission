#ch 7 ex 1
def isQueuefull():
	global SIZE, queue, front, rear
	if (rear == SIZE-1):
		return True
	else:
		return False

def isQueueEmpty():
	global SIZE, queue, front, rear
	if (front == rear):
		return True
	else:
		return False
def enQueue(person):
	global SIZE, queue, front, rear
	if (isQueuefull() == True):
		print("줄이 꽉 찼습니다")
		return
	rear += 1
	queue[rear] = person

def deQueue():
	global SIZE, queue, front, rear

	if (isQueueEmpty() == True):
		print("줄이 비었습니다")
		return None
	front += 1
	person = queue[front]
	queue[front] = None

	for i in range(front + 1, rear+1):
		queue[i - 1] = queue[i]
		queue[i] = None
	front -= 1
	rear -= 1
	return person

#전역 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

#메인 함수
if __name__ == "__main__":
	enQueue('정국')
	enQueue('뷔')
	enQueue('지민')
	enQueue('진')
	enQueue('슈가')
	print(f'대기 줄 상태:{queue}')

	for _ in range(rear+1):
		print(f'{deQueue()}님이 식당에 들어감')
		print(f'대기 줄 상태:{queue}')
	print('식당 영업 종료!')
