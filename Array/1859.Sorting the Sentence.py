class Solution:
    def sortSentence(self, s: str) -> str:
        
        word = s.split()
        ans = [None] * len(word)
        
        """
        list indexing, it returns all elements[:]
             0 1 2 3 4        
        a = [1,2,3,4,5]
        a[start:end]
        
        a[:-1]
        [1,2,3,4]
        
        a[2:3]
        [3]
        """
        
        """
        None keyword is used to define a null variable or an object
        """
        
        """
        How to Initialize a list with an size and values
        example:
        l = [0] * 10
        print(l)
        #[0,0,0,0,0,0,0,0,0,0]
        """
        for w in word:
            # the given 1-indexed word position starts at 1
            # but the list index start at 0 so we need to subtract 1
            # [:-1] not include the last char of each word
            ans[int(w[-1]) -1] = w[:-1]
        
        """
        join() method takes all items in an iterable and joins them into one string
        A string must be specified as the separatoe
        
        Syntax
        string.join(iterable)
        """
        
        return " ". join(ans)
            
            
                
        
        
        
        
        
        
        """
        Python String Split Method 
        
        Splits a string into a list 
        
        Syntax
        string.split(separator,maxsplit)
        
        Parameter  Description
        maxsplit   how many splits to do.
        
        example with parameter maxsplit:
        
        txt = "apple#banana#cherry#orange"
        
        x = txt.split("#",1)
        # max split parameter is 1 will return a list with 2 elements
        
        print(x)
        # result will be "apple,#banana#cherry#orange"
        """
