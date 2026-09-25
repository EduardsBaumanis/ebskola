using Godot;
using System;
using System.Threading.Tasks;

// Runs in a temporary copy, outside the downloadable student project.
public partial class SmokeTest : Node
{
    private Level level;
    private Player player;
    private int checks;

    public override void _Ready()
    {
        Callable.From(Run).CallDeferred();
    }

    private void Check(bool condition, string description)
    {
        if (!condition) throw new Exception(description);
        checks++;
        GD.Print("PASS: " + description);
    }

    private async Task Frames(int count)
    {
        for (int i = 0; i < count; i++)
        {
            await ToSignal(GetTree(), SceneTree.SignalName.PhysicsFrame);
            await ToSignal(GetTree(), SceneTree.SignalName.ProcessFrame);
        }
    }

    private void ReadScene()
    {
        level = (Level)GetTree().CurrentScene;
        player = level.GetNode<Player>("Player");
    }

    private async Task Restart()
    {
        Input.ActionPress("restart");
        await Frames(3);
        Input.ActionRelease("restart");
        await Frames(60);
        ReadScene();
        Check(!level.GameEnded && player.IsActive, "R restarts an active game");
        Check(player.Score == 0 && !player.HasKey, "R resets inventory");
        Check(level.HasNode("Coin1") && level.HasNode("Key"), "R restores pickups");
        Check(Mathf.Abs(player.Position.X - 80) < 1 && player.IsOnFloor(), "R restores spawn and ground contact");
    }

    private async Task Place(Vector2 position)
    {
        player.Position = position;
        player.Velocity = Vector2.Zero;
        await Frames(6);
    }

    private async Task JumpRight(int frames)
    {
        Check(player.IsOnFloor(), "Jump starts on a platform");
        Input.ActionPress("jump");
        Input.ActionPress("move_right");
        await Frames(frames);
        Input.ActionRelease("move_right");
        Input.ActionRelease("jump");
        await Frames(50);
        Check(!level.GameEnded && player.IsOnFloor(), "Jump lands safely");
    }

    private async void Run()
    {
        try
        {
            var packed = GD.Load<PackedScene>("res://Scenes/Level1.tscn");
            level = packed.Instantiate<Level>();
            GetTree().Root.AddChild(level);
            GetTree().CurrentScene = level;
            ReadScene();
            await Frames(60);
            Check(player.IsOnFloor(), "Player lands on ground");
            Check(player.Score == 0 && !player.HasKey, "Fresh game has empty inventory");
            Check(level.GetNode<Label>("HUD/Instructions").Text.Contains("Space"), "HUD displays controls");
            foreach (var pair in new[] { ("move_left", Key.Left), ("move_right", Key.Right), ("jump", Key.Space), ("restart", Key.R) })
                Check(InputMap.ActionHasEvent(pair.Item1, new InputEventKey { PhysicalKeycode = pair.Item2 }), pair.Item1 + " keyboard binding");

            Input.ActionPress("move_right");
            await Frames(24);
            Input.ActionRelease("move_right");
            await Frames(2);
            Check(player.Position.X > 180 && player.Position.X < 210, "Horizontal speed and stopping");
            Check(player.Score == 1 && !level.HasNode("Coin1"), "BodyEntered collects a coin exactly once");
            await Frames(10);
            Check(player.Score == 1, "No repeated coin award");
            await Restart(); // Also verifies R while the game is active.

            // Traverse the three platforms with actual input, without teleporting.
            await JumpRight(40);
            Check(Mathf.Abs(player.Position.Y - 526) < 2, $"Platform 1 is reachable: {player.Position}");
            await JumpRight(40);
            Check(Mathf.Abs(player.Position.Y - 436) < 2, $"Platform 2 is reachable: {player.Position}");
            await JumpRight(40);
            Check(Mathf.Abs(player.Position.Y - 346) < 2 && player.HasKey, "Platform 3 and key are reachable");
            Check(player.Score == 6, "Route collects one coin and one gem");
            Input.ActionPress("move_right");
            await Frames(34);
            Input.ActionRelease("move_right");
            await Frames(80);
            Check(level.GameEnded && !player.IsActive, "Route reaches the finish and wins");
            Check(level.GetNode<Label>("HUD/Message").Text.Contains(level.WinText), "Story ending is visible");
            float endX = player.Position.X;
            Input.ActionPress("move_right");
            await Frames(12);
            Input.ActionRelease("move_right");
            Check(Mathf.IsEqualApprox(player.Position.X, endX), "Movement stops after winning");
            int endScore = player.Score;
            player.OnPickup(PickupType.Gem);
            Check(player.Score == endScore, "Inventory is frozen after winning");
            await Restart();

            await Place(new Vector2(850, 610));
            Check(!level.GameEnded && player.IsActive, "Finish refuses player without key");
            Check(level.GetNode<Label>("HUD/Message").Text == level.LockedText, "Locked finish gives a hint");
            await Place(new Vector2(440, 610));
            Check(level.GameEnded && !player.IsActive, "Hazard causes loss");
            Check(level.GetNode<Label>("HUD/Message").Text.Contains(level.LoseText), "Loss text is visible");
            await Restart();
            await Place(new Vector2(-80, 790));
            await Frames(30);
            Check(level.GameEnded && !player.IsActive, "Falling out of the level causes loss");
            await Restart();

            // The jump button cannot refresh vertical speed while airborne.
            Input.ActionPress("jump");
            await Frames(5);
            Input.ActionRelease("jump");
            await Frames(3);
            float before = player.Velocity.Y;
            Input.ActionPress("jump");
            await Frames(2);
            Input.ActionRelease("jump");
            Check(player.Velocity.Y > before, "Airborne jump press cannot reset upward velocity");
            await Frames(70);
            Check(player.IsOnFloor(), "Player lands after jump");
            await Restart();
            foreach (string name in new[] { "Coin1", "Coin2", "Gem", "Coin3", "Coin4", "Key" })
            {
                var pickup = level.GetNode<Area2D>(name);
                await Place(pickup.Position);
            }
            Check(player.Score == 9 && player.HasKey, "All five point pickups and key have correct totals");
            Check(level.GetNode<Label>("HUD/Status").Text.Contains("9"), "HUD reflects collected score");
            GD.Print($"SUCCESS: {checks} checks");
            GetTree().Quit();
        }
        catch (Exception exception)
        {
            GD.PushError(exception.ToString());
            GetTree().Quit(1);
        }
    }
}
