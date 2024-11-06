#include"Simulated_Annealing.h"
#include<vector>
#include<string>
#include<iostream>
#include<ctime>
using namespace std;
std::string filedir("../data/");
std::string files[16] = {"input_group678.txt", "input_group679.txt", "input_group680.txt", "input_group684.txt", "input_group687.txt", "input_group689.txt", "input_group690.txt", "input_group691.txt", "input_group692.txt", "input_group695.txt", "input_group701.txt", "input_group702.txt", "input_group705.txt", "input_group707.txt", "input_group709.txt"};
int main(){
    Graph g;
    Simulated_Annealing SA;
    for(int i=0;i<16;++i){
        std::string filename = filedir+files[i];
        g.getInput(filename.c_str());
        //g.print();
        SA.setGraph(&g);
        clock_t start,end;
        std::cout<<filename<<" Running"<<std::endl;
        start = clock();
        SA.run();
        std::cout<<"best result:"<<SA.getResult()<<std::endl;
        end = clock();
        std::cout<<"total running time: "<<(double)(end-start)/CLOCKS_PER_SEC<<std::endl;
        std::cout<<"--------------------------"<<std::endl;
        g.clear();
    }
    return 0;
};