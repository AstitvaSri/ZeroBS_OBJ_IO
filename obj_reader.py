import numpy as np
import pickle

fname = ''
f = open(fname)

v = []
vt = []
vn = []
f_v = []
f_vt = []
f_vn = []

for line in f:

    if line[0:2]=='v ':
        info = line.strip().split(" ")
        v.append([float(info[1]),float(info[2]),float(info[3])])
    
    elif line[0:2]=='vt':
        info = line.strip().split(" ")
        vt.append([float(info[1]),float(info[2])])
    
        
    elif line[0:2]=='vn':
        info = line.strip().split(" ")
        vt.append([float(info[1]),float(info[2]),float(info[3])])

    elif line[0:2]=='f ':
        info = line.strip().split(" ")
        face1 = info[1].split("/")
        face2 = info[2].split("/")
        face3 = info[4].split("/")
        verts_idx = [int(face1[0]),int(face2[0]),int(face3[0])]
        verts_tex_idx = [int(face1[1]),int(face2[1]),int(face3[1])]
        verts_norm_idx = [int(face1[2]),int(face2[2]),int(face3[2])]
        f_v.append(verts_idx)
        f_vt.append(verts_tex_idx)
        f_vn.append(verts_norm_idx)

v = np.array(v)
vt = np.array(vt)
vn = np.array(vn)
f_v = np.array(f_v)
f_vt = np.array(f_vt)
f_vn = np.array(f_vn)

print(v.shape)
print(vt.shape)
print(vn.shape)
print(f_v.shape)
print(f_vt.shape)
print(f_vn.shape)

mesh_info = {'v':v,'vt':vt,'vn':vn,'f_v':f_v,'f_vt':f_vt,'f_vn':f_vn}

with open('/home/astitva/Workspace/Peel2Tex/peelmaps/random/103/poisson_param_shifted.pickle', 'wb') as f:
    pickle.dump(mesh_info, f)
