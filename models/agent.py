from enum import Enum

class Status(Enum):
    Active = "Active"
    Injured = "Injured"
    Missing = "Missing"
    Retired = "Retired"

class Agent:
    def __init__(self,codeName:str,realName:str,location,status:Status,missionsCompleted:int,id:int = None):
        self.id = id
        self.codeName = codeName
        self.realName = realName
        self.location = location
        self.status = status
        self.missionsCompleted = missionsCompleted

    def __str__(self):
        return f"id: {self.id} \ncode name: {self.codeName} \nreal name: {self.realName} \nlocation: {self.location} \nstatus: {self.status} \nmissions completed: {self.missionsCompleted}"
