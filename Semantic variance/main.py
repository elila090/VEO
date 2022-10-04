"""
Created by Elise Lång 2022-09-30

Calculation of Semantic Variance of ontologies.
"""
import math
from data import *


def semantic_variance(o):
    """Semantic variance as a sum of each concept's semantic distance normalized to ontology's size.

    :param  o:  list of all concept in ontology and with their depth from root
    :type   o:  list
    :returns:   positive normalized value in range [0,1]
    :rtype:     float
    """
    sum_semantic_distance = 0
    for c in o:
        d = semantic_distance(c)
        sum_semantic_distance += d ** 2

    variance = sum_semantic_distance/len(o)
    return variance


def semantic_distance(concept, root=1):
    """Semantic distance as a function of number of non-common taxonomic ancestors

    :param  concept:    number of taxonomic ancestors of concept in the ontology, including itself
    :type   concept:    int
    :param  root:       root of ontology, default = 1
    :type   root:       int
    :returns:           positive normalized value in range [0,1]
    :rtype: float
    """
    distance = math.log2(1 + (concept - root) / concept)
    return distance


def maximum_depth(o):
    """Length of the longest taxonomic branch in the ontology, measured as the number of concepts from the root
        node to the leaves of the taxonomy

    :param  o:    list of all concept in ontology and with their depth from root
    :type   o:    list
    :returns:     maximum depth of ontology
    :rtype: int
    """
    depth = max(o)
    return depth


def average_depth(o):
    """Average length of all taxonomic branches from the root node

    :param  o:    list of all leaf concept in ontology and with their depth from root
    :type   o:    list
    :returns:     average depth of ontology
    :rtype: float
    """
    depth = (sum(o) - len(o)) / len(o)
    return depth


if __name__ == '__main__':
    ontologies = [veo, codo, vio, hhear, vico, ncit]
    for ontology in ontologies:
        print(f'---------------- {ontology.name} -----------------')
        print(f'semantic variance:  {semantic_variance(ontology.data)}')
        print(f'maximum depth:      {maximum_depth(ontology.data)}')
        print(f'number of classes:  {len(ontology.data)}')

