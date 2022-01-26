import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

// time and space complexity 

// time: if there is N element in the given list , we need to loop through all the element once O(N)

// space: we create a set to add non non duplicate elemnt, if there are M non duplicate values the space complexity will be O(M)

public class DuplicatedProducts {
    public static void main(String[]args) {

        List<String> name = new ArrayList<String>();
        List<Integer> price = new ArrayList<Integer>();
        List<Integer> weight = new ArrayList<Integer>();
        name.add("ball");
        name.add("box");
        name.add("ball");
        name.add("ball");
        name.add("box");
        price.add(2);
        price.add(2);
        price.add(2);
        price.add(2);
        price.add(2);
        weight.add(1);
        weight.add(2);
        weight.add(1);
        weight.add(1);
        weight.add(3);
        int count = duplicatedProducts(name,price,weight);
        System.out.println(count);
		
	}
    public static int duplicatedProducts(List<String> name,List<Integer> price,List<Integer> weight ){
        // set is an unordered collection of objects in which duplicate values cannot be stored

        // the Method we are going to use in our approach
        // Method       description
        // add(element) adds elem only if the specified elem is not already present in the set, else the 
        //              function returns False if the elem is already present in the set

        // our approach is we combine name, price weight to one string 
        // we add it to the set
        // if the add method didn't return false we increment the count by one 
        int res = 0;

         // create a set 
         Set<String> set = new HashSet<>();
        // loop through all the products 
        for(int i = 0; i < price.size(); i++){

            String product = name.get(i)+ String.valueOf(price.get(i))+ String.valueOf(weight.get(i));
            
            if(set.add(product)){
                
            }else{
                // return false when we add, means there is a duplicate 
                res +=1;

            }
        }



        return res;

    }
    
    
}

/*
You are given a list of n products, each with a name, price and weight.

Find out how many duplicates of a product are present within the list. A duplicate is a product with all parameters, equal to some other product.

input is 3 lists

   Name Price Weight
 1. ball 2     1
 2. box  2     2
 3. ball 2     1
 4. ball 2     1
 5. box  2     3
output:

    2


*/

