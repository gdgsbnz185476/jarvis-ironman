class AgentState:
    def __init__(self):
        self.memory = []
        self.last_task = None
        self.plan = []
        self.errors = []
