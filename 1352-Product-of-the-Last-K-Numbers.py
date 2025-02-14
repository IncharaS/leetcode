class ProductOfNumbers(object):

    def __init__(self):
        self.productList = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.productList = [1]
        else:
            self.productList.append(self.productList[-1] * num)
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        ## because there was a zero in the previous deleted list
        l = len(self.productList)
        if k >= l:
            return 0
        
        return self.productList[-1]//self.productList[-(k+1)]


        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)