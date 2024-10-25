from tkinter import Button, Label, Tk
import config
from modules import UserManagement
from modules import TableReservation
from modules import AgentMangement

def handle_button():
    print("test")

def main():
    print(f"Hello world - config: {config.user_details["email"], config.user_details["password"]}")
    # TableReservation.createTableReservation({
    #     "date": "2024-10-01",
    #     "time": "18:00",
    #     "party_size": 4,
    #     "customer_name": "John Doe",
    #     "customer_phone": "1234567890"
    # })

    AgentMangement.createAgent("agent 1")
    AgentMangement.createProcess("process_1", "A process",       "http://127.0.0.1:8080/hello_world", "", "GET")
    AgentMangement.createProcess("process_2", "Another process", "http://127.0.0.1:8080/hello_world", "", "POST")

    AgentMangement.createJob("job_1", "A job")
    AgentMangement.addProcessToJob("job_1", "process_1", 1)
    AgentMangement.addProcessToJob("job_1", "process_1", 3)
    AgentMangement.assignJobToAgent("agent_1", "job_1")

    
    print(f"=====[Agents ({len(AgentMangement.agents)})]=====")
    for agent in AgentMangement.agents:
        print(f"{agent["id"]}: {agent["name"]} - {agent.get("assigned_job", "NONE")}")

    print(f"=====[Stored Jobs]=====")
    for job in AgentMangement.jobs:
        print(f"{job["job_id"]}: {job["description"]} - {len(job["processes"])} processes")
        processes = job.get("processes", [])
        if len(processes) == 0:
            print("No process")
        else:
            for index, process in enumerate(processes):
                print(f"\t{index + 1}: {process["process_id"]} - delay: {process["delay"]}")


    # root = Tk()
    # 
    # root.title = "Customer Simulator"
    # w = Label(root, text='Customer Simulator')
    # w.pack()
    # button = Button(root, text='Run', width=25, command=handle_button)
    # button.pack()
    # root.mainloop()

if __name__ == "__main__":
    main()