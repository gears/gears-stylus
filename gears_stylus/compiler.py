import os
import re
from pkg_resources import iter_entry_points

from gears.asset_attributes import AssetAttributes
from gears.compilers import ExecCompiler


IMPORT_RE = re.compile(r"""@import\s+(['"]?)(.*?)\1""")


class StylusCompiler(ExecCompiler):

    result_mimetype = 'text/css'
    executable = 'node'
    params = [os.path.join(os.path.dirname(__file__), 'compiler.js')]

    def __init__(self, *args, **kwargs):
        self.paths = []
        super(StylusCompiler, self).__init__(*args, **kwargs)
        for entry_point in iter_entry_points('gears_stylus', 'register'):
            register = entry_point.load()
            register(self)

    def __call__(self, asset):
        self.asset = asset
        self.register_dependencies()
        super(StylusCompiler, self).__call__(asset)

    def get_args(self):
        args = super(StylusCompiler, self).get_args()
        args.append(self.asset.absolute_path)
        args.extend(self.paths)
        return args

    def register_dependencies(self):
        for match in IMPORT_RE.findall(self.asset.processed_source):
            path = self.get_relative_path(match[1].split('?')[0])
            list = self.asset.attributes.environment.list(path, self.asset.attributes.mimetype)
            for asset_attributes, absolute_path in list:
                self.asset.dependencies.add(absolute_path)

    def get_relative_path(self, import_path):
        import_path = os.path.join(self.asset.attributes.dirname, import_path)
        return os.path.normpath(import_path)
