#!/usr/bin/env python3
"""Build the lesson scripts and run real Godot physics checks in temporary copies."""
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
    result = subprocess.run(command, cwd=cwd, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=90)
    print(result.stdout)
    if result.returncode or 'ERROR:' in result.stdout:
        raise SystemExit(result.returncode or 1)
    return result.stdout

with tempfile.TemporaryDirectory(prefix='ebskola-pong-') as temp:
    temp = Path(temp)
    for stage in ['1_3', '1_4', '1_5']:
        checkpoint = temp / stage
        checkpoint.mkdir()
        sources = sorted((root / 'kods' / stage).glob('*.cs')) if stage != '1_5' else [root / 'pong/Scripts/Paddle.cs', root / 'pong/Scripts/Ball.cs']
        for source in sources:
            shutil.copy(source, checkpoint)
        shutil.copy(root / 'pong/Pong.csproj', checkpoint)
        run([str(dotnet), 'build', '--nologo'], checkpoint)
    project = temp / 'Pong'
    shutil.copytree(root / 'pong', project, ignore=shutil.ignore_patterns('.godot', 'bin', 'obj'))
    shutil.copy(root / 'parbaudes/SmokeTest.cs', project)
    (project / 'SmokeTest.tscn').write_text('''[gd_scene load_steps=2 format=3]
[ext_resource type="Script" path="res://SmokeTest.cs" id="1"]
[node name="SmokeTest" type="Node"]
script = ExtResource("1")
''')
    # Same scene geometry as the lessons, before the controller is attached in 1.6.
    stage5 = (project / 'Scenes/Main.tscn').read_text().replace('load_steps=5', 'load_steps=4')
    stage5 = stage5.replace('[ext_resource type="Script" path="res://Scripts/Game.cs" id="1"]\n', '')
    stage5 = stage5.replace('script = ExtResource("1")\n', '')
    (project / 'Scenes/Stage5.tscn').write_text(stage5)
    run([str(dotnet), 'build', '--nologo'], project)
    run([godot, '--headless', '--path', str(project), '--editor', '--import', '--quit'], project)
    for extra in [['--', '--stage5'], []]:
        output = run([godot, '--headless', '--path', str(project), '--fixed-fps', '60',
                      '--quit-after', '5000', 'res://SmokeTest.tscn'] + extra, project)
        if 'SUCCESS:' not in output:
            raise SystemExit('Game checks did not finish.')
