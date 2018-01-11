#!/usr/bin/python

'''
Simple example script demonstrating how to use the PeptideBuilder library.

The script generates a peptide consisting of six arginines in alpha-helix
conformation, and it stores the peptide under the name "example.pdb".
'''

from __future__ import print_function
from PeptideBuilder import Geometry
import PeptideBuilder
import Bio.PDB
from Bio.PDB.Vector import calc_angle
import numpy as np

def generateAA(aaName):
	geo = Geometry.geometry(aaName)
	# geo.phi=-60
	geo.phi=0
	# geo.psi_im1=-40
	geo.psi_im1=0
	structure = PeptideBuilder.initialize_res(geo)
	out = Bio.PDB.PDBIO()
	out.set_structure(structure)
	out.save( "example.pdb" )

	return structure[0]['A'][1]

def getCG1_CB_CG2_angle():
	residue = generateAA('V')
	v1 = residue['CG1'].get_vector()
	v2 = residue['CG2'].get_vector()
	v3 = residue['CB'].get_vector()
	CG1_CB_CG2_angle = calc_angle(v1,v3,v2)
	print(CG1_CB_CG2_angle)

def getOG1_CB_CG2_angle():
	residue = generateAA('T')
	v1 = residue['OG1'].get_vector()
	v2 = residue['CG2'].get_vector()
	v3 = residue['CB'].get_vector()
	OG1_CB_CG2_angle = calc_angle(v1,v3,v2)
	print(OG1_CB_CG2_angle)

def getOD1_CG_OD2_angle():
	residue = generateAA('D')
	v1 = residue['OD1'].get_vector()
	v2 = residue['OD2'].get_vector()
	v3 = residue['CG'].get_vector()
	OD1_CG_OD2_angle = calc_angle(v1,v3,v2)
	print(OD1_CG_OD2_angle)

def getIleAngles():
	residue = generateAA('I')
	v1 = residue['CA'].get_vector()
	v2 = residue['CG1'].get_vector()
	v3 = residue['CB'].get_vector()
	CG1_CB_CG2_angle = calc_angle(v1,v3,v2)

def getHis():
	residue = generateAA('H')
	print ('R_CG_CD2 = ', residue['CG'] - residue['CD2'])
	print ('R_CG_ND1 = ', residue['CG'] - residue['ND1'])
	print ('R_CG_NE2 = ', residue['CG'] - residue['NE2'])
	print ('R_CG_CE1 = ', residue['CG'] - residue['CE1'])
	v1 = residue['CB'].get_vector()
	v2 = residue['CG'].get_vector()
	v_ne2 = residue['NE2'].get_vector()
	v_nd1 = residue['ND1'].get_vector()
	v_ce1 = residue['CE1'].get_vector()
	v_cd2 = residue['CD2'].get_vector()
	print ('CB_CG_NE2_angle = ', calc_angle(v1,v2,v_ne2))
	print ('CB_CG_ND1_angle = ', calc_angle(v1,v2,v_nd1))
	print ('CB_CG_CE1_angle = ', calc_angle(v1,v2,v_ce1))
	print ('CB_CG_CD2_angle = ', calc_angle(v1,v2,v_cd2))
	

def getPro():
	residue = generateAA('P')
	vN = residue['N'].get_coord()
	vCA = residue['CA'].get_coord()
	vCB = residue['CB'].get_coord()
	vCG = residue['CG'].get_coord()
	vCD = residue['CD'].get_coord()
	vC = residue['C'].get_coord()
	
	angle = np.pi-np.arccos(vN[0]/(residue['CA']-residue['N']))
	
	rotMat = np.array([[np.cos(angle), -np.sin(angle),0], [np.sin(angle), np.cos(angle), 0], [0,0,1]])
	print ('N', np.dot(rotMat,vN))
	print ('CA', np.dot(rotMat,vCA))
	print ('CB', np.dot(rotMat,vCB))
	print ('CG', np.dot(rotMat,vCG))
	print ('CD', np.dot(rotMat,vCD))
	print ('C', np.dot(rotMat,vC))

def getPhe():
	residue = generateAA('F')
	


if __name__=='__main__':
	getPhe()
	