# Programmēšana II screenshot (ekrānuzņēmums) source audit

Audit date: 2026-09-02

## Current status

- The lesson HTML (hiperteksta iezīmēšanas valoda) files (faili) reference (atsauce) 65 PNG (bezzudumu attēlu formāts) files (faili) in `programmesana2/img`.
- All 65 referenced files (faili) are present; no broken local (rediģējamais skats) image paths were found.
- `topic1_godot_pm.png` is a real screenshot (ekrānuzņēmums).
- The other 64 PNG (bezzudumu attēlu formāts) files (faili) are placeholder images with the same diagonal stripe pattern.
- No placeholders were overwritten in this pass; the table below separates good
  candidates from approximate ones.

## License-safe internet (internets) buckets found

- Godot official documentation screenshots (ekrānuzņēmums): CC BY 3.0. Attribution required to "Juan Linietsky, Ariel Manzur and the Godot community". License note: `https://docs.godotengine.org/en/stable/about/faq.html`
- Godot official demo project (projekts) screenshots (ekrānuzņēmums): MIT license, from `godotengine/godot-demo-projects`. License note: `https://github.com/godotengine/godot-demo-projects`

## Candidate matches

| Local (rediģējamais skats) target | HTML (hiperteksta iezīmēšanas valoda) lesson context | Candidate source | Fit |
| --- | --- | --- | --- |
| `topic1_editor_layout.png` | 1.1 editor (redaktors) first open (atvērt): Scene Tree (scēnu koks), FileSystem (failu sistēma), Viewport (skatlogs), Inspector (īpašību panelis) | `https://docs.godotengine.org/en/4.0/_images/editor_intro_editor_empty.webp` | Good official match |
| `topic1_scene_tree.png` | 1.2 Pong scene (scēna) hierarchy (hierarhija) | `https://docs.godotengine.org/en/4.0/_images/editor_intro_scene_dock.webp` | Only generic Scene dock (scēnas panelis); does not show Pong nodes (mezgli) |
| `topic1_inspector.png` | 1.2 Inspector (īpašību panelis) with selected `CharacterBody2D` (vadāma 2D tēla mezgls) transform (pārveidojums) values | `https://docs.godotengine.org/en/4.0/_images/editor_intro_inspector_dock.webp` | Generic Inspector (īpašību panelis); node (mezgls) type (tips) differs |
| `topic1_create_node.png` | 1.4 Add Child Node (pievienot bērna mezglu) with custom (pielāgots) `Hello` class (klase) | `https://docs.godotengine.org/en/stable/_images/globalclasses_addnode.webp` | Shows a custom (pielāgots) class (klase), but not `Hello` exactly |
| `topic1_project_settings.png` | 1.5 Display (attēlojums) -> Window (logs), viewport (skatlogs) 1280x720 | `https://docs.godotengine.org/en/4.5/_images/03.window_settings.webp` | Same settings (iestatījumi) screen (ekrāns); dimensions differ |
| `topic1_input_map.png`, `topic2_input_map.png` | Input Map (ievades darbību karte) with course-specific action names | `https://docs.godotengine.org/en/4.7/_images/inputs_inputmap.webp` | Same UI (lietotāja saskarne); action names differ |
| `topic1_pong_layout.png`, `topic1_pong_running.png` | Pong layout (izkārtojums)/running state (stāvoklis) | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/2d/pong/screenshots/pong.png` | Official Pong screenshot (ekrānuzņēmums); score/AI (mākslīgais intelekts) state (stāvoklis) differ |
| `topic2_level1.png`, `topic2_player_moving.png`, `topic2_pickups.png`, `topic2_score_hud.png` | Platformer (platformas spēle) gameplay (spēles norise)/HUD (spēles informācijas panelis)/pickups | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/2d/platformer/screenshots/platformer.webp` | Good theme (noformējuma tēma) match; exact HUD (spēles informācijas panelis)/finish state (stāvoklis) differs |
| `topic2_jump_arc.png` | Jump arc diagram | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/2d/physics_platformer/screenshots/beginning.png` | Platformer (platformas spēle) reference (atsauce) only; no arc overlay |
| `topic3_rpg_battle.png` | Class (klase) tournament battle simulator (simulators) | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/2d/role_playing_game/screenshots/battle.png` | Battle UI (lietotāja saskarne) match; course-specific class-tournament UI (lietotāja saskarne) differs |
| `topic4_bullets_pool.png` | Many bullets/object pooling (objektu atkārtota izmantošana) | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/2d/bullet_shower/screenshots/collision.png` | Good official match for (skaitītāja cikls) many projectiles |
| `topic4_navmesh.png` | Baked navigation mesh (navigācijas tīkls) in editor (redaktors) | `https://docs.godotengine.org/en/4.5/_images/nav_mesh_mini_2d.webp` | Good official match |
| `topic4_pathfinding_demo.png` | Enemy paths around obstacle | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/2d/navigation_astar/screenshots/navigation_astar.webp` | A* pathfinding (ceļa meklēšana) match; game objects (objekti) differ |
| `topic5_save_slots.png` | Save/Load (saglabāšana/ielāde) UI (lietotāja saskarne) with three slots (saglabāšanas vietas) | `https://raw.githubusercontent.com/godotengine/godot-demo-projects/master/loading/serialization/screenshots/save_load.png` | Save/load (saglabāšana/ielāde) concept match; slot (saglabāšanas vieta) UI (lietotāja saskarne) differs |
| `topic5_profiler.png`, `topic6_profiler.png` | Godot Profiler (profilētājs) function (funkcija) timing table and graph | `https://docs.godotengine.org/en/4.5/_images/profiler.png` | Good official match |
| `topic6_audio_bus.png` | Audio Bus (skaņas kopne) editor (redaktors) with sliders (slīdnis) and mute controls | `https://docs.godotengine.org/en/4.5/_images/audio_buses1.webp` | Good official match; bus (skaņas kopne) names differ |
| `topic6_animation_editor.png` | AnimationPlayer (animāciju atskaņotājs) timeline (laika skala) with keyframes (atslēgkadrs) | `https://docs.godotengine.org/en/4.5/_images/animation_animation_panel_overview.webp` | Same editor (redaktors) panel (panelis); no walk keyframes (atslēgkadrs) |
| `topic6_debugger.png` | Debugger (atkļūdotājs) at breakpoint (pārtraukumpunkts) with stack (steks)/locals (vietējie mainīgie) | `https://docs.godotengine.org/en/4.5/_images/overview_debugger.webp` | Same debugger (atkļūdotājs) panel (panelis); no active breakpoint (pārtraukumpunkts) values |
| `topic6_export_dialog.png` | Desktop (darbvirsma) export (eksportēt) dialog | `https://docs.godotengine.org/en/4.5/_images/export_dialog.webp` | Export (eksportēt) dialog match; not desktop (darbvirsma) preset-specific |

## Images that still need custom (pielāgots) screenshots (ekrānuzņēmums)

These targets are too specific to replace safely with internet (internets) screenshots (ekrānuzņēmums) without changing the lesson meaning: `topic1_csharp_output.png`, `topic1_dotnet_build.png`, `topic2_collision_layers.png`, `topic2_fps_debug.png`, `topic2_game_complete.png`, `topic2_hud.png`, `topic2_movement.png`, `topic2_pickups_collected.png`, `topic3_class_hierarchy.png`, `topic3_hero_class.png`, `topic3_inheritance_tree.png`, `topic3_inspector_custom.png`, `topic3_signals_diagram.png`, `topic3_stats_panel.png`, `topic3_uml_class.png`, `topic4_ai_chase.png`, `topic4_enemy_spawn.png`, `topic4_inventory_ui.png`, `topic4_state_diagram.png`, `topic4_topdown_gameplay.png`, `topic4_wave_ui.png`, `topic5_big_o_chart.png`, `topic5_meta_progress.png`, `topic5_random_walk.png`, `topic5_resource_inspector.png`, `topic5_roguelike_gameplay.png`, `topic5_rooms_corridors.png`, `topic5_save_json.png`, `topic5_user_data_folder.png`, `topic6_damage_popup.png`, `topic6_github_pages.png`, `topic6_github_release.png`, `topic6_hud.png`, `topic6_main_menu.png`, `topic6_published_url.png`, `topic6_puzzle_game.png`, `topic6_settings_panel.png`, `topic6_sound_effects.png`, `topic6_web_game_running.png`.
