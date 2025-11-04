class Stadt:
    staedte_insgesammt= 0

    def __init__(self, name, region, localtime, temp_c):
        self.name = name
        self.region = region
        self.localtime = localtime
        self.temp_c = temp_c
        Stadt.staedte_insgesammt+=1
    

