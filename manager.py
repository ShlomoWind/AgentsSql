from DAL.agent_dal import AgentDal
from models.agent import Agent, Status


class Manager:
    def __init__(self):
        self.dal = AgentDal()

    def show_menu(self):
        print("=================================")
        print("1. Add new agent")
        print("2. View all agents")
        print("3. View agent by ID")
        print("4. Update agent")
        print("5. Delete agent")
        print("6. Exit")
        print("=================================")

    def agent_user_input(self):
        print("Enter new agent details:")
        code_name = input("Code name: ")
        real_name = input("Real name: ")
        location = input("Location: ")
        status_input = input("Status (Active, Injured, Missing, Retired): ")
        missions_completed = int(input("Missions completed: "))
        status = Status(status_input)
        agent = Agent(code_name,real_name,location,status,missions_completed)
        return agent

    def menu(self):
        while True:
            self.show_menu()
            choose = input("enter the number of your choose:")
            match choose:
                case "1":
                    agent = self.agent_user_input()
                    self.dal.add_agent(agent)
                case "2":
                    agents = self.dal.get_all_agents()
                    if not agents:
                        print("no agents")
                    else:
                        for agent in agents:
                            print("-" * 20)
                            print(agent)
                        print("-" * 20)
                case "3":
                    try:
                        agent_id = int(input("enter agent id:"))
                        agent = self.dal.get_agent_by_id(agent_id)
                        if agent:
                            print(agent)
                        else:
                            print("not found")
                    except ValueError:
                        print("invalid ID! enter a number")
                case "4":

                case "5":
                    try:
                        agent_id = int(input("enter the agent id to delete: "))
                        self.dal.delete_agent(agent_id)
                    except ValueError:
                        print("invalid agent id")
                case "6":
                    print("Exiting program. Goodbye!")
                    self.dal.close()
                    break
