f = open("MPD.csv", "r").read()
ft = f.replace(",,", "\n")
p = open("MPDD.csv", "w")
p.write(ft)
p.close()