class StatProcessor:
    __max_pts = 1024

    def __init__(self):
        self.tickMod = 1
        self.tick = 0
        self.data = []

    def upd(self):
        self.tick = 0
        self.tickMod = 1
        self.data = []

    def double_size(self):
        self.tick = 0

    # structure:
    # (time, {"Vx":12, "Vy":24, "x":..., "y":...})

    def __call__(self, *args, **kwargs):
        if len(self.data) == self.__max_pts - 1:
            self.data = self.data[::2]
            self.tickMod *= 2

        self.tick += 1

        if self.tick % self.tickMod == 0:
            timestamp, params = args
            self.data.append((timestamp, params))

    def return_stats(self):
        time, params = zip(*self.data)
        keys = params[0].keys()
        dict_transposed = dict()
        for key in keys:
            dict_transposed.update({key: []})
        for elem in params:
            for key in keys:
                dict_transposed.get(key).append(elem.get(key))
        return time, dict_transposed
