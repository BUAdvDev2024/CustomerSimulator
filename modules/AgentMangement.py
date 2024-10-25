agents = []
processes = []
jobs = []

def createAgent(name):
    agents.append({ "id": f"agent_{len(agents) + 1}", "name": name})


def createProcess(process_id, description, endpoint, authorisation_data, method):
    processes.append({ "process_id": process_id, "description": description, "method": method, "endpoint": endpoint, "authorisation_data": authorisation_data})


def createJob(job_id, description):
    jobs.append({ "job_id": job_id, "description": description, "processes": []})


def addProcessToJob(job_id: str, process_id: str, delay: float):
    found_job = next(iter([job for job in jobs if job["job_id"] == job_id]), None)
    if found_job == None:
        print("No job found")
        return
    found_process = next(iter([process for process in processes if process["process_id"] == process_id]), None)
    if found_process == None:
        print("No process found")
        return 
    
    found_job.get("processes").append({ "process_id": process_id, "delay": delay})


def assignJobToAgent(agent_id, job_id):
    found_job = next(iter([job for job in jobs if job["job_id"] == job_id]), None)
    if found_job == None:
        print("No job found")
        return
    agent_found = False
    for index, agent in enumerate(agents):
        if agent["id"] == agent_id:
            agent["assigned_job"] = job_id
            print(f"Job assigned to agent {agent['id']}")
            agent_found = True
    if agent_found == False:
        print("No agent found")   
    

def getAgents():
    return agents