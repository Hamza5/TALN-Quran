# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
from Functions.QuranCorpus import parse_quranic_corpus
def load(file):
    f = open(file, 'rU', encoding='utf-8')
    return f.read()

def index_ahkam(file_ahkam):
     file = load(file_ahkam)
     spliedfile = file.split(")")
     ahkam_dict = dict()
     ayate_dict = dict()
     prev_sourat = 1
     for aya in spliedfile:
         if aya == "\n" or aya == "": 
             break
         splited_aya = aya.split("(")
         sourat_mad = splited_aya[0]
         aya_sourat = splited_aya[1].split(":")
         sourat_number = aya_sourat[0]
         aya_number = aya_sourat[1]
         ayate_dict[int(aya_number)] = sourat_mad
         if int(aya_number) == 1:
             ahkam_dict[prev_sourat]= ayate_dict.copy()
             prev_sourat = int(sourat_number)
             ayate_dict.clear()
         if int(sourat_number) == 114 and int(aya_number) == 6: 
             ahkam_dict[int(sourat_number)]= ayate_dict.copy()
             ayate_dict.clear()     
     return ahkam_dict
         
def histoplot(sourate,deb,fin,quran, title):
    elements = []
    labels = []
    index_ahkam1 = index_ahkam("../ahkaam_encoding.txt")
    counts = {i: 0 for i in 'aiouA'}
    addedspace = 0;
    for ayat in range(deb, fin):
        label = list(index_ahkam1[sourate+1][ayat])
        addedspace = 0
        ayastring = quran[sourate][ayat]
        for word in str(ayastring).split(" "):
            numerVoy = 0
            for char in str(word):
                if char in counts:
                    numerVoy += 1
            addedspace +=numerVoy
            labels.append(word)
            labels.extend([''] * (numerVoy - 1))
        elements.extend(label)
        if len(label)-addedspace >= 0:
            labels.extend([''] * (len(label)-addedspace))
        else:
            elements.extend(['0'] * (addedspace - len(label)))
    resultat = list(map(int, elements))
    import pylab as pl
    figure = pl.figure()
    ax = pl.subplot(111)
    y_pos = np.arange(len(labels))
    performance = resultat
    ax.bar(y_pos, performance, align='center', alpha=1)
    ax.set_label(performance)
    pl.xticks(y_pos, labels, rotation=30)
    ax.set_xlabel('Elongations')
    ax.set_title(title)
    return figure

if __name__ == '__main__':
    quran= parse_quranic_corpus("../quranic-corpus-morphology-0.4.txt")
    histoplot(2, 2, 5, quran).show()
    
