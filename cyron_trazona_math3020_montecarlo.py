import numpy as np
import matplotlib.pyplot as plt

# Parameters with simple Error Handling
num_cpu = int(input("Please input the number of CPUs: "))
while num_cpu <= 0:
    num_cpu = int(input("Invalid input. Please input the number of CPUs: "))

infection_prob = float(input("Please input the probability of the infection spreading(between 0 and 1): "))
while infection_prob <= 0 or infection_prob > 1:
    infection_prob = float(input("Invalid input. Please input the probability of the infection spreading(between 0 and 1): "))

num_trials = int(input("How many trials would you like to run: "))
while num_trials <= 0:
    num_trials = int(input("Invalid input. How many trials would you like to run: "))

technician_cleans = int(input("Please input the number of computers the technician cleans per day: "))
while technician_cleans <= 0 or technician_cleans > num_cpu:
    technician_cleans = int(input("Invalid input. Please input the number of computers the technician cleans per day: "))

# Outputs for confirmation
print(f"Number of CPUs: {num_cpu}")
print(f"Infection probability: {infection_prob}")
print(f"Number of trials: {num_trials}")
print(f"Technician cleans per day: {technician_cleans}")

# Simulation function
def monte_carlo_simulation():
    # Initial infection status: 1 infected computer
    infection_status = np.zeros(num_cpu, dtype=bool)
    initial_infected = np.random.randint(0, num_cpu)  # Infect one computer at random
    infection_status[initial_infected] = True

    # Track if a computer has ever been infected
    ever_infected = infection_status.copy()
    
    # Count how many days it takes to clean all infections
    days = 0
    while infection_status.any():  # While there are infected computers
        days += 1
        
        # Spread infection: Vectorized approach
        if infection_status.any():
            uninfected = np.where(~infection_status)[0]  # Indices of uninfected computers
            new_infections = np.random.rand(len(uninfected)) < infection_prob
            infection_status[uninfected[new_infections]] = True
        
        ever_infected |= infection_status  # Track ever-infected computers

        # Technician cleans a number of infected computers at random
        infected_indices = np.where(infection_status)[0]
        cleaned = np.random.choice(infected_indices, size=min(technician_cleans, len(infected_indices)), replace=False)
        infection_status[cleaned] = False  # Clean selected computers

    # Return the number of days, the total number of infected computers, and the ever-infected status
    return days, ever_infected.sum(), ever_infected

# Run Monte Carlo Simulation
results_days = []
results_total_infected = []
ever_infected_counts = np.zeros(num_cpu, dtype=int)
all_infected_count = 0

for n in range(num_trials):
    days_to_clear, total_infected, ever_infected = monte_carlo_simulation()
    results_days.append(days_to_clear)
    results_total_infected.append(total_infected)
    ever_infected_counts += ever_infected  # Increment count for computers that were infected
    
    # Count trials where all computers were infected
    if ever_infected.sum() == num_cpu:
        all_infected_count += 1

# Convert results to NumPy arrays
results_days = np.array(results_days)
results_total_infected = np.array(results_total_infected)

# Calculate statistics
average_days_to_clear = np.mean(results_days)
average_infections = np.mean(results_total_infected)

# Calculate probabilities
average_probability_single_computer = np.mean(ever_infected_counts / num_trials)
probability_all_computers_infected = all_infected_count / num_trials

# Output Results
print(f"Expected days to completely clean the computers: {average_days_to_clear:.2f}")
print(f"Expected number of computers infected per trial: {average_infections:.2f}")
print(f"Overall average probability that any single computer gets infected at least once: {average_probability_single_computer:.4f}")
print(f"Probability that all computers get infected during a trial: {probability_all_computers_infected:.4f}")

# Visualize Results
# 1. Histogram of days to clear infections
plt.figure(figsize=(10, 6))
bins = np.linspace(results_days.min(), results_days.max(), 30)
plt.hist(results_days, bins=bins, edgecolor='black', alpha=0.7)
plt.xlabel("Days to Clear Infections")
plt.ylabel("Frequency")
plt.title(f"Days to Clear Infections\nAverage: {average_days_to_clear:.2f}")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2. Histogram of total infections
plt.figure(figsize=(10, 6))
bins = np.arange(0, num_cpu + 2)
plt.hist(results_total_infected, bins=bins, edgecolor='black', alpha=0.7)
plt.xlabel("Number of Computers Infected")
plt.ylabel("Frequency")
plt.title(f"Number of Infected Computers Per Trial\nAverage: {average_infections:.2f}")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 3. Bar chart of "ever infected" occurrences for each computer
plt.figure(figsize=(12, 6))
plt.bar(range(1, num_cpu + 1), ever_infected_counts, alpha=0.7)
plt.xlabel("Computer")
plt.ylabel("Number of Trials Ever Infected")
plt.title("Number of Trials Each Computer Was Ever Infected")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
