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

    public struct nodeStructure
    {
        public int nNodesPending, nRelatedComponent;
        public bool isRootRelatedParComponent;
    }
    
    static int maxEdges(int treeNodes, List<int>[] graph, nodeStructure[] nodesInfo) {
        bool[] markedNodes = new bool[treeNodes];
        Array.Clear(markedNodes, 0, markedNodes.Length);
        for(int node=0; node<treeNodes;node++) {
            if(!markedNodes[node]) dsf(node, markedNodes, graph, nodesInfo);
        }
        return nodesInfo[0].nRelatedComponent-1;
    }
    
    static void dsf(int node, bool[] marked, List<int>[] graph, nodeStructure[] nodesInfo) {
        int nNodesPending, nRelatedComponent;
        nNodesPending = 1;
        nRelatedComponent = 0;
        marked[node] = true;
        // root case
        if(!graph[node].Any()) {
            nodesInfo[node].nNodesPending = 1;
            nodesInfo[node].nRelatedComponent = 0;
            nodesInfo[node].isRootRelatedParComponent = false;
        }
        // general case
        foreach(int childrenNode in graph[node]) {
            if(!marked[childrenNode]) {
                dsf(childrenNode, marked, graph, nodesInfo);
                if(!nodesInfo[childrenNode].isRootRelatedParComponent) {
                    nNodesPending += nodesInfo[childrenNode].nNodesPending;
                }
                nRelatedComponent += nodesInfo[childrenNode].nRelatedComponent;
            }
        }
        nodesInfo[node].nNodesPending = nNodesPending;
        nodesInfo[node].nRelatedComponent = nRelatedComponent;
        if(nNodesPending%2==0) {
          nodesInfo[node].isRootRelatedParComponent = true;
          nodesInfo[node].nRelatedComponent++;
        } 
        /*
        Console.WriteLine("node: " + node
                        + "nNodesPending: " + nodesInfo[node].nNodesPending
                        + "nRelatedComponent:" + nodesInfo[node].nRelatedComponent
                        + "isRootRelatedParComponent" + nodesInfo[node].isRootRelatedParComponent);
                        */
    }
    
    
    static List<int>[] buildGraph(int treeNodes, int treeEdges, int[] treeFrom, int[] treeTo, nodeStructure[] nodesInfo) {
        List<int>[] graph  = new List<int>[treeNodes];
        for(int i=0; i<treeNodes; i++) { 
            nodesInfo[i] = new nodeStructure();
            graph[i] = new List<int>();
        }
        
        for(int j=0; j<treeEdges; j++) {
            graph[treeFrom[j]-1].Add(treeTo[j]-1);
            graph[treeTo[j]-1].Add(treeFrom[j]-1);
        }
        return graph;
    }

    static void Main(string[] args) {
        string[] treeNodesEdges = Console.ReadLine().Split(' ');
        int treeNodes = Convert.ToInt32(treeNodesEdges[0]);
        int treeEdges = Convert.ToInt32(treeNodesEdges[1]);

        int[] treeFrom = new int[treeEdges];
        int[] treeTo = new int[treeEdges];

        for (int i = 0; i < treeEdges; i++) {
            string[] treeFromTo = Console.ReadLine().Split(' ');
            treeFrom[i] = Convert.ToInt32(treeFromTo[0]);
            treeTo[i] = Convert.ToInt32(treeFromTo[1]);
        }
        nodeStructure[] nodesInfo = new nodeStructure[treeNodes];
        List<int>[] graph = buildGraph(treeNodes, treeEdges, treeFrom, treeTo, nodesInfo);
        int maxNumbreEddges = maxEdges(treeNodes, graph, nodesInfo);
        Console.WriteLine(maxNumbreEddges);
        // Write your code here.
    }
}