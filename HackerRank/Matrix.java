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
    
    static int INFINITE = Int32.MaxValue;

    class Node {
        
        private int adyacentNode, cost;
        
        public Node(int p_adyacentNode, int p_cost) {
            adyacentNode = p_adyacentNode;
            cost = p_cost;
        }
        
        
        public int AdyacentNode
        {
            get
            {
                return adyacentNode;
            }
            set
            {
                adyacentNode = value;
            }
        }
        
        public int Cost
        {
            get
            {
                return cost;
            }
            set
            {
                cost = value;
            }
        }
        
    }
    
    class NodeTree {
        private int cutOffCost, minEdge;
        private bool hashMachine;
        
        public NodeTree(bool isMachine) {
            minEdge = INFINITE;
            hashMachine = isMachine;
        }
        
        public int CutOffCost
        {
            get
            {
                return cutOffCost;
            }
            set
            {
                cutOffCost = value;
            }
        }
        
        public int MinEdge
        {
            get
            {
                return minEdge;
            }
            set
            {
                minEdge = value;
            }
        }
        
        public bool HashMachine
        {
            get
            {
                return hashMachine;
            }
            set
            {
                hashMachine = value;
            }
        }
        
    }
    
    // Complete the minTime function below.
    static int minTime(int n, int k, int[][] roads, int[] machines) {
        List<Node>[] graph = buildGraph(n, k, roads);
        bool[] isMachine = new bool[n];
        for(int i=0; i<k; i++) isMachine[machines[i]] = true;
        return dfs_launcher(n, isMachine, graph);
    }
    
    static int dfs_launcher(int n, bool[] isMachine, List<Node>[] graph) {
        bool[] markedNodes = new bool[n];
        NodeTree[] nodeTrees = new NodeTree[n];
        for(int v=0; v<n; v++) dfs(v, isMachine, markedNodes, nodeTrees, graph);
        return nodeTrees[0].CutOffCost;
    }
    
    static int min(int a, int b) {
        if(a<b) return a;
        return b;
    }
    
    static void dfs(int v, bool[] isMachine, bool[] markedNodes, NodeTree[] nodeTrees, List<Node>[] graph) {
        markedNodes[v] = true;
        nodeTrees[v] = new NodeTree(isMachine[v]);
        int minEdge;
        foreach(Node node in graph[v]) {
            if(!markedNodes[node.AdyacentNode]) {
                 dfs(node.AdyacentNode, isMachine, markedNodes, nodeTrees, graph);
                // Merge nodes operation
                if(nodeTrees[node.AdyacentNode].HashMachine) {
                        nodeTrees[v].CutOffCost += nodeTrees[node.AdyacentNode].CutOffCost;
                        minEdge = min(nodeTrees[node.AdyacentNode].MinEdge, node.Cost);
                        if(nodeTrees[v].HashMachine) {
                        if(minEdge < nodeTrees[v].MinEdge) {
                            nodeTrees[v].CutOffCost += minEdge;
                        }
                        else {
                            nodeTrees[v].CutOffCost += nodeTrees[v].MinEdge;
                            if(!isMachine[v]) nodeTrees[v].MinEdge = minEdge;
                        }
                    }

                    else if(!isMachine[v]) {
                        nodeTrees[v].HashMachine = true;
                        nodeTrees[v].MinEdge = minEdge;
                    }
                }
            }
        }
           
    } 
    
    
    static List<Node>[] buildGraph(int n, int k, int[][] roads) {
        List<Node>[] graph = new List<Node>[n];
        for(int i=0; i<n; i++) {
            graph[i] = new List<Node>();
        }
        
        for(int i=0; i<n-1; i++) {
            graph[roads[i][0]].Add(new Node(roads[i][1], roads[i][2]));
            graph[roads[i][1]].Add(new Node(roads[i][0], roads[i][2]));
        }
        return graph;
    }


    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string[] nk = Console.ReadLine().Split(' ');

        int n = Convert.ToInt32(nk[0]);

        int k = Convert.ToInt32(nk[1]);

        int[][] roads = new int[n - 1][];

        for (int i = 0; i < n - 1; i++) {
            roads[i] = Array.ConvertAll(Console.ReadLine().Split(' '), roadsTemp => Convert.ToInt32(roadsTemp));
        }

        int[] machines = new int [k];

        for (int i = 0; i < k; i++) {
            int machinesItem = Convert.ToInt32(Console.ReadLine());
            machines[i] = machinesItem;
        }

        int result = minTime(n, k, roads, machines);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
