from collections import deque

class Customer:
    def __init__(self, customer_id, item_count):
        self.customer_id = customer_id
        self.item_count = item_count
        self.wait_time = 0

    def __str__(self):
        return f"Customer {self.customer_id} ({self.item_count} items)"

class CheckoutLane:
    def __init__(self, processing_rate):
        self.queue = deque()
        self.processing_rate = processing_rate 
        self.current_customer = None
        self.time_remaining = 0

    def add_customer(self, customer):
        self.queue.append(customer)

    def is_idle(self):
        return self.current_customer is None

    def tick(self):
        if self.current_customer:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                print(f"{self.current_customer} finished checkout ✅")
                self.current_customer = None

        if not self.current_customer and self.queue:
            self.current_customer = self.queue.popleft()
            self.time_remaining = max(1, self.current_customer.item_count // self.processing_rate)
            print(f"{self.current_customer} started checkout 🛒")

    def queue_length(self):
        return len(self.queue) + (0 if self.is_idle() else 1)

class Supermarket:
    def __init__(self, num_lanes, rates):
        self.lanes = [CheckoutLane(rate) for rate in rates]
        self.time = 0

    def arrive_customer(self, customer):
        best_lane = min(self.lanes, key=lambda lane: lane.queue_length())
        best_lane.add_customer(customer)
        print(f"{customer} chose lane with rate {best_lane.processing_rate} 🏁")

    def tick(self):
        print(f"\n⏱️ Time: {self.time}")
        for i, lane in enumerate(self.lanes):
            print(f"  Lane {i+1}: ", end="")
            lane.tick()
        self.time += 1

# Tests
supermarket = Supermarket(num_lanes=3, rates=[2, 3, 1])
# Simulate customer arrival
customers = [
    Customer(1, 6),
    Customer(2, 4),
    Customer(3, 2),
    Customer(4, 9),
    Customer(5, 5)
]
for cust in customers:
    supermarket.arrive_customer(cust)
# Simulate 10 time units
for _ in range(10):
    supermarket.tick()
