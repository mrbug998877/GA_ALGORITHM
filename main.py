import random
from operator import itemgetter


class Gene:
    def __init__(self,**data):
        self.__dict__.update(data)
        self.size = len(data['data'])#length of gene

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
        self.pop = pop
        self.bestindividual = self.selectBest(self.pop)

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
    def selection(self,individuals,k):
        s_inds = sorted(individuals,key=itemgetter,reverse=True)
        sum_fits = sum(ind['fitness'] for ind in individuals)

        chosen = []
        for i in range (k):
            u = random.random()*sum_fits
            sum_ = 0
            for ind in s_inds:
                sum_ += ind['fitness']
                if sum_ >= u:
                    chosen.append(ind)
                    break
        chosen = sorted(chosen,key=itemgetter("fitness"),reverse=False)
        return chosen

    def crossoperate(self,offspring):
        dim = len(offspring[0]['Gene'].data)

        geneinfo1 = offspring[0]['Gene'].data
        geneinfo2 = offspring[1]['Gene'].data

        if dim ==1:
            pos1 = 1
            pos2 = 1
        else:
            pos1 = random.randrange(1,dim)
            pos2 = random.randrange(1,dim)
        newoff1 = Gene(data=[])
        newoff2 = Gene(data=[])

        temp1 = []
        temp2 = []
        for i in range (dim):
            if min(pos1,pos2) <= i < max(pos1,pos2):
                temp2.append(geneinfo2[i])
                temp1.append(geneinfo1[i])
            else:
                temp2.append(geneinfo1[i])
                temp1.append(geneinfo2[i])
        newoff1.data = temp1
        newoff2.data = temp2
        return  newoff1,newoff2

    def mutation(self, crossoff, bound):
        dim = len(crossoff.data)
        if dim == 1:
            pos = 0
        else:
            pos = random.randrange(0,dim)
        crossoff.data[pos] = random.randint(bound[0][pos],bound[1][pos])
        return crossoff

    def GA_main(self):
        popsize = self.parameter[3]
        print("start of evolution")
        for g in range(NGEN):
            print("############## Generation {} ################".format(g))

            selectpop = self.selection(self.pop, popsize)

            nextoff = []
            while len(nextoff) != popsize:
                #apply crossover and mutation on the offspring

                #select two individuals
                offspring = [selectpop.pop() for _ in range (2)]

                if random.random() < CXPB:#cross two individuals with probability CXPB
                    crossoff1, crossoff2 = self.crossoperate(offspring)
                    if random.random() < MUTPB:
                        muteoff1 = self.mutation(crossoff1,self.bound)
                        muteoff2 = self.mutation(crossoff2,self.bound)
                        fit_muteoff1 = self.evaluate(muteoff1.data)
                        fit_muteoff2 = self.evaluate(muteoff2.data)
                        nextoff.append({'Gene':muteoff1,'fitness':fit_muteoff1})
                        nextoff.append({'Gene':muteoff2,'fitness':fit_muteoff2})
                    else:
                        fit_muteoff1 = self.evaluate(crossoff1.data)
                        fit_muteoff2 = self.evaluate(crossoff2.data)
                        nextoff.append({'Gene':crossoff1,'fitness':fit_muteoff1})
                        nextoff.append({'Gene':crossoff2,'fitness':fit_muteoff2})
                else:
                    nextoff.extend(offspring)
                #The population is entirely replaced by the offspring
                self.pop = nextoff

                fits = [ind['fitness'] for ind in self.pop]

                best_ind = self.selectBest(self.pop)

                if best_ind['fitness'] > self.bestindividual['fitness']:
                    self.bestindividual = best_ind
                print("Best individual found is {},{}".format(self.bestindividual['Gene'].data,
                                                              self.bestindividual['fitness']))

                print(" Max fitness of current pop: {}".format(max(fits)))
            print("--------End of (successful) evolution")
if __name__ == "__main__":




