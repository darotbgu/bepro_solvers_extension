class BaseComposer(object):

    def __init__(self):
        pass

    def compose(self, b_threads):
        return [thread["request"] for thread in b_threads]

    def next_event(self, requested, blocked):
        pass

    def advance_bthreads(self, event, snapshots):
        pass
