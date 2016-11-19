from skimage import io
from lensfunpy import Database, Modifier
from lensfunpy.util import remap

db = Database()
cam = db.find_cameras(maker="Sony", model="ILCE-5000")[0]
lens = db.find_lenses(cam, maker="Sony", lens="E PZ 16-50mm f/3.5-5.6 OSS")[0]

# Photo params
focal_length = 16
aperture = 3.5
distance = 2  # approx meters to focus point

img = io.imread("DSC06586.jpg")
height, width, depth = img.shape

mod = Modifier(lens, cam.crop_factor, width, height)
mod.initialize(focal_length, aperture, distance)
undist_coords = mod.apply_geometry_distortion()

im_undist = remap(img, undist_coords)
io.imsave('DSC06586_undist.jpg', im_undist)
print("Distortion removed. Photo saved")