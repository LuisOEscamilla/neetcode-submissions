class TimeMap:

    def __init__(self):
        self.dictionary = { }

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            keyList = [None] * (timestamp + 1)
            keyList[timestamp] = value
            self.dictionary[key] = keyList
        else:
            size = len(self.dictionary[key])
            self.dictionary[key] += [None] * (timestamp - size)
            self.dictionary[key].append(value)
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ""
        for i in range(timestamp, -1, -1):
            if i < len(self.dictionary[key]) and self.dictionary[key][i] != None:
                return self.dictionary[key][i]
        return ""
