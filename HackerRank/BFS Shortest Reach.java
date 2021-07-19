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
        
    static void setArray(int n, int s, int[] cost) {
        for(int i=0; i<n; i++) {
            if(i == (s-1)) cost[i] = 0;
            else cost[i] = -1;
        }
    }
    
    static List<int>[] buildGraph(int n, int m, int[][] edges) {
        List<int>[] graph = new List<int>[n];
        for(int i=0; i<n; i++) {
            graph[i] = new List<int>();
        }
        for(int k=0; k<m; k++) {
            graph[edges[k][0]-1].Add(edges[k][1]-1);
            graph[edges[k][1]-1].Add(edges[k][0]-1);
        }
        /*
        for(int i=0; i< n; i++) {
            foreach(int v in graph[i]) {
                Console.Write(i + " - " + v + " ");
            }
            Console.WriteLine();
        }
        */
        return graph;
    }
    
    // Complete the bfs function below.
    static int[] bfs(int n, int m, int[][] edges, int s) {
        int[] cost = new int[n];
        setArray(n, s, cost);
        int parent; 
        bool[] markedNodes = new bool[n];
        Array.Clear(markedNodes, 0, markedNodes.Length);
        List<int>[] graph = buildGraph(n, m, edges);
        Queue<int> nodesQueue = new Queue<int>();
        nodesQueue.Enqueue(s-1);
        markedNodes[s-1]=true;
        cost[s-1] = 0;
        while(nodesQueue.Any()) {
            parent = nodesQueue.Dequeue();
            foreach(int childrenNode in graph[parent]) {
                if(!markedNodes[childrenNode]) {
                    markedNodes[childrenNode] = true;
                    nodesQueue.Enqueue(childrenNode);
                    cost[childrenNode] = cost[parent] + 6;
                    Console.WriteLine(parent + " - " + childrenNode + " - " + cost[childrenNode]);
                }
            }
        }
      return cost;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int q = Convert.ToInt32(Console.ReadLine());

        for (int qItr = 0; qItr < q; qItr++) {
            string[] nm = Console.ReadLine().Split(' ');

            int n = Convert.ToInt32(nm[0]);

            int m = Convert.ToInt32(nm[1]);

            int[][] edges = new int[m][];

            for (int i = 0; i < m; i++) {
                edges[i] = Array.ConvertAll(Console.ReadLine().Split(' '), edgesTemp => Convert.ToInt32(edgesTemp));
            }

            int s = Convert.ToInt32(Console.ReadLine());

            int[] result = bfs(n, m, edges, s);

            textWriter.WriteLine(string.Join(" ", result.Where(x => x!=0)));
        }

        textWriter.Flush();
        textWriter.Close();
    }
}