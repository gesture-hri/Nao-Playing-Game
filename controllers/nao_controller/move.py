class Move:
    def __init__(self, sequence, execution_time):
        self.sequence = sequence
        self.execution_time = execution_time
        self.start_stamp = float('-inf')

    def start(self, time_stamp):
        self.start_stamp = time_stamp

    def is_completed(self, time_stamp):
        return time_stamp - self.start_stamp >= self.execution_time