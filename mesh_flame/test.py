import os.path
try:
    from flame_utils import gen_util
except ImportError as e:
    print("Import error({0}): {1}".format(e.errno, e.strerror))


if __name__ == '__main__':
    fname = os.path.join(R'D:\Jake\FaceModels\flame\postech-flame-fitting\models', "generic_model.pkl")
    #fname = os.path.join(R'/mnt/d/Jake/FaceModels/flame/postech-flame-fitting/models', "generic_model.pkl")
    if os.path.isfile(fname):
        print("File Exists")
    else:
        print("File Does Not Exist")

    outfile = gen_util.gen_all(R'D:\Jake\FaceModels\flame\postech-flame-fitting\models\generic_model.pkl')
    #outfile = gen_util.gen_all('D:\\Jake\FaceModels\\flame\\postech-flame-fitting\\models\\female_model.pkl')
    #outfile = gen_util.gen_all('/mnt/d/Jake/FaceModels/flame/postech-flame-fitting/models/generic_model.pkl')
    #outfile = gen_util.gen_all(fname)
    print("Output:", outfile)

