# set operation program in python

# defining sets for program
E = {1, 3, 5, 7, 9, 0};
N = {0, 2, 4, 6, 8, 10};

#union of sets
print("Union of sets - E and N is",E | N)

#intersection of sets
print("Intersection of sets - E and N is", E & N)

#difference of sets
print("Difference of sets - E and N is", E - N)

#symmetric difference of sets
print("Symmetric difference of sets - E and N is", E ^ N)
