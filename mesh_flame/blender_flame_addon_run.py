import os
import sys
#sys.path.append(R'D:\Jake\FaceModels\flame\blender_flame')
#sys.path.append(R'D:\Jake\FaceModels\flame\postech-flame-fitting')

filename = os.path.join(R'D:\Jake\blender-addons\addons\mesh_flame', "blender_flame_addon.py")
exec(compile(open(filename).read(), filename, 'exec'))
