
from Functions.QuranCorpus import parse_quranic_corpus

def load(file):
    f = open(file, 'rU', encoding='utf-8')
    return f.read()

def index_ahkam(file_ahkam):
     file = load(file_ahkam)
     spliedfile = file.split(")")
     ahkam_dict = dict()
     ayate_dict = dict()
     prev_sourat = 96
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
def Mad_dist(mad_aya,mad_test):
    list_aya = list(map(int, mad_aya))
    list_test = list(map(int, mad_test))
    spec_mad = [2,4,6]
    if mad_test in mad_aya :
        return 0
    dist_glob = 100
    if len(list_aya) < len(list_test):
        return dist_glob
    for i in range(0, len(list_aya) - len(list_test)+1):
        dist = 0
        for j in range(0,len(list_test)):
            if list_test[j]!=list_aya[i+j] and  list_test[j] in spec_mad and list_aya[i+j] in spec_mad:
                spec_mad.remove(list_test[j])
                spec_mad.remove(list_aya[i+j])
                item = spec_mad.pop()
                spec_mad = [2,4,6]
                if item != 4 :
                    dist += 1
                    continue 
            dist += abs(list_test[j]-list_aya[i+j]) 
        if dist_glob > dist : 
            dist_glob = dist
    return dist_glob
def Madsim(mad_serie,quran,mad_encode):
    index_ahkam1 = index_ahkam(mad_encode)
    aya_sim = list()
    aya_found = 0
    for sourat, ayate in index_ahkam1.items():
        for aya, made in ayate.items():
            if Mad_dist(made,mad_serie) < 2:
                aya_sim.insert(aya_found, quran[sourat][aya])
                aya_found += 1
    return aya_sim


if __name__ == '__main__':
    quran = parse_quranic_corpus("quranic-corpus-morphology-0.4.txt")
    list_ = Madsim("11211011212140",quran,"ahkaam_encoding.txt")
    for elem in list_:
        print (elem.arabic_text())