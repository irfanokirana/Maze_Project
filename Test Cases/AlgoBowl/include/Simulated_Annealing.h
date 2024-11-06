#include<math.h>
#include<vector>
#include"Graph.h"
#include"Solution.h"
#include"Union_Find_Set.h"
class Simulated_Annealing{
    private:
        const long int Tmax=(10000),Tmin=1;
        int Evaluationfunc(Solution& s);
        int cooldown(int T); //cool down function
        unsigned int equilibrium = 200;
        Graph* g;
        int bestres;
    public:
        void setGraph(Graph* g){this->g=g;}
        void run();
        int getResult(){return bestres;};
};