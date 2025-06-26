from enum import Enum

class Status(Enum):
    Active = "Active"
    Injured = "Injured"
    Missing = "Missing"
    Retired = "Retired"

class Agent:
    def __init__(self,code_name:str,real_name:str,location,status:Status,missions_completed:int,agent_id:int = None):
        self.agent_id = agent_id
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_completed

    def __str__(self):
        return f"id: {self.agent_id} \ncode name: {self.code_name} \nreal name: {self.real_name} \nlocation: {self.location} \nstatus: {self.status} \nmissions completed: {self.missions_completed}"
