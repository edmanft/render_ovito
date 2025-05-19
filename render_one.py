import sys
import os
from ovito.io import import_file
from ovito.vis import Viewport, TachyonRenderer
from ovito.pipeline import StaticSource

# Args
xyz_filename = sys.argv[1]
movie_name = sys.argv[2]
output_dir = sys.argv[3]

# Views
views = {
    "top":    ((0, 0, -1), (0, 1, 0)),                    # Looking down from +Z
    "front":  ((-1, 1, 0), (0, 0, 1))                     # 45° in XY, up is Z
}

# Settings
render_size = (1600, 1200)
fps = 2

# Load trajectory
pipeline = import_file(xyz_filename)
pipeline.add_to_scene()

# Remove the simulation cell (box)
pipeline.source.data.cell.vis.enabled = False

# Render views
for view_name, (direction, up_vector) in views.items():
    vp = Viewport(type=Viewport.Type.Perspective)
    vp.camera_dir = direction
    vp.camera_up = up_vector
    vp.zoom_all()

    output_file = os.path.join(output_dir, f"{movie_name}_{view_name}.avi")
    print(f"🎬 Rendering {output_file} ...")

    vp.render_anim(
        filename=output_file,
        size=render_size,
        fps=fps,
        renderer=TachyonRenderer()
    )

# Cleanup
pipeline.remove_from_scene()
