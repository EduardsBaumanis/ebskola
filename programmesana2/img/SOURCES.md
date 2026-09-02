# Programmēšana II screenshot source audit

Audit date: 2026-09-02

## Current status

- The lesson HTML files reference 65 PNG files in `programmesana2/img`.
- All 65 referenced files are present; no broken local image paths were found.
- `topic1_godot_pm.png` is a real screenshot.
- The other 64 PNG files are placeholder images with the same diagonal stripe pattern.
- No placeholders were overwritten in this pass; the table below separates good
  candidates from approximate ones.

## License-safe internet buckets found

- Godot official documentation screenshots: CC BY 3.0. Attribution required to "Juan Linietsky, Ariel Manzur and the Godot community". License note: `https://docs.godotengine.org/en/stable/about/faq.html`
- Godot official demo project screenshots: MIT license, from `godotengine/godot-demo-projects`. License note: `https://github.com/godotengine/godot-demo-projects`

## Candidate matches

| Local target | HTML lesson context | Candidate source | Fit |
| --- | --- | --- | --- |
| `topic1_editor_layout.png` | 1.1 editor first open: Scene Tree, FileSystem, Viewport, Inspector | `https://docs.godotengine.org/en/4.0/_images/editor_intro_editor_empty.webp` | Good official match |
| `topic1_scene_tree.png` | 1.2 Pong scene hierarchy | `https://docs.godotengine.org/en/4.0/_images/editor_intro_scene_dock.webp` | Only generic Scene dock; does not show Pong nodes |
| `topic1_inspector.png` | 1.2 Inspector with selected `CharacterBody2D` transform values | `https://docs.godotengine.org/en/4.0/_images/editor_intro_inspector_dock.webp` | Generic Inspector; node type differs |
| `topic1_create_node.png` | 1.4 Add Child Node with custom `Hello` class | `https://docs.godotengine.org/en/stable/_images/globalclasses_addnode.webp` | Shows a custom class, but not `Hello` or GDExtension |
| `topic1_project_settings.png` | 1.5 Display -> Window, viewport 1280x720 | `https://docs.godotengine.org/en/4.5/_images/03.window_settings.webp` | Same settings screen; dimensions differ |
| `topic1_input_map.png`, `topic2_input_map.png` | Input Map with course-specific action names | `https://docs.godotengine.org/en/4.7/_images/inputs_inputmap.webp` | Same UI; action names differ |
| `topic1_pong_layout.png`, `topic1_pong_running.png` | Pong layout/running state | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/2d/pong/screenshots/pong.png` | Official Pong screenshot; score/AI state differ |
| `topic2_level1.png`, `topic2_player_moving.png`, `topic2_pickups.png`, `topic2_score_hud.png` | Platformer gameplay/HUD/pickups | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/2d/platformer/screenshots/platformer.webp` | Good theme match; exact HUD/finish state differs |
| `topic2_jump_arc.png` | Jump arc diagram | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/2d/physics_platformer/screenshots/beginning.png` | Platformer reference only; no arc overlay |
| `topic3_rpg_battle.png` | Class tournament battle simulator | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/2d/role_playing_game/screenshots/battle.png` | Battle UI match; course-specific class-tournament UI differs |
| `topic4_bullets_pool.png` | Many bullets/object pooling | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/2d/bullet_shower/screenshots/collision.png` | Good official match for many projectiles |
| `topic4_navmesh.png` | Baked navigation mesh in editor | `https://docs.godotengine.org/en/4.5/_images/nav_mesh_mini_2d.webp` | Good official match |
| `topic4_pathfinding_demo.png` | Enemy paths around obstacle | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/2d/navigation_astar/screenshots/navigation_astar.webp` | A* pathfinding match; game objects differ |
| `topic5_save_slots.png` | Save/Load UI with three slots | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/loading/serialization/screenshots/save_load.png` | Save/load concept match; slot UI differs |
| `topic5_profiler.png`, `topic6_profiler.png` | Godot Profiler function timing table and graph | `https://docs.godotengine.org/en/4.5/_images/profiler.png` | Good official match |
| `topic6_audio_bus.png` | Audio Bus editor with sliders and mute controls | `https://docs.godotengine.org/en/4.5/_images/audio_buses1.webp` | Good official match; bus names differ |
| `topic6_animation_editor.png` | AnimationPlayer timeline with keyframes | `https://docs.godotengine.org/en/4.5/_images/animation_animation_panel_overview.webp` | Same editor panel; no walk keyframes |
| `topic6_debugger.png` | Debugger at breakpoint with stack/locals | `https://docs.godotengine.org/en/4.5/_images/overview_debugger.webp` | Same debugger panel; no active breakpoint values |
| `topic6_export_dialog.png` | Web export dialog | `https://docs.godotengine.org/en/4.5/_images/export_dialog.webp` | Export dialog match; not Web preset-specific |

## Images that still need custom screenshots

These targets are too specific to replace safely with internet screenshots without changing the lesson meaning: `topic1_cpp_output.png`, `topic1_scons_build.png`, `topic2_collision_layers.png`, `topic2_fps_debug.png`, `topic2_game_complete.png`, `topic2_hud.png`, `topic2_movement.png`, `topic2_pickups_collected.png`, `topic3_class_hierarchy.png`, `topic3_hero_class.png`, `topic3_inheritance_tree.png`, `topic3_inspector_custom.png`, `topic3_signals_diagram.png`, `topic3_stats_panel.png`, `topic3_uml_class.png`, `topic4_ai_chase.png`, `topic4_enemy_spawn.png`, `topic4_inventory_ui.png`, `topic4_state_diagram.png`, `topic4_topdown_gameplay.png`, `topic4_wave_ui.png`, `topic5_big_o_chart.png`, `topic5_meta_progress.png`, `topic5_random_walk.png`, `topic5_resource_inspector.png`, `topic5_roguelike_gameplay.png`, `topic5_rooms_corridors.png`, `topic5_save_json.png`, `topic5_user_data_folder.png`, `topic6_damage_popup.png`, `topic6_github_pages.png`, `topic6_github_release.png`, `topic6_hud.png`, `topic6_main_menu.png`, `topic6_published_url.png`, `topic6_puzzle_game.png`, `topic6_settings_panel.png`, `topic6_sound_effects.png`, `topic6_web_game_running.png`.
