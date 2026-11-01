class LogSystem(object):

    def __init__(self):
        self.logs = []
        self.granularity_indices = {
            "Year": 4,      # e.g., "2017"
            "Month": 7,     # e.g., "2017:01"
            "Day": 10,      # e.g., "2017:01:01"
            "Hour": 13,     # e.g., "2017:01:01:23"
            "Minute": 16,   # e.g., "2017:01:01:23:59"
            "Second": 19    # e.g., "2017:01:01:23:59:59"
        }

    def put(self, id, timestamp):
        self.logs.append((id, timestamp))

    def retrieve(self, start, end, granularity):
        idx = self.granularity_indices[granularity]
        
        start_prefix = start[:idx]
        end_prefix = end[:idx]
        
        result = []
        for log_id, timestamp in self.logs:
            if start_prefix <= timestamp[:idx] <= end_prefix:
                result.append(log_id)
                
        return result
