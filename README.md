# Mission Database: Manage the Field Agents

A simple command-line Python application to manage field agents using a MySQL database.  
You can add, view, update, and delete agents, each with a status and mission count.

## 📦 Project Structure
.
├── main.py
├── manager.py
├── models/
│ └── agent.py
└── DAL/
└── agent_dal.py

## 🚀 Features

- Add a new agent
- View all agents
- View a specific agent by ID
- Update agent information
- Delete agent by ID
- All data is stored and retrieved from a MySQL database

## 🧠 Agent Model

Each agent has the following attributes:

- `id`: unique identifier (auto-incremented by DB)
- `codeName`: the codename of the agent
- `realName`: the real name
- `location`: the agent's current location
- `status`: one of `Active`, `Injured`, `Missing`, `Retired`
- `missionsCompleted`: number of completed missions

## 🛠 Requirements

- Python 3.10+
- MySQL server
- `mysql-connector-python` package

## Database Setup
Create the following table in your MySQL eagleeyedb database:


- CREATE TABLE agents (
- id INT AUTO_INCREMENT PRIMARY KEY,
-    codeName VARCHAR(100),
-    realName VARCHAR(100),
-    location VARCHAR(100),
-    status VARCHAR(50),
-    missionsCompleted INT
);

## ▶️ How to Run
Make sure MySQL server is running.

Open the terminal inside the project folder.

Run the main file:

python main.py
Use the menu to interact with the system.

✅ Example Interaction

1. Add new agent
2. View all agents
3. View agent by ID
4. Update agent
5. Delete agent
6. Exit

📁 Notes
Status input must match one of the enum values: Active, Injured, Missing, Retired.

The program handles invalid inputs (e.g. strings instead of numbers).

Update and Delete options require a valid agent_id.

👤 Author

shlomo wind 

[sh.z.wind@gmail.com]()