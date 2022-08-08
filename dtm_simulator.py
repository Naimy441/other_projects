import sys, copy, numpy, math, random, time

'''
We need to work out the formulas for the State class:

The number of births in a population should be determined by
(1) the current population,
(2) the development variables,
(3) the birth causes and preventions (which is not completely outlined),
(4) a small random element.

The number of deaths in a population should be determined by
(1) the current population,
(2) the development variables,
(3) the death causes (which is already outlined),
(4) a small random element.

We can create 5 pre-made settings for the development variables that
generally portray each stage of the DTM.

Possible new ideas to implement:
(1) Global events, such as wars and pandemics
(2) ...
'''

def framework():
    initialize()
    conduct()

#prepare variables and ask user for various things
def initalize():
    print("Welcome User.")

def autoGenerateStates(numOfStates, population_range = (500, 1000)):
    statesList = []
    for i in range(numOfStates):
        state = State(random.randint(population_range[0], population_range[1])
        statesList.append(state)
    return statesList

def manuallyGenerateStates(numOfStates):
    for i in range(numOfStates):
        starting_population = int(input("Enter Initial Population: "))
        dev_vars = {}
        dev_vars_edit_mode = input("Would you like to edit the development variables? (y/n): ")
        if dev_vars_edit_mode == "y":
            while True:
                print("economic_dev, political_dev, technological_dev, social_dev")
                edit_dev_var = input("'Enter one of the above development variables: ")
                #add more code to manually input development variables that the user would like to change

        state = State(starting_population, dev_vars)

def iterate(iterations):
    for i in range(iterations):
        pass

class State:
    def __init__(self, starting_population = 0, dev_vars = {}):
        self.populationsList = [starting_population]
        self.dev_vars = dev_vars
        seld.birth_causes = {}
        self.death_causes = {}

    def initVariables():
        #randomly generates development variables if user did not manually input them in
        dev_vars.setdefault('economic_dev', random.uniform(0.00, 1.00, 2))
        dev_vars.setdefault('political_dev', random.uniform(0.00, 1.00, 2))
        dev_vars.setdefault('technological_dev', random.uniform(0.00, 1.00, 2))
        dev_vars.setdefault('social_dev', random.uniform(0.00, 1.00, 2))

        #replace None with equation that defines a birth cause or prevention; use development variables
        birth_causes['placeholder1'] = None
        birth_causes['placeholder2'] = None
        birth_causes['placeholder3'] = None
        birth_causes['fertility_rate'] = None

        #replace None with equation that defines death_cause; use development variables
        death_causes['medical_issues'] = None
        death_causes['environment'] = None
        death_causes['human_induced'] = None
        death_causes['politics'] = None
        death_causes['natural_aging'] = None

    def updateVariables():
        #after the function development variables define the death causes and the next population is calculated
        #then updates the development variables based on their biases
        #also updates death_causes based on the updates to the development variables
        pass

    def calculateNextPopulation():
        #this function will calculate the next population based on
        #development vars, birth_causes, death_causes, and possible other values

        def calculateBirths():
            #replace None with equation that calculates births
            return None

        def calculateDeaths():
            #replace None with equation that calculates deaths
            return None

        def calculateMigrations():
            #replace None with equation that calculates the number of people who left and came to the state
            return None

        nextPopulation = prevPopulationsList[-1] + calculateBirths() + calculateDeaths() + calculateMigrations()
        populationsList.append(nextPopulation)
        return nextPopulation
