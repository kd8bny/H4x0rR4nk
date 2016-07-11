import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {  

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        try{
            /* First lets get all of our data and make it pretty*/
            int[] time = new int[2];
            int[] prevRand = new int[10];
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int numCases = Integer.parseInt(br.readLine()); 

            for(int i = 0; i < numCases; i++){
                String[] TIME = new String[2];
                TIME = br.readLine().split(" ");
                time[0] = Integer.parseInt(TIME[0]);
                time[1] = Integer.parseInt(TIME[1]);
                for(int j = 0; j < 10; j++){
                    prevRand[j] = Integer.parseInt(br.readLine());
                }
            
            /* 
            * Here is the flow to the problem
            * First we have to make a new random number and set the seed to the time 
            * https://docs.oracle.com/javase/7/docs/api/java/util/Random.html
            * The purpose of the loop is to inc the time by one until we find a 
            * set of 10 rand nums that match the last. After the count hits 10 
            * we calculate the next 10 and stop
            */
                Random rand = new Random();
                rand.setSeed(time[0]);

                int seedTime = time[0];
                int count = 0;
                while(true){
                    int temp = rand.nextInt(1000);
                    if(count == 9){
                        String ans = seedTime + " ";
                        for(int j = 0; j < 10; j++){
                            ans += rand.nextInt(1000) + " ";
                        }
                        System.out.println(ans);
                        break;   
                    }else{
                        if(temp == prevRand[count]){
                            count++;
                        }else{
                            count = 0;
                            seedTime++;
                            rand.setSeed(seedTime);
                        }
                    }
                }     
            }
        }catch(IOException e){}
    }
}
