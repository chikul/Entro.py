#!/usr/bin/python3.6
import sys
import argparse
from entrolib import *


def process_file_list(in_file_name, out_file_name):
    """
    Creates an entropy report for a list of files and saves it in a CSV spreadsheet.
    """
    with open(in_file_name, "r") as f:
        file_list = f.readlines()

    sizes = []
    entropies = []
    pi_deviations = []
    chis = []

    with open(out_file_name, "w") as file_out:
        file_out.write("File Name;File Size (B);Entropy;Pi Deviation (%);Chi-Squared\r\n")

    for i in range(len(file_list)):
        file_name = file_list[i].strip()
        sys.stdout.write("\rProcessing %d%%" % (i * 100 / len(file_list)))
        sys.stdout.flush()

        byte_array = []
        with open(file_name, "rb") as f:
            byte_array = f.read()

        file_size = len(byte_array)
        entropy = compute_entropy(byte_array)
        pi_deviation = get_pi_deviation(compute_monte_carlo_pi(byte_array))
        chi_squared = compute_chi_squared(byte_array)

        with open(out_file_name, "a") as file_out:
            file_out.write("%s;%d;%f;%f;%f\r\n" % (file_name, file_size, entropy, pi_deviation, chi_squared))

        sizes.append(file_size)
        entropies.append(entropy)
        pi_deviations.append(pi_deviation)
        chis.append(chi_squared)

    print("Size:         %d, %d, %d" % (sum(sizes)/len(sizes), min(sizes), max(sizes)))
    print("Entropy:      %.4f, %.4f, %.4f" % (sum(entropies)/len(entropies), min(entropies), max(entropies)))
    print("Pi deviation: %.4f, %.4f, %.4f" % (sum(pi_deviations)/len(pi_deviations), min(pi_deviations), max(pi_deviations)))
    print("Chi-Squared:  %.4f, %.4f, %.4f" % (sum(chis)/len(chis), min(chis), max(chis)))


def write_entropy_graph(in_file_name, out_file_name, step):
    """
    Calculates entropy variation for a file and write it to CSV spreadsheet.
    """
    byte_array = []
    with open(in_file_name, "rb") as f:
        byte_array = f.read()

    entropies = compute_entropy_graph(byte_array, step)
    with open(out_file_name, "w") as file_out:
        file_out.write("Entropy (per %d bytes);High Entropy\r\n" % step)
        for i in range(len(entropies)):
            file_out.write("%f;%s\r\n" % (entropies[i][0], str(entropies[i][1]) if entropies[i][1] == 8 else ""))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Provides different methods of entropy calculation.')
    '''if len(sys.argv) != 2:
        print("Usage: ./entro.py <filepath>")
        sys.exit()'''

    write_entropy_graph(sys.argv[1], "outss.csv", 512)
    '''byte_array = []
    with open(sys.argv[1], "rb") as f:
        byte_array = f.read()

    entries = detect_high_entropy_chunks(byte_array, 512)
    for e in entries:
        print("%7d %7d" % (e[0]/512, e[1]/512))'''

    print()
