class myQueue:
    def __init__(self):
        self.queueList = []

    def isEmpty(self):
        return self.size() == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.queueList[0]

    def back(self):
        if self.isEmpty():
            return None
        return self.queueList[-1]

    def size(self):
        return len(self.queueList)

    def enqueue(self, value):
        self.queueList.append(value)

    def dequeue(self):
        if self.isEmpty():
            return None
        front = self.front()
        self.queueList.remove(self.front())
        return front


queue = myQueue()

while queue.isEmpty() == False:
    print("Dequeue(): " + str(queue.dequeue()))

def findBin(number):
    result = []
    queue = myQueue()
    queue.enqueue(1)
    for i in range(number):
        print("i is", i)
        # print("queue[0] is ",str(queue.dequeue()))

        result.append(str(queue.dequeue()))
        print(" After result appended the dequeue is", result)
        print("result[", i, "]", "is", result[i])

        s1 = result[i] + "0"
        print("s1 = ", s1)

        s2 = result[i] + "1"
        print("s2 = ", s2)

        queue.enqueue(s1)
        queue.enqueue(s2)
        # print("queue is ", queue)

    return result;  # For number = 3 , result = {"1","10","11"};


print(findBin(7))