class JSONIterator:
    def __init__(self, data):
        self.data = data
        self.stack = [(None, data, iter(data.items()))] if isinstance(data, dict) else [(None, data, iter(enumerate(data)))]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            key, current_data, current_iter = self.stack[-1]
            try:
                key, value = next(current_iter)
                if isinstance(value, (dict, list)):
                    self.stack.append((key, value, iter(value.items()) if isinstance(value, dict) else iter(enumerate(value))))
                return key, value, len(self.stack) - 1
            except StopIteration:
                self.stack.pop()
        raise StopIteration
