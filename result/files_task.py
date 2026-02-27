def store(filename,stuname,total,pers):
    file = open(filename,"w")
    file.write(f"Student Name {stuname}")
    file.write(f"Total mark {total}")
    file.write(f"Student pers {pers}")
    file.close()
        