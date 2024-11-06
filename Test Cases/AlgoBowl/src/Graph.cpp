#include "Graph.h"
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool Graph::getInput(const char* filename){
    //Open file stream
    ifstream inputFile(filename);

    //Handle file IO error
    if (!inputFile.is_open()) {
        cerr << "Error: Unable to open input file." << endl;
        return 1;
    }

    //If already processed
    if(isread){
        return false;
    }

    //Get nodes edges and terminals
    inputFile >> numNodes >> numEdges >> numTerminals;
    //cout << numNodes << numEdges << numTerminals << endl;

    //Initialize the graph and edges
    graph = new int*[numNodes];
    for(int i=0;i<numNodes;++i){
        graph[i] = new int[numNodes];
    }
    for(int i=0;i<numNodes;++i)
        for(int j=0;j<numNodes;++j)
            graph[i][j]=INF;
    edges = new Edge [numEdges];

    //Get terminals
    terminals = new int[numTerminals];
    for (int i = 0; i < numTerminals; ++i) {
        inputFile>>terminals[i];
        --terminals[i];
    }

    //Read edges
    for(int i=0;i<numEdges;++i){
        inputFile >> edges[i].from >> edges[i].to >> edges[i].weight;
        --edges[i].from;
        --edges[i].to;
        graph[edges[i].from][edges[i].to] = edges[i].weight;
        graph[edges[i].to][edges[i].from] = edges[i].weight;
    }

    inputFile.close();
    isread=true;
    return true;
};

Graph::~Graph(){
    if(isread) clear();
};

void Graph::clear(){
    if(!isread) return;
    isread=false;
    for(int i=0;i<numNodes;++i)
        delete[] graph[i];
    delete[] graph;
    delete[] terminals;
};

void Graph::getEdges(bool* nodes,std::set<Edge>& set){
    for(int i=0;i<numEdges;++i){
        bool a=false,b=false;
        a = (nodes[edges[i].to]);
        b = (nodes[edges[i].from]);
        if(a&&b) set.insert(edges[i]);
    }
};

void Graph::print(){
    printf("Graph:\n");
    printf("nodenum: %d\n",numNodes);
    for(int i=0;i<numNodes;++i){
        for(int j=0;j<numNodes;++j){
            if(graph[i][j]==INF) printf("-1 "); 
            else printf("%d ",graph[i][j]);
        }
        printf("\n");
    }
    printf("Edegs:\n");
    for(int i=0;i<numEdges;++i) printf("%d %d %d\n",edges[i].from+1,edges[i].to+1,edges[i].weight);
    printf("Terminals:\n");
    for(int i=0;i<numTerminals;++i) printf("%d ",terminals[i]+1);
    printf("\n");
};
void Graph::getGraphCopy(int**& g){
    g = new int*[numNodes];
    for(int i=0;i<numNodes;++i){
        g[i] = new int[numNodes];
    }
    for(int i=0;i<numNodes;++i)
        for(int j=0;j<numNodes;++j)
            g[i][j]=graph[i][j];
};
void Graph::freeGraph(int** g){
    for(int i=0;i<numNodes;++i)
        delete[] g[i];
    delete[] g;
};