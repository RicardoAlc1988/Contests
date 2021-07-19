using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    
    
    
    static int INFINITE = Int32.MaxValue;
    static int NILL = 0;
    
    public struct Client
    {
        public int idx, area, prize, nill_id;

        public Client(int p_idx, int p_area, int p_prize)
        {
            idx = p_idx;
            area = p_area;
            prize = p_prize;
            nill_id = 0;
        }
    }
    
    public struct House
    {
        public int idx, area, prize, nill_id;

        public House(int p_idx, int p_area, int p_prize)
        {
            idx = p_idx;
            area = p_area;
            prize = p_prize;
            nill_id = 0;
        }
    } 
    
    static int max(int n, int m) {
        if(n>m) return n;
        else return m;
    }
    
    static List<int>[] buildGraph(int n, int m,IEnumerable<Client> clients, IEnumerable<House> houses) {
        List<int>[] graph = new List<int>[n+1];
        IEnumerable<int> relatedHouses;
        for(int i=0; i<=n; i++) {
            graph[i] = new List<int>();
        }
        
        var query = from client in clients 
                      join house in houses 
                      on client.nill_id equals house.nill_id 
                      where client.area <= house.area
                         && client.prize >= house.prize
                      select new { cIndex = client.idx, hIndex =  house.idx };
        
        var agroupedData = query.GroupBy(x => x.cIndex)
                                .Select(y => new {cIndex = y.Key, 
                                                  rHouses = y.ToList()}
                                        );
        foreach(var x in agroupedData) {
            graph[x.cIndex].AddRange(x.rHouses.Select(y => y.hIndex));
        }
        
        return graph;
        
    }
    
    static bool bfs(List<int>[] graph, int[] pairU, int[] pairV, int[] dist) {
        Queue<int> queue = new Queue<int>();
        int u;
        for(int i=1; i<pairU.Length; i++) {
            // free vertex are marked
            if(pairU[i]==NILL) {
                dist[i]=0;
                queue.Enqueue(i);
            }
            
            else dist[i]=INFINITE;
        }
        
        dist[NILL] = INFINITE;
        
        while(queue.Any()) {
            u = queue.Dequeue();
            
            if(dist[u] < dist[NILL]) {
                foreach(int v in graph[u]) {
                    // edge not yet considered
                    if(dist[pairV[v]] == INFINITE) {
                        dist[pairV[v]] = dist[u] + 1;
                        queue.Enqueue(pairV[v]);
                    }
                }
            }
        }
        
        //  an augmenting path has been founded
        return dist[NILL] != INFINITE;
    }
    
    
    static bool dfs(int u, List<int>[] graph, int[] pairU, int[] pairV, int[] dist) {
        if(u != NILL) {
          foreach(int v in graph[u]) {
            if(dist[pairV[v]] == dist[u]+1) {
               if(dfs(pairV[v], graph, pairU, pairV, dist)) {
                        pairV[v] = u;
                        pairU[u] = v;
                        return true;
                    }
                }
          }
          dist[u]=INFINITE;
          return false;
        }
        return true;
  }
    
    

    static int realEstateBroker(int n, int m, List<Client> clients, List<House> houses) {
        int[] pairU = new int[n+1];
        int[] pairV = new int[m+1];
        int[] dist = new int[n+1];
 
        for (int u=0; u<n; u++)
            pairU[u] = NILL;
        for (int v=0; v<m; v++)
            pairV[v] = NILL;

        int result = 0;
        
        List<int>[] graph = buildGraph(n, m,clients, houses);
        
        while(bfs(graph, pairU, pairV, dist)) {
            for(int u=1; u<=n; u++) {
                if(pairU[u]==NILL && dfs(u, graph, pairU, pairV, dist)) {
                    result++;
                }
            }
        }
        
        return result;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);
        
        string[] nm = Console.ReadLine().Split(' ');

        int n = Convert.ToInt32(nm[0]);

        int m = Convert.ToInt32(nm[1]);

        List<Client> clients = new List<Client>();
    
        int idx;
        int[] clientData;
        for (int clientsRowItr = 0; clientsRowItr < n; clientsRowItr++) {
            idx=clientsRowItr;
            clientData = Array.ConvertAll(Console.ReadLine().Split(' '), clientsTemp => Convert.ToInt32(clientsTemp));
            clients.Add(new Client(++idx, clientData[0], clientData[1]));
        }

        List<House> houses = new List<House>();
        int[] houseData;
        for (int housesRowItr = 0; housesRowItr < m; housesRowItr++) {
            idx=housesRowItr;
            houseData = Array.ConvertAll(Console.ReadLine().Split(' '), housesTemp => Convert.ToInt32(housesTemp));
            houses.Add(new House(++idx, houseData[0], houseData[1]));
            
        }

    int result = realEstateBroker(n, m, clients, houses);
    

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}