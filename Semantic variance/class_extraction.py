"""
Created by Elise Lång 2022-10-03

Extraction of class hierarchy from ontology.
"""
import pandas as pd


def term_extraction(excel_name, required_cols):
    """Converts terms and parent from excel input to dictionary

    :param  excel_name:     name of Excel file
    :type   excel_name:     str
    :param  required_cols:  list of column indexes which should be extracted from excel file
    :type   required_cols:  list

    :returns:   term and parent relation dictionary
    :rtype:     dict
    """

    df = pd.read_excel(excel_name, usecols=required_cols)
    rdict = {}
    size = len(df.index)
    for i_row in range(size):
        rdict[df.iloc[i_row][0]] = df.iloc[i_row][1]

    # entity is type float
    return rdict


def hierarchy_extraction(relation_dict):
    """Extracts hierarchy for each term end returns dictionary

    :param  relation_dict:      terms in ontology and their parent
    :type   relation_dict:      dict

    :returns:   term hierarchy dictionary
    :rtype:     dict
    """
    hierarchy_dict = {}
    for term in relation_dict.keys():
        hierarchy_dict[term] = get_term_hierarchy(relation_dict, hierarchy_dict, term)

    return hierarchy_dict


def get_term_hierarchy(relation_dict, hierarchy_dict, term, level=0):
    """Extracts hierarchy term

    :param  relation_dict:      terms in ontology and their parent
    :type   relation_dict:      dict
    :param  hierarchy_dict:     term hierarchy dictionary with each term and with their depth from root
    :type   hierarchy_dict:     dict
    :param  term:               selected term from iteration or parent
    :type   term:               str
    :param  level:              hierarchy number, default as start value is 0
    :type   level:              int

    :returns:   level
    :rtype:     int
    """
    if term in hierarchy_dict:
        return hierarchy_dict[term] + level
    elif type(relation_dict[term]) == float:
        return level + 1
    elif relation_dict[term] == "http://www.w3.org/2002/07/owl#Thing":
        return level + 1
    else:
        return get_term_hierarchy(relation_dict, hierarchy_dict, relation_dict[term], level + 1)


def dict_to_int_list(dictionary):
    """Converts dictionary of term hierarchy to list of hierarchy numbers

    :param  dictionary:      term hierarchy dictionary with each term and with their depth from root
    :type   dictionary:      dict
    :returns:   list of hierarchy numbers
    :rtype:     list
    """
    return list(dictionary.values())











