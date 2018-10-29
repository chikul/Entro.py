import math
"""
entrolib.py: Function library for different data entropy tests.
"""
__author__    = "Pavel Chikul"
__copyright__ = "Copyright 2018, REGLabs"


def compute_entropy(data):
    """
    Calculate Shannon entropy value for a given byte array.

    Keyword arguments:
    data -- data bytes
    """
    entropy = 0
    for x in range(256):
        it = float(data.count(x))/len(data)
        if it > 0:
            entropy += - it * math.log(it, 2)

    return entropy


def compute_entropy_graph(data, step):
    """
    Calculates an array of Shannon entropy values with a given step.

    Keyword arguments:
    data -- data bytes
    step -- step in bytes
    """
    entropies = []
    current_position = 0

    while current_position < len(data):
        new_entropy = compute_entropy(data[current_position:current_position + step])
        new_chi = compute_chi_squared(data[current_position:current_position + step])
        entropies.append([new_entropy, new_chi])
        current_position += step # Note: We skip the last chunk if it's less than step.

    return entropies


def detect_high_entropy_chunks(data, step):
    """
    Returns a list of high-entropy ranges in the given data block.

    Keyword arguments:
    data -- data bytes
    step -- step in bytes
    """
    high_entropies = []
    current_position = 0
    started = -1

    while current_position < len(data):
        new_entropy = compute_entropy(data[current_position:current_position + step])

        if started == -1 and new_entropy > 7.3:
            # Found start of high-entropy block.
            started = current_position

        if started != -1 and new_entropy <= 7.3:
            # Found end of high-entropy block.
            if current_position - started > 4096: # TODO: Experimental value.
                high_entropies.append((started, current_position))
            started = -1

        current_position += step # Note: We skip the last chunk if it's less than step.

    return high_entropies


def compute_monte_carlo_pi(data):
    """
    Calculate Monte Carlo Pi approximation for a given byte array.

    Keyword arguments:
    data -- data bytes
    """
    set_length = int(len(data) / 2) # All of the set values are inside square.
    r_square = 128 * 128
    circle_surface = 0

    for i in range(set_length):
        if ((data[i*2] - 128) ** 2 + (data[i*2+1] - 128) ** 2) <= r_square:
            circle_surface += 1

    return 4 * circle_surface / set_length


def get_pi_deviation(pi_value):
    """
    Returns an absolute percentage of difference between the provided Pi value and canonic.

    Keyword arguments:
    pi_value -- Pi value to be tested for difference
    """
    return abs(100 - (pi_value * 100 / math.pi))


def compute_chi_squared(data):
    """
    Calculate Chi-Squared value for a given byte array.

    Keyword arguments:
    data -- data bytes
    """
    expected = len(data) / 256
    observed = [0] * 256
    for b in data:
        observed[b] += 1

    chi_squared = 0
    for o in observed:
        chi_squared += (o - expected) ** 2 / expected

    return chi_squared


def write_xy2(data, out_file_name):
    file = open(out_file_name, "w") 
    
    set_length = int(len(data) / 2)
    r_square = 128 * 128
    
    for i in range(set_length):
        if ((data[i*2] - 128) ** 2 + (data[i*2+1]-128) ** 2) <= r_square:
            file.write(str(data[i*2]) + " " + str(data[i*2+1]) + "\r\n")
    file.close()
