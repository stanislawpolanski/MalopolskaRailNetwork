class OnChangePrinter:
    totalSteps = 0
    stepsMade = 0

    def __init__(self, totalStepsNumber):
        self.totalSteps = totalStepsNumber

    def StepMade(self):
        self.stepsMade += 1
        print('Step number made:', self.stepsMade, 'of', self.totalSteps)

#test
x = OnChangePrinter(5)
x.StepMade()
x.StepMade()