using Godot;
using System;
using System.Threading.Tasks;

// Executed only in a temporary project by check.py.
public partial class SmokeTest : Node
{
    private Node2D main;
    private Game game;
    private Ball ball;
    private Paddle left;
    private Paddle right;
    private int checks;

    public override void _Ready() => Callable.From(Run).CallDeferred();

    private void Check(bool value, string description)
    {
        if (!value) throw new Exception(description);
        GD.Print("PASS: " + description);
        checks++;
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
        main = (Node2D)GetTree().CurrentScene;
        game = main as Game;
        ball = main.GetNode<Ball>("Ball");
        left = main.GetNode<Paddle>("PaddleLeft");
        right = main.GetNode<Paddle>("PaddleRight");
    }

    private async Task Press(string action, int frames)
    {
        Input.ActionPress(action);
        await Frames(frames);
        Input.ActionRelease(action);
        await Frames(2);
    }

    private async Task Restart()
    {
        await Press("restart", 3);
        ReadScene();
        Check(!game.GameOver && game.ScoreLeft == 0 && game.ScoreRight == 0, "R resets scores and winner");
        Check(!ball.IsMoving && ball.ExitSide == 0 && ball.Position == new Vector2(640, 360), "R restores ball and serve wait");
        Check(left.Position == new Vector2(60, 360) && right.Position == new Vector2(1220, 360), "R restores paddles");
        Check(left.IsActive && right.IsActive, "R restores controls");
    }

    private async Task Score(bool forLeft)
    {
        ball.ResetBall();
        ball.Position = new Vector2(forLeft ? 1288 : -8, 360);
        ball.Serve(forLeft ? 1 : -1);
        ball.Velocity = new Vector2(forLeft ? 420 : -420, 0);
        await Frames(6);
    }

    private async Task Bounce(Vector2 position, Vector2 velocity, string description)
    {
        ball.ResetBall();
        ball.Position = position;
        ball.Serve(1);
        ball.Velocity = velocity;
        await Frames(12);
        Check(ball.Velocity.Dot(velocity) < 0, description);
        Check(Mathf.Abs(ball.Velocity.Length() - velocity.Length()) < 0.1f, "Bounce preserves speed");
        ball.Stop();
    }

    private async void Run()
    {
        try
        {
            bool stage5 = Array.IndexOf(OS.GetCmdlineUserArgs(), "--stage5") >= 0;
            var scene = GD.Load<PackedScene>(stage5 ? "res://Scenes/Stage5.tscn" : "res://Scenes/Main.tscn");
            main = scene.Instantiate<Node2D>();
            GetTree().Root.AddChild(main);
            GetTree().CurrentScene = main;
            ReadScene();
            await Frames(3);
            Check(ball.IsMoving == stage5, stage5 ? "1.5 ball starts without Game" : "1.6 game waits for Space");
            ball.Stop();
            foreach (var pair in new[] { ("p1_up", Key.W), ("p1_down", Key.S), ("p2_up", Key.Up), ("p2_down", Key.Down), ("serve", Key.Space), ("restart", Key.R) })
                Check(InputMap.ActionHasEvent(pair.Item1, new InputEventKey { PhysicalKeycode = pair.Item2 }), pair.Item1 + " keyboard binding");

            await Press("p1_up", 20);
            Check(left.Position.Y < 240 && right.Position.Y == 360, "W moves only left paddle");
            float stoppedY = left.Position.Y;
            await Frames(10);
            Check(Mathf.Abs(left.Position.Y - stoppedY) < 0.01f, "Release stops paddle");
            Input.ActionPress("p1_up");
            Input.ActionPress("p1_down");
            await Frames(10);
            Input.ActionRelease("p1_up");
            Input.ActionRelease("p1_down");
            Check(Mathf.Abs(left.Position.Y - stoppedY) < 0.01f, "Opposite keys cancel");
            Input.ActionPress("p1_down");
            Input.ActionPress("p2_up");
            await Frames(8);
            Input.ActionRelease("p1_down");
            Input.ActionRelease("p2_up");
            Check(left.Position.Y > stoppedY && right.Position.Y < 360, "Both players can move simultaneously");
            await Press("p1_up", 100);
            await Press("p2_up", 100);
            Check(Mathf.Abs(left.Position.Y - 80) < 1 && Mathf.Abs(right.Position.Y - 80) < 1, "Top wall stops both paddles");
            await Press("p1_down", 150);
            await Press("p2_down", 150);
            Check(Mathf.Abs(left.Position.Y - 640) < 1 && Mathf.Abs(right.Position.Y - 640) < 1, "Bottom wall stops both paddles");
            left.Position = new Vector2(60, 360);
            right.Position = new Vector2(1220, 360);
            await Bounce(new Vector2(640, 40), new Vector2(0, -420), "Ball bounces off top wall");
            await Bounce(new Vector2(640, 680), new Vector2(0, 420), "Ball bounces off bottom wall");
            await Bounce(new Vector2(90, 360), new Vector2(-420, 0), "Ball bounces off left paddle");
            await Bounce(new Vector2(1190, 360), new Vector2(420, 0), "Ball bounces off right paddle");
            ball.ResetBall();
            ball.Serve(1);
            Check(Mathf.Abs(ball.Velocity.Length() - 420) < 0.1f && ball.Velocity.X > 0 && Mathf.Abs(ball.Velocity.Y) > 0, "Serve is normalized and angled");
            ball.Stop();

            if (stage5)
            {
                await Score(true);
                Check(ball.ExitSide == 1 && !ball.IsMoving, "1.5 right exit stops ball");
                await Score(false);
                Check(ball.ExitSide == -1 && !ball.IsMoving, "1.5 left exit stops ball");
                ball.ResetBall();
                Check(ball.ExitSide == 0, "ResetBall clears exit marker");
            }
            else
            {
                await Restart();
                Check(game.GetNode<Label>("HUD/Instructions").Text.Contains("W/S"), "Controls displayed");
                Check(game.GetNode<Label>("HUD/Message").Text.Contains(game.Mission), "Story mission displayed");
                await Press("serve", 3);
                Check(ball.IsMoving && ball.Velocity.X > 0, "Space serves to the right first");
                await Score(true);
                Check(game.ScoreLeft == 1 && game.ScoreRight == 0, "Right exit awards left player");
                Check(ball.Position == new Vector2(640, 360) && !ball.IsMoving && ball.ExitSide == 0, "Point resets ball and waits");
                await Frames(50);
                Check(game.ScoreLeft == 1, "One exit awards only one point");
                await Press("serve", 2);
                Check(ball.IsMoving && ball.Velocity.X < 0, "Next serve alternates direction");
                await Score(false);
                Check(game.ScoreLeft == 1 && game.ScoreRight == 1, "Left exit awards right player");
                Check(game.GetNode<Label>("HUD/Score").Text == "1 : 1", "HUD updates both scores");
                await Restart();
                foreach (bool forLeft in new[] { true, false })
                {
                    for (int i = 1; i <= 5; i++)
                    {
                        await Score(forLeft);
                        Check((forLeft ? game.ScoreLeft : game.ScoreRight) == i, "Score advances to " + i);
                        Check(game.GameOver == (i == 5), "Match ends exactly at target");
                    }
                    string winner = forLeft ? game.LeftName : game.RightName;
                    Check(game.GetNode<Label>("HUD/Message").Text.Contains(winner), "Correct winner displayed");
                    Check(game.GetNode<Label>("HUD/Message").Text.Contains(game.VictoryText), "Story ending displayed");
                    Vector2 leftPos = left.Position;
                    Vector2 rightPos = right.Position;
                    Input.ActionPress("p1_up");
                    Input.ActionPress("p2_down");
                    await Press("serve", 20);
                    Input.ActionRelease("p1_up");
                    Input.ActionRelease("p2_down");
                    Check(!ball.IsMoving && left.Position == leftPos && right.Position == rightPos, "Winner freezes play and blocks Space");
                    Check((forLeft ? game.ScoreLeft : game.ScoreRight) == 5, "Score cannot increase after winner");
                    await Restart();
                }
            }
            GD.Print($"SUCCESS: {checks} checks ({(stage5 ? "1.5" : "1.6")})");
            GetTree().Quit();
        }
        catch (Exception error)
        {
            GD.PushError(error.ToString());
            GetTree().Quit(1);
        }
    }
}
