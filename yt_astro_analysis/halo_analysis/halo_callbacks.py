"""
Halo callback object.

Author: Britton Smith <brittonsmith@gmail.com>
Affiliation: Michigan State University
Author: Matthew Turk <matthewturk@gmail.com>
Affiliation: Columbia University
Homepage: http://yt-project.org/
License:
  Copyright (C) 2013 Britton Smith, Matthew Turk.  All Rights Reserved.

  This file is part of yt.

  yt is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

class HaloCallback(object):
    def __init__(self, function, args, kwargs):
        self.function = function
        self.args
        self.kwargs

    def __call__(self, halo_catalog, halo):
        self.function(halo_catalog, halo, *self.args, **self.kwargs)
        return True

    def initialize(self, halo_catalog):
        pass

    def finalize(self, halo_catalog):
        pass

class SaveParticles(object):
    def __init__(self, filename, arr_names = ("particle_ids")):
        self.filename = filename
        self.arr_names = arr_names
        self.handle = None

    def initialize(self, halo_catalog):
        self.handle = h5py.File(self.filename)

    def __call__(self, halo_catalog, halo):
        g = self.handle.create_group("/Halo%08i" % halo.halo_id)
        for arr in arr_names:
            g.create_dataset(arr, data=halo[arr])

    def finalize(self, halo_catalog):
        self.handle.close()
