class Solution {
    public int mostWordsFound(String[] sentences) {
        
        int res = 0;
        int count = 0;
        for(String s: sentences){
            
            for(int i = 0; i < s.length(); i++){
                if(s.charAt(i) == ' '){
                    count += 1;
                }
            }
            res = Math.max(res,count);
            count = 0;
        }
        return res + 1;
        
    }
}
// count the space in each sentence and return Max Count + 1
