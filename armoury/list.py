class PoweredList(list):
    def in_batches_of(self, batch_size=1):
        for i in range(0, len(self), batch_size):
            yield self[i:i+batch_size]
