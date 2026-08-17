# database-success-broker-failure-inconsistency
This Python script simulates a common problem in distributed systems: a database operation succeeds, but a subsequent message broker operation fails. It demonstrates how this can lead to data inconsistency, where one part of the system (the database) has updated state, but other parts (relying on messages from the broker) are unaware.
