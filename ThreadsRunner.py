class ThreadsRunner(object):

    def __init__(self, bthreads,  composer):
        self._bthreads = bthreads
        self._snapshots = []
        self._composer = composer

    def _collect_initial_snapshots(self):
        for bt in self._bthreads:
            ss = next(bt)
            ss['bt'] = bt
            self._snapshots.append(ss)

    def _next_event(self):
        requested, blocked = self._composer.compose(self._snapshots)
        return self._composer.next_event(requested, blocked)

    def _advance_bthreads(self, event):
        self._composer.advance_bthreads(event, self._snapshots)

    def run(self):
        self._collect_initial_snapshots()

        while True:
            event = self._next_event()

            if event is None:
                return

            print("Event--->", event)

            self._advance_bthreads(event)


# TODO: prints or logs when debuging of debug
# TODO: numpyComposer
# TODO: composer functions
