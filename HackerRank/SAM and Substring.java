import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'substrings' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING n as parameter.
     */

    public static long substrings(String n) {
        long module = 1000000007;
    // Write your code here
        Long[] substringsSum = new Long[n.length()];
        Long parsedValue = Long.parseUnsignedLong(String.valueOf(n.charAt(0))); 
        substringsSum[0] = parsedValue;
        System.out.println(substringsSum[0]);
        Long resul = substringsSum[0];
        for (int i=1; i<n.length(); i++) {
            parsedValue = Long.parseUnsignedLong(String.valueOf(n.charAt(i)));
            substringsSum[i] = ((substringsSum[i-1] * 10) % module + ((i+1) * parsedValue) % module) % module;
            // System.out.println(substringsSum[i]);
            resul += substringsSum[i] % module;
        } 
        return resul % module;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String n = bufferedReader.readLine();

        long result = Result.substrings(n);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}