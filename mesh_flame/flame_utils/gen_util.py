'''
demo code for loading FLAME face model
Tianye Li <tianye.li@tuebingen.mpg.de>
Based on the hello-world script from SMPL python code
http://smpl.is.tue.mpg.de/downloads
'''
from __future__ import print_function

import sys
#sys.path.append('/mnt/d/Jake/blender-addons/modules')
#sys.path.append(R'D:\Jake\FaceModels\flame\postech-flame-fitting')
#sys.path.append(R'D:\Jake\blender-addons\modules')

import numpy as np
from os.path import join, abspath
#from smpl_webuser import serialization
from flame_fitting.smpl_webuser.serialization import load_model, save_model
from flame_fitting.fitting.util import write_simple_obj, safe_mkdir

# -----------------------------------------------------------------------------


def gen_pose(model):
    # Change Pose
    model.pose[:]  = np.random.randn( model.pose.size ) * 0.05

    return model


def gen_shape(model):
    # Change Shape
    model.betas[0:299] = np.random.randn( model.betas[0:299].size ) * 1.0

    return model


def gen_express(model):
    # Change Expression
    model.betas[300:] = np.random.randn( model.betas[300:].size ) * 1.0

    return model


def save_output(model, fname, outmesh_dir='./output'):
    safe_mkdir( outmesh_dir )
    outmesh_path = join( outmesh_dir, fname )
    write_simple_obj( mesh_v=model.r, mesh_f=model.f, filepath=outmesh_path )

    return outmesh_path


def gen_all(model_path='./models/generic_model.pkl', outmesh_dir='./output'):

    print("loading model from:", model_path)
    model = load_model( model_path )
    print("loaded model from:", model_path)

    gen_express(gen_pose(gen_shape(model)))

    saved_fpath = save_output(model, "blender_out.obj", outmesh_dir)
    print("Output Saved to:", saved_fpath)
    return abspath(saved_fpath)


def gen_test_models(model_path, model_type, shape_no=0):
    
    model = load_model( model_path )
    print("loaded model from:", model_path)

    new_model = gen_shape(model)
    save_output(new_model, "{}_shape{}.obj".format(model_type, shape_no))

    nTrys=5

    for i in range(1, nTrys):
        output_name = '{}_shape{}_express{}.obj'.format(model_type,shape_no,i)
        print(output_name)
        ex_model = gen_express(new_model)
        save_output(ex_model, output_name)
    
    model.betas[300:]  = np.zeros( model.betas[300:].size )

    for i in range(1, nTrys):
        output_name = '{}_shape{}_pose{}.obj'.format(model_type,shape_no,i)
        print(output_name)
        pose_model = gen_pose(new_model)
        save_output(pose_model, output_name)
        
    model.pose[:] = np.zeros( model.pose.size )


if __name__ == '__main__':

    # Load FLAME model (here we load the female model)
    # Make sure path is correct
    fem_model_path = './models/female_model.pkl'
    man_model_path = './models/male_model.pkl'
    gen_model_path = './models/generic_model.pkl'

    # -----------------------------------------------------------------------------

    # Assign random pose and shape parameters
    gen_test_models(fem_model_path, "female")
    gen_test_models(man_model_path, "male")
    gen_test_models(gen_model_path, "generic")


    # Print message
    #print 'output mesh saved to: ', outmesh_path 

