import subprocess
import numpy as np

ig = np.load("to_ignore_dependencies.npy")

ig_arg = []
for i in ig :
    ig_arg.append("--exclude")
    ig_arg.append(i)

# print(ig_arg)

write_arg = [">","requirements.txt"]

a = subprocess.run(["pip","freeze"] + ig_arg + write_arg, shell=True)

print(a)
