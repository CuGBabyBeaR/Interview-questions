class LinkedList(object):

    class Node(object):

        def next(self):
            return self.__next
            pass

        def setNext(self, node):
            self.__next = node
            pass

        def data(self):
            return self.__data
            pass

        def setData(self, data):
            self.__data = data
            pass

        def __init__(self, data = None, next = None):
            self.__data = data
            self.__next = next
            pass

    __start = Node(None,None)
    __cursor = __start

    def fromList(self,list_in):
        pre = self.Node(list_in[0])
        self.__start.setNext(pre) 
        for data in list_in[1:]:
            node = self.Node(data,None)
            pre.setNext(node)
            pre = node
            pass
        pass

    def next(self):
        self.__cursor = self.__cursor.next()
        if not self.__cursor:
            return None
            pass
        return self.__cursor.data()
        pass

    def move(self,offset):
        if offset >= 0 :
            for x in xrange(0,offset):
                self.__cursor = self.__cursor.next()
                pass
            pass
        pass

    def moveto(self,index):
        self.__cursor = self.__start
        self.move(index)
        pass

    def moveBeforeFirst(self):
        self.__cursor = self.__start
        pass

    def insert(self,data,i):
        self.moveto(i)
        node = self.Node(data,self.__cursor.next())
        self.__cursor.setNext(node)
        pass

    def remove(self,i):
        self.moveto(i)
        pre = self.__cursor
        node = pre.next()
        pre.setNext(node.next())
        del node
        pass

    def generator(self):
        cur = self.__start.next()
        while cur:
            yield cur
            cur = cur.next()
            pass
        pass

    def __init__(self, list_in):
        super(LinkedList, self).__init__()
        self.fromList(list_in)

    def __del__( self ):  
        for node in self.generator():
            del node 
        pass 

    def __str__(self):
        if self.__start.next() == None:
            return ""
            pass
        return " => ".join([str(n.data()) for n in self.generator()])
