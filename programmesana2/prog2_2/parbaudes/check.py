#!/usr/bin/env python3
"""Build lesson checkpoints and exercise the final game in a temporary Godot project."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument('--godot', required=True, help='Godot .NET executable')
parser.add_argument('--dotnet', default='dotnet', help='.NET SDK executable')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
dotnet = Path(shutil.which(args.dotnet) or args.dotnet).resolve()
godot = str(Path(shutil.which(args.godot) or args.godot).resolve())
env = dict(os.environ, DOTNET_ROOT=str(dotnet.parent), DOTNET_CLI_TELEMETRY_OPTOUT='1')
env['PATH'] = str(dotnet.parent) + os.pathsep + env['PATH']

def run(command, cwd):
    result = subprocess.run(command, cwd=cwd, env=env, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, timeout=90)
    print(result.stdout)
    if result.returncode or 'ERROR:' in result.stdout:
        raise SystemExit(result.returncode or 1)
    return result.stdout

with tempfile.TemporaryDirectory(prefix='ebskola-platformer-') as temp:
    temp = Path(temp)
    for stage in ['2_1', '2_2', '2_3']:
        checkpoint = temp / stage
        shutil.copytree(root / 'kods' / stage, checkpoint)
        shutil.copy(root / 'platformer/Platformer.csproj', checkpoint)
        run([str(dotnet), 'build', '--nologo'], checkpoint)
    project = temp / 'Platformer'
    shutil.copytree(root / 'platformer', project,
                    ignore=shutil.ignore_patterns('.godot', 'bin', 'obj'))
    shutil.copy(root / 'parbaudes/SmokeTest.cs', project)
    (project / 'SmokeTest.tscn').write_text('''[gd_scene load_steps=2 format=3]
[ext_resource type="Script" path="res://SmokeTest.cs" id="1"]
[node name="SmokeTest" type="Node"]
script = ExtResource("1")
''')
    run([str(dotnet), 'build', '--nologo'], project)
    run([godot, '--headless', '--path', str(project), '--editor', '--import', '--quit'], project)
    output = run([godot, '--headless', '--path', str(project), '--fixed-fps', '60',
         '--quit-after', '5000', 'res://SmokeTest.tscn'], project)

    if 'SUCCESS:' not in output:
        raise SystemExit('The game checks did not finish.')
