class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0;
        int count = 0;
        for(int num:nums){
            if(num == 1){
                
                count+=1;
                maxCount = Math.max(maxCount,count);
            }
            else{
                count = 0;
            }
            
        }
        return maxCount;
        
        
    }
    // Approach:
    // we need a var maxCount to keep track of the max init to 0;
    
    // another max in the loop to keep track of the count of 1's, if we see a one we
    // increment one, if we see a zero we reset to zero 
    
    // use for each loop to loop through nums

}
