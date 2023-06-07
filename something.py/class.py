
class character:
    def __init__(self):
        self.result = 0
    
    def hp(self,num):
        self.result = 20* num 
        return self.result

    def atk(self, num):
        self.result = 5 * num 
        return self.result

    def dfn(self, num):
        self.result =  5 * num
        return self.result
    
    def dex(self, num):
        self.result = 5 * num
        return self.result

zombie = character()
skeleton = character()

stat_zombie = [zombie.hp(4), zombie.atk(5), zombie.dfn(5), zombie.dex(1) ]

stat_skeleton = [skeleton.hp(2), skeleton.atk(8), skeleton.dfn(1), skeleton.dex(4) ]

print(stat_zombie)
print(stat_skeleton)