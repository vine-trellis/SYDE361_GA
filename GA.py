from Note import *
from Composition import *
from Fitness import *
from random import randrange, uniform

# This class is the genetic algorithm controller. The only interface function is 'runGA', which inputs
# the initial composition, number of iterations, and outputs the genetically imporved algorithm.
class GA:
    def runGA(self, baseTrack, iterations):
        # inital run
        print("Running the genetic algorithm.")
        firstGeneration = [baseTrack] * 8 # copies 8 versions of the Composition object
        mutatedGeneration = self.mutate(firstGeneration, 0.8)
        highestFitnessComp = baseTrack
        highestFitnessComp.fitness = 0
        for _ in range(iterations):
            fitnessedGeneration = list(map(self.addFitnessToComposition, mutatedGeneration))
            sortedFitnessedGeneration = self.sortGenerationByFitness(fitnessedGeneration)
            highestFitnessComp = max(sortedFitnessedGeneration + [highestFitnessComp], key=lambda x: x.getFitness())
            fittestGeneration = self.eliminateUnfitCandidates(sortedFitnessedGeneration)
            mutatedGeneration = self.mutate(fittestGeneration, 0.8)
        finalGen = self.sortGenerationByFitness(fitnessedGeneration)
        print("Done.")
        chosenCandidate =  max(finalGen + [highestFitnessComp], key=lambda x: x.getFitness())
        print(f"Chosen candidate fitness: {chosenCandidate.getFitness()}")
        return chosenCandidate

    def addFitnessToComposition(self, comp):
        compFitness = Fitness.determineFitness(comp)
        comp.setFitness(compFitness)
        return comp

    # Get rid of the bottom half unfit generations.
    def eliminateUnfitCandidates(self, generation):
        return generation[:len(generation)//2] + generation[:len(generation)//2]

    def mutate(self, generation, mutationProbability):
        mutatedGeneration = [] # store the mutated candidates
        for candidate in generation: # go through each of the 8 candidate Composition objects
            if uniform(0, 1) < mutationProbability: # mutate XX% of this generation
                mutatedGeneration.append(self.mutateCandidate(candidate, mutationProbability))
            else: # rotate candidate
                continue
                mutatedGeneration.append(self.rotateCandidate(candidate)) # rotate candidate
        return mutatedGeneration
        
    def mutateCandidate(self, candidate, mutationProbability):
        newNotes = [] # list containing the new notes for the specific composition
        for i, note1 in enumerate(candidate.notes): # each note is a Note object
            newNote = note1
            for j, note2 in enumerate(candidate.notes):
                if j >= i:
                    continue
                if uniform(0,1) < (mutationProbability / 2): # randomly change 40% of notes.
                    newNote += randrange(1,10)
            newNotes.append(newNote)
        return Composition(newNotes)

    def rotateCandidate(self, candidate):
        oldNotes = candidate.notes
        rotationIndex1 = randrange(0, 8) # rotate once
        tempNotes = oldNotes[rotationIndex1:] + oldNotes[:rotationIndex1]
        rotationIndex2 = randrange(0, 8) # rotate twice
        newNotes = tempNotes[rotationIndex2:] + tempNotes[:rotationIndex2]
        return Composition(newNotes)

    def sortGenerationByFitness(self, generation):
        return sorted(generation, key=lambda x: x.getFitness(), reverse=True)

