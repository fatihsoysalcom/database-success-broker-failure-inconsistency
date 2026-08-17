import random
import time

# Simulate a database where an order is saved
def save_order_to_database(order_id: str) -> bool:
    print(f"  [DB] Attempting to save order {order_id} to database...")
    # Simulate network latency or processing time
    time.sleep(0.1)
    # For this demonstration, we assume the database operation usually succeeds.
    print(f"  [DB] Order {order_id} successfully saved to database.")
    return True

# Simulate a message broker where an event is published
def publish_order_event(order_id: str, event_type: str) -> bool:
    print(f"  [Broker] Attempting to publish '{event_type}' event for order {order_id}...")
    time.sleep(0.2)
    # Simulate a random failure for the message broker.
    # This is the core of the problem discussed in the article: database succeeds, broker fails.
    if random.choice([True, False, False]): # 1/3 chance of success, 2/3 chance of failure
        print(f"  [Broker] Event '{event_type}' for order {order_id} successfully published.")
        return True
    else:
        print(f"  [Broker] ERROR: Failed to publish '{event_type}' event for order {order_id}. (Simulated failure)")
        return False

def process_new_order(order_id: str):
    print(f"\n--- Processing New Order: {order_id} ---")

    db_success = save_order_to_database(order_id)

    if db_success:
        print(f"  [System State] Database has order {order_id}. Now attempting to publish event.")
        broker_success = publish_order_event(order_id, "OrderCreated")

        if broker_success:
            print(f"  [Result] Order {order_id} processed successfully and event published. System is consistent.")
        else:
            # This is the critical scenario the article describes: DB success, Broker failure.
            print(f"  [Result] WARNING: Order {order_id} saved to DB, BUT event failed to publish.")
            print(f"  [Result] System is now INCONSISTENT: Database has the order, but downstream services (via broker) are unaware.")
            print(f"  [Result] This highlights the need for robust retry mechanisms, idempotency, or eventual consistency patterns.")
    else:
        print(f"  [Result] ERROR: Failed to save order {order_id} to database. Event not published.")
        print(f"  [Result] Order processing failed entirely. System state is consistent (no order anywhere). This is less problematic.")


if __name__ == "__main__":
    print("Simulating distributed order processing with potential message broker failures.")
    print("Watch for scenarios where the database operation succeeds but the message broker operation fails.")

    # Run multiple times to demonstrate both success and failure scenarios
    for i in range(1, 4):
        process_new_order(f"ORDER-{i:03d}")

    print("\n--- Simulation Complete ---")
    print("This example clearly illustrates how a successful database operation followed by a failed message broker operation")
    print("can lead to data inconsistency in distributed systems, a core challenge discussed in the article.")
