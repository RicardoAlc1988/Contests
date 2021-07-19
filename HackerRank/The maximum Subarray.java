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


    // Complete the maxSubarray function below.
    static int[] maxSubarray(int n, int[] arr) {
        int[] resul = new int[2];
        int[] subArray = new int[n];
        int[] subSequence = new int[n];
        int max;
        subArray[0] = arr[0];
        subSequence[0] = arr[0];
        max = subSequence[0];
        for(int i=1; i<n; i++) {
            subSequence[i] = Math.Max(Math.Max(subSequence[i-1] + arr[i], subSequence[i-1]),arr[i]);
            subArray[i] = Math.Max(subArray[i-1]+arr[i], arr[i]);
            if(subArray[i] > max) max = subArray[i];
            Console.WriteLine("i: " + subArray[i]);
 
        }
        resul[0] = max;
        resul[1] = subSequence[n-1];
        return resul;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int t = Convert.ToInt32(Console.ReadLine());

        for (int tItr = 0; tItr < t; tItr++) {
            int n = Convert.ToInt32(Console.ReadLine());

            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp))
            ;
            int[] result = maxSubarray(n, arr);

            textWriter.WriteLine(string.Join(" ", result));
        }

        textWriter.Flush();
        textWriter.Close();
    }
}
