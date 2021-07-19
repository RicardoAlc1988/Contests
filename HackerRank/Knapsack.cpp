using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Solution {

    
    static int min(int a, int b) {
        if(a < b) return a;
        return b;
    }
    
    // Complete the unboundedKnapsack function below.
    static int unboundedKnapsack(int k, int[] arr) {
        int n, c, max, temp;
        n = arr.Length;
        int[][] Knapsack = new int[n][];
        
        for(int i=0; i<n; i++) Knapsack[i] = new int[k+1];
        
        // Base cases
        for(int j=0; j<=k; j++) Knapsack[0][j] = (j/arr[0]) * arr[0];

        
        for(int i=1; i<n; i++) {
            c = k/arr[i];
            for(int j=0; j<=k; j++) {
                max = Int32.MinValue;
                for(int r=0; r<=min(j,c); r++) {
                    temp = r * arr[i];
                    if(temp <= j) {
                        temp = Knapsack[i-1][j-temp] + temp;
                        if(temp > max) max = temp;
                    }
                }
                Knapsack[i][j] = max;
            }
        }
        /*
        for(int i=0; i<n; i++) {
            for(int j=0; j<=k; j++) {
                Console.Write(Knapsack[i][j] + "   ");
            }
            Console.WriteLine();
        }
        */
        return Knapsack[n-1][k];
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);
        int result;
        int t = Convert.ToInt32(Console.ReadLine());
        for(int i=0; i<t; i++) {
            string[] nk = Console.ReadLine().Split(' ');

            int n = Convert.ToInt32(nk[0]);

            int k = Convert.ToInt32(nk[1]);

            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp));
            
            result = unboundedKnapsack(k, arr);
            textWriter.WriteLine(result);
        }


        textWriter.Flush();
        textWriter.Close();
    }
}
