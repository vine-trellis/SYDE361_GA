from Note import *
from Composition import *
from MetricManager import *
from GA import *
import numpy as np
from random import randrange, uniform

baseFreq = 440
A4 = Note(baseFreq, "A4")
A4sh = Note(baseFreq * 2 ** (1 / 12), "A4#")
B4 = Note(baseFreq * 2 ** (2 / 12), "B4")
C4 = Note(baseFreq * 2 ** (3 / 12), "C4")
C4sh = Note(baseFreq * 2 ** (4 / 12), "C4#")
D4 = Note(baseFreq * 2 ** (5 / 12), "D4")
D4sh = Note(baseFreq * 2 ** (6 / 12), "D4#")
E4 = Note(baseFreq * 2 ** (7 / 12), "E4")
F4 = Note(baseFreq * 2 ** (8 / 12), "F4")
F4sh = Note(baseFreq * 2 ** (9 / 12), "F4#")
G4 = Note(baseFreq * 2 ** (10 / 12), "G4")
G4sh = Note(baseFreq * 2 ** (11 / 12), "G4#")
A5 = Note(baseFreq * 2 ** ((12) / 12), "A5#")
A5sh = Note(baseFreq * 2 ** ((1 + 12) / 12), "A5#")
B5 = Note(baseFreq * 2 ** ((2 + 12) / 12), "B5")
C5 = Note(baseFreq * 2 ** ((3 + 12) / 12), "C5")
C5sh = Note(baseFreq * 2 ** ((4 + 12) / 12), "C5#")
D5 = Note(baseFreq * 2 ** ((5 + 12) / 12), "D5")
D5sh = Note(baseFreq * 2 ** ((6 + 12) / 12), "D5#")
E5 = Note(baseFreq * 2 ** ((7 + 12) / 12), "E5")
F5 = Note(baseFreq * 2 ** ((8 + 12) / 12), "F5")
F5sh = Note(baseFreq * 2 ** ((9 + 12) / 12), "F5#")
G5 = Note(baseFreq * 2 ** ((10 + 12) / 12), "G5")
G5sh = Note(baseFreq * 2 ** ((11 + 12) / 12), "G5#")

selectedTrack1 = [C4, G4, A5, A5sh, F4, E5, D4, C4]
# selectedTrack2 = [E, D, C, D, E, E, D, D]
# selectedTrack3 = [F, A, D, D, G, E, A, C]

times = MetricManager.timeCall(GA().runGA, selectedTrack1, 10, 10)
MetricManager.writeResultsToCSV("GA_timings_10_iterations_8_notes", times)
