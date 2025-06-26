import mysql.connector
from models.agent import Agent

class AgentDal:
    def __init__(self,host="localhost",user="root",password="",database="eagleeyedb"):
        self.conn =  mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database)
        self.cursor = self.conn.cursor(dictionary=True)

    def close(self):
        self.cursor.close()
        self.conn.close()

    def add_agent(self,agent:Agent):
        query = "INSERT INTO agents(codeName,realName,location,status,missionsCompleted) VALUES(%s, %s, %s, %s, %s)"
        self.cursor.execute(query,(
            agent.codeName,
            agent.realName,
            agent.location,
            agent.status.value,
            agent.missionsCompleted
        ))
        self.conn.commit()

    def get_all_agents(self):
        query = "SELECT * FROM agents"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return [Agent(**row) for row in result]

    def get_agent_by_id(self,agent_id:int):
        query = "SELECT * FROM agents WHERE id = %s"
        self.cursor.execute(query,(agent_id,))
        result = self.cursor.fetchone()
        return Agent(**result) if result else None

    def update_agent(self,agent:Agent):
        query = "UPDATE agents SET codeName = %s,realName = %s,location = %s,status = %s,missionsCompleted = %s WHERE id = %s"
        self.cursor.execute(query,(
            agent.codeName,
            agent.realName,
            agent.location,
            agent.status.value,
            agent.missionsCompleted,
            agent.id
        ))
        self.conn.commit()

    def delete_agent(self,agent_id:int):
        query = "DELETE FROM agents WHERE id = %s"
        self.cursor.execute(query,(agent_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
