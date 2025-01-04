class Solution {
    /**
     * Find the redundant connection in a graph
     * Using Union-Find algorithm to detect cycles
     */
    public int[] findRedundantConnection(int[][] edges) {
        // Initialize parent array for Union-Find
        int n = edges.length;
        int[] parent = new int[n + 1];
        int[] rank = new int[n + 1];
        
        // Initialize each node as its own parent
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
        
        // Process each edge
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            
            // If nodes are already in the same set, we found our cycle
            if (!union(parent, rank, u, v)) {
                return edge; // This is the redundant edge
            }
        }
        
        return new int[0]; // Should never reach here given the problem constraints
    }
    
    /**
     * Find the root parent of a node with path compression
     */
    private int find(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = find(parent, parent[x]); // Path compression
        }
        return parent[x];
    }
    
    /**
     * Union two sets by rank
     * Returns false if already connected (cycle detected)
     */
    private boolean union(int[] parent, int[] rank, int x, int y) {
        int rootX = find(parent, x);
        int rootY = find(parent, y);
        
        // If roots are the same, adding this edge would create a cycle
        if (rootX == rootY) {
            return false;
        }
        
        // Union by rank to keep the tree balanced
        if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        } else if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        } else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
        
        return true;
    }
}
