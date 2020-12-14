
"""


@author: matt Senibaldi
"""


def fixScrn(theList):
    for i in range(len(theList)):
        theList[i] = theList[i].replace('\n', '')
    return theList