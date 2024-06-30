import os
import numpy as np
import pickle
import re

# custom OBJ reader
def ZEROBS_OBJ_READER(file_path):
	f = open(file_path)

	v = []
	vt = []
	vn = []
	f_v = []
	f_vt = []
	f_vn = []

	for line in f:
		line = re.sub(' +', ' ',line) #removes unwanted spaces from string
		if line[0:2]=='v ':
			info = line.strip().split(" ")
			v.append([float(info[1]),float(info[2]),float(info[3])])
		
		elif line[0:2]=='vt':
			info = line.strip().split(" ")
			vt.append([float(info[1]),float(info[2])])
		
			
		elif line[0:2]=='vn':
			info = line.strip().split(" ")
			vn.append([float(info[1]),float(info[2]),float(info[3])])

		elif line[0:2]=='f ':
			info = line.strip().split(" ")
			face1 = info[1].split("/")
			face2 = info[2].split("/")
			face3 = info[3].split("/")
			verts_idx = [int(face1[0]),int(face2[0]),int(face3[0])]
			f_v.append(verts_idx)
			if min(len(face1),len(face2),len(face3))==3:
				verts_tex_idx = [int(face1[1]),int(face2[1]),int(face3[1])]
				verts_norm_idx = [int(face1[2]),int(face2[2]),int(face3[2])]
				f_vt.append(verts_tex_idx)
				f_vn.append(verts_norm_idx)

	f.close()
	v = np.array(v)
	vt = np.array(vt)
	vn = np.array(vn)
	f_v = np.array(f_v)
	f_vt = np.array(f_vt)
	f_vn = np.array(f_vn)

	mesh_info = {'v':v,'vt':vt,'vn':vn,'f_v':f_v,'f_vt':f_vt,'f_vn':f_vn}
	return mesh_info

# custom OBJ writer
def ZEROBS_OBJ_WRITER(save_path,mesh_info, exists=False):
	mode = 'w'
	if exists:
		mode = 'a'
	if len(mesh_info['v'])>0:
		with open(save_path,mode) as f:
			for idx in range(len(mesh_info['v'])):
				v0,v1,v2 = mesh_info['v'][idx]
				line = f"v {v0} {v1} {v2}\n"
				f.write(line)
			f.close()
	if len(mesh_info['vn'])>0:
		with open(save_path,'a') as f:
			for idx in range(len(mesh_info['vn'])):
				v0,v1,v2 = mesh_info['vn'][idx]
				line = f"vn {v0} {v1} {v2}\n"
				f.write(line)
			f.close()
	if len(mesh_info['vt'])>0:
		with open(save_path,'a') as f:
			for idx in range(len(mesh_info['vt'])):
				u,v = mesh_info['vt'][idx]
				line = f"vt {u} {v}\n"
				f.write(line)
			f.close()
	with open(save_path,'a') as f:
		for idx in range(len(mesh_info['f_v'])):
			fv0=fv1=fv2=fn0=fn1=fn2=fvt0=fvt1=fvt2 = ''
			if len(mesh_info['f_v'])>0:
				fv0, fv1, fv2 = mesh_info['f_v'][idx]
			if len(mesh_info['f_vt'])>0:
				fvt0, fvt1, fvt2 = mesh_info['f_vt'][idx]
			if len(mesh_info['f_vn'])>0:
				fn0, fn1, fn2 = mesh_info['f_vn'][idx]
			line = f"f {fv0}/{fvt0}/{fn0} {fv1}/{fvt1}/{fn1} {fv2}/{fvt2}/{fn2}\n"
			f.write(line)
		f.close()
