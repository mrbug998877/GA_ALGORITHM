import random
import random
from operator import itemgetter


class Gene:
    def __init__(self,**data):
        self.__dict__.update(data)
        self.size = len(data['data'])#length of gene
        # print("length of gene is %d" % self.size)

class GA:
    def __init__(self,parameter):
        #parameter = [CXPB(交叉概率), MUTPB(变异概率), NGEN(代数), popsize, low, up]
        self.parameter = parameter
        low = self.parameter[4]
        up = self.parameter[5]
        self.bound = []
        self.bound.append(low)
        self.bound.append(up)

        pop = []
        for i in range (self.parameter[3]):
            geneinfo = []
            for pos in range(len(low)):
                geneinfo.append(random.randint(self.bound[0][pos],self.bound[1][pos]))#initialize poppulation

            fitness = self.evaluate(geneinfo)#evaluate each chromosome
            pop.append({'Gene':Gene(data=geneinfo),'fitness':fitness})

            # print(geneinfo)
            # print(len(pop))

            print(Gene(data=geneinfo).data)
        self.pop = pop
        s_inds = sorted(pop, key=itemgetter("fitness"), reverse=True)
        self.bestindividual = self.selectBest(self.pop)

        # print(self.pop )

    def evaluate(self,geneinfo):
        x1 = geneinfo[0]
        x2 = geneinfo[1]
        x3 = geneinfo[2]
        x4 = geneinfo[3]
        y = x1**2 + x2**2 + x3**3 + x4**4
        return y
    def selectBest(self,pop):
        s_inds = sorted(pop,key=itemgetter("fitness"),reverse=True)
        return s_inds[0]
if __name__ == "__main__":
    CXPB, MUTPB, NGEN, popsize = 0.8, 0.1, 1000, 100  # popsize must be even number

    up = [30, 30, 30, 30]  # upper range for variables
    low = [1, 1, 1, 1]  # lower range for variables
    parameter = [CXPB, MUTPB, NGEN, popsize, low, up]
    run = GA(parameter)
    u = random.random()
    # print(u)
    newoff1 = Gene(data=[])
    # print(newoff1.data)
    #run.GA_main()