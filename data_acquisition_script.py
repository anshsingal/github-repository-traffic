import sys
print("inline arguments are:")
print("\n".join(sys.argv))

import os
print(os.environ['TOKEN'])


f = open("temp_clones.txt", "r")
print(f.read())
