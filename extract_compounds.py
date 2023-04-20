import random
N = 400

def get_uniq_compoundid():
    file_path = './actives_final.mol2'
    with open(file_path) as f:
        lines = f.readlines()

    lines_strip = [line.strip() for line in lines ]
    list_id = [line_s for line_s in lines_strip if 'CHEMBL' in line_s ]
    return list_id

def write_mol2(datalist, j):
    f2 = open('myfile.mol2', 'a')
    for k in range(j,len(datalist)):
        f2.write(datalist[k-1])
        if datalist[k] == '@<TRIPOS>MOLECULE\n':
            break
    f2.close()

list_id = get_uniq_compoundid()
list_id_s = set(list_id)
uniq_id = random.sample(list(list_id_s), N)

f = open('actives_final.mol2', 'r', encoding='UTF-8')
datalist = f.readlines()

for i in range(0, len(uniq_id)):
    for j in range(0, len(datalist)):
        if uniq_id[i]+'\n' == datalist[j]:
            write_mol2(datalist, j)
            break

f.close()