# resource_consumer.py
import time

def consume_cpu():
    """Function to consume CPU resources."""
    while True:
        [x**2 for x in range(10000)]

def consume_memory():
    """Function to consume Memory resources."""
    a = []
    while True:
        a.append('x' * 10**6)  # Append 1 million characters to the list
        time.sleep(1)

if __name__ == "__main__":
    consume_cpu()
    consume_memory()

