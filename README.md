<h1>📽️ OVITO Rendering Pipeline for Molecular Trajectories</h1>

<p>This pipeline batch-renders <code>.xyz</code> trajectory files using OVITO from two perspectives:</p>
<ul>
  <li><strong>Top view</strong> (looking down Z)</li>
  <li><strong>45° front view</strong> (XY diagonal)</li>
</ul>

<p>Each trajectory is rendered in an isolated subprocess to avoid memory leaks and global state issues.</p>

<h2>📁 Folder Structure</h2>
<pre><code>create_avi_movies_spectroscopies/
├── pp_xyz_movies/              # Input .xyz files
│   ├── movie_S1_h2o_top_o_hb.xyz
│   ├── ...
├── rendered_movies/            # Output .avi files
│   ├── movie_S1_h2o_top_o_hb_top.avi
│   ├── movie_S1_h2o_top_o_hb_front.avi
├── render_one.py               # Renders one trajectory
├── main_render.py              # Loops over and renders all trajectories
</code></pre>

<h2>🧪 Environment Setup</h2>

<p><strong>Always follow the official installation instructions when available.</strong></p>

<h3>1. Create a clean environment</h3>
<pre><code>conda create -n render_ovito python=3.10
conda activate render_ovito
</code></pre>

<h3>2. Install OVITO properly (important!)</h3>
<pre><code>conda install --strict-channel-priority \
  -c https://conda.ovito.org \
  -c conda-forge \
  ovito=3.12.3
</code></pre>

<h3>3. (Optional) Add support for Jupyter + ASE</h3>
<pre><code>conda install -c conda-forge ase ipython jupyterlab
</code></pre>

<h2>▶️ How the Code Works</h2>

<h3><code>main_render.py</code></h3>
<ul>
  <li>Cleans <code>rendered_movies/</code> (removes files only)</li>
  <li>Creates <code>TMP/</code> folder inside <code>pp_xyz_movies/</code></li>
  <li>For each <code>.xyz</code> file:
    <ul>
      <li>Copies it into a temp folder</li>
      <li>Calls <code>render_one.py</code> as a subprocess</li>
      <li>Moves resulting movies to <code>rendered_movies/</code></li>
    </ul>
  </li>
</ul>

<h3><code>render_one.py</code></h3>
<ul>
  <li>Loads the trajectory using OVITO</li>
  <li>Hides the simulation cell</li>
  <li>Renders two perspectives:
    <ul>
      <li><strong>Top view</strong>: camera_dir = (0, 0, -1)</li>
      <li><strong>Front view</strong>: camera_dir = (-1, 1, 0)</li>
    </ul>
  </li>
  <li>Uses <code>TachyonRenderer</code> for ray-traced images</li>
</ul>

<h2>✅ Notes</h2>
<ul>
  <li>Output format is <code>.avi</code></li>
  <li>Rendering is sandboxed to avoid OVITO bugs</li>
  <li>Tested with OVITO <code>3.12.3</code> from official channel</li>
</ul>
</body>
</html>
