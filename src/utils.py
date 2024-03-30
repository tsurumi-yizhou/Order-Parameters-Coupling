from order import Order
from atom import Atom
from ase.cell import Cell
from spglib import get_symmetry
import matplotlib.pyplot as plt


def atomic_number(element) -> int:
    elements = {
        "H": 1,
        "He": 2,
        "Li": 3,
        "Be": 4,
        "B": 5,
        "C": 6,
        "N": 7,
        "O": 8,
        "F": 9,
        "Ne": 10,
        "Na": 11,
        "Mg": 12,
        "Al": 13,
        "Si": 14,
        "P": 15,
        "S": 16,
        "Cl": 17,
        "Ar": 18,
        "K  ": 19,
        "Ca": 20,
        "Sc": 21,
        "Ti": 22,
        "V": 23,
        "Cr": 24,
        "Mn": 25,
        "Fe": 26,
        "Co": 27,
        "Ni": 28,
        "Cu": 29,
        "Zn": 30,
        "Ga": 31,
        "Ge": 32,
        "As": 33,
        "Se": 34,
        "Br": 35,
        "Kr": 36,
        "Rb": 37,
        "Sr": 38,
        "Y": 39,
        "Zr": 40,
        "Nb": 41,
        "Mo": 42,
        "Tc": 43,
        "Ru": 44,
        "Rh": 45,
        "Pd": 46,
        "Ag ": 47,
        "Cd": 48,
        "In": 49,
        "Sn": 50,
        "Sb ": 51,
        "Te": 52,
        "I": 53,
        "Xe": 54,
        "Cs": 55,
        "Ba": 56,
        "La": 57,
        "Ce": 58,
        "Pr": 59,
        "Nd": 60,
        "Pm": 61,
        "Sm": 62,
        "Eu": 63,
        "Gd": 64,
        "Tb": 65,
        "Dy": 66,
        "Ho": 67,
        "Er": 68,
        "Tm": 69,
        "Yb": 70,
        "Lu": 71,
        "Hf": 72,
        "Ta": 73,
        "W  ": 74,
        "Re": 75,
        "Os": 76,
        "Ir": 77,
        "Pt": 78,
        "Au": 79,
        "Hg ": 80,
        "Tl": 81,
        "Pb": 82,
        "Bi": 83,
        "Po": 84,
        "At": 85,
        "Rn": 86,
        "Fr": 87,
        "Ra": 88,
        "Ac": 89,
        "Th": 90,
        "Pa": 91,
        "U": 92,
        "Np": 93,
        "Pu": 94,
        "Am": 95,
        "Cm": 96,
        "Bk": 97,
        "Cf": 98,
        "Es": 99,
        "Fm": 100,
        "Md": 101,
        "No": 102,
        "Lr": 103,
        "Rf": 104,
        "Db": 105,
        "Sg": 106,
        "Bh": 107,
        "Hs": 108,
        "Mt": 109,
        "Ds": 110,
        "Rg": 111,
        "Cn": 112,
        "Nh": 113,
        "Fl": 114,
        "Mc": 115,
        "Lv": 116,
        "Ts": 117,
        "Og": 118
    }
    return elements[element]


def read_symmetry_from_file(filename: str) -> list[list[list[float]]]:
    with open(filename, 'r') as file:
        meta_data = file.readline().split()
        element = meta_data[0]
        count = int(meta_data[1])
        cell = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        atoms = []
        atomic_numbers = [atomic_number(element)] * count
        for _ in range(count):
            line = list(map(float, file.readline().split()))
            atoms.append([line[0], line[1], line[2]])
        return get_symmetry((cell, atoms, atomic_numbers))


def read_orders_from_file(filename: str) -> list[Order]:
    with open(filename, 'r') as file:
        orders = []
        atoms = []
        meta_data = file.readline().split()
        element = meta_data[0]
        count = int(meta_data[1])
        for _ in range(count):
            line = list(map(float, file.readline().split()))
            atoms.append(Atom(line[0], line[1], line[2], line[3]))
        for _ in range(count):
            line = list(map(int, file.readline().split()))
            plus = set()
            for index in line:
                plus.add(atoms[index - 1])
            minus = set(atoms) - plus
            orders.append(Order(element, plus, minus))
        return orders


def display(order_param: Order):
    figure = plt.figure()
    ax = figure.add_subplot(111, projection='3d')

    ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0], color='black')
    ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [1, 1, 1, 1, 1], color='black')
    ax.plot([0, 0], [0, 0], [0, 1], color='black')
    ax.plot([1, 1], [0, 0], [0, 1], color='black')
    ax.plot([0, 0], [1, 1], [0, 1], color='black')
    ax.plot([1, 1], [1, 1], [0, 1], color='black')

    for atom in order_param.plus:
        ax.scatter(atom.position[0], atom.position[1], atom.position[2], c='r', s=100)

    for atom in order_param.minus:
        ax.scatter(atom.position[0], atom.position[1], atom.position[2], c='g', s=100)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.view_init(elev=20, azim=40)
    plt.show()

