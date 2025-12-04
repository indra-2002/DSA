class Solution:
    def median(self, matrix):
    	# code here 
    	n=len(matrix)
        m1=len(matrix[0])
    	low=min(row[0] for row in matrix)
    	high=max(row[-1] for row in matrix)
           	 
    	required=(n*
    	m1 +1)//2
        while low< high:
            
    	     
    	    mid=(low+high)//2
    	     
    	    count=0
    	    for row in matrix:
    	        
    	         
        	    l=0
        	    h=m1-1
        	    while l<=h:
        	        m=(l+h)//2
        	        if row[m]<=mid:
        	            l=m+1
        	        else:
        	            h=m-1
        	    count+=l
        	if count< required:
        	    low=mid+1
        	else:
        	    high=mid
        return low
    	