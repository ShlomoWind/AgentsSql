from enum import Enum

class Status(Enum):
    Active = "Active"
    Injured = "Injured"
    Missing = "Missing"
    Retired = "Retired"

class Agent:
    def __init__(self,code_name:str,real_name:str,location,status:Status,missions_completed:int,agent_id:int = None):
        self.id = agent_id
        self.codeName = code_name
        self.realName = real_name
        self.location = location
        self.status = status
        self.missionsCompleted = missions_completed

    def __str__(self):
        return f"id: {self.id} \ncode name: {self.codeName} \nreal name: {self.realName} \nlocation: {self.location} \nstatus: {self.status} \nmissions completed: {self.missionsCompleted}"
