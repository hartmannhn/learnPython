prdgen.py  
by @hartmannhn
- used to produce graph which plot actual chance of proc from base proc chance
- made with Python 3.7.4 (x64)
- learning plotting with matplotlib, using numpy, random, and progressbar
- learning using classes, functions, setting default parameters, and make a habit to place comments or documentation
- best viewed through cmd window (progress bar looks weird in IDLE)

what is PRD?  
- abbreviated from pseudo-random distribution 
- simply put, an attempt to prevent streak of luck/bad luck by increasing chance of happening with each  not-happening instance (start at smaller chance) instead of relying to internal random number generator which deemed prone to "streak of luck/bad luck"

how it is done?  
by performing 10.000 instances check for each base proc chance, increasing chance with its base proc chance.  
each proc reset chance back into base proc chance and starts again until number of instances check runs out.  
the actual chance value is estimated from number of procs / number of instances check.

input required
- none

output
line graph displaying base proc chance to actual proc chance based on pseudo-random distribution

future-update-plan  
- add prompt to save result graph into .jpg

v1.0  (2019/08/22)
- now has progressbar which display how long until process finished
- added graph smoothing for better result viewing
- now uses classes and functions instead of looping through whole list
