import numpy as np
import matplotlib.pyplot as plt

def radioactive_decay_simulation(N0, decay_constant, time_steps):
    N = [N0]
    times = np.linspace(0, time_steps, time_steps + 1)

    for t in range(time_steps):
        decayed = 0
        for i in range(N[-1]):
            if np.random.random() < decay_constant:
                decayed += 1
        N.append(N[-1] - decayed)

    return times, N

def plot_decay(times, N):
    plt.figure(figsize=(10, 6))
    plt.plot(times, N, label='Remaining Atoms', color='blue')
    plt.title("Radioactive Decay Simulation")
    plt.xlabel("Time Steps")
    plt.ylabel("Number of Atoms")
    plt.legend()
    plt.grid()
    plt.show()

def main():
    print("Welcome to the Radioactive Decay Simulator!")
    try:
        N0 = int(input("Enter the initial number of atoms: "))
        decay_constant = float(input("Enter the decay constant (0 < λ < 1): "))
        time_steps = int(input("Enter the number of time steps to simulate: "))

        print("\nSimulating radioactive decay... Please wait!")
        times, N = radioactive_decay_simulation(N0, decay_constant, time_steps)
        plot_decay(times, N)

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()
