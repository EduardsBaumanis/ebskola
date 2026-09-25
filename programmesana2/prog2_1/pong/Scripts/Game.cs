using Godot;

public partial class Game : Node2D
{
    [Export] public string GameTitle = "Zvaigžņu duelis";
    [Export] public string LeftName = "Komēta";
    [Export] public string RightName = "Meteors";
    [Export] public string Mission = "Divas kosmosa komandas sacenšas par enerģijas kodolu.";
    [Export] public string VictoryText = "Enerģijas kodols ir nogādāts mājās!";
    [Export(PropertyHint.Range, "1,20,1")] public int TargetScore = 5;

    public int ScoreLeft { get; private set; } = 0;
    public int ScoreRight { get; private set; } = 0;
    public bool GameOver { get; private set; } = false;

    private Ball ball;
    private Paddle left;
    private Paddle right;
    private Label score;
    private Label message;
    private int serveDirection = 1;

    public override void _Ready()
    {
        ball = GetNode<Ball>("Ball");
        left = GetNode<Paddle>("PaddleLeft");
        right = GetNode<Paddle>("PaddleRight");
        score = GetNode<Label>("HUD/Score");
        message = GetNode<Label>("HUD/Message");
        TargetScore = Mathf.Max(1, TargetScore);
        GetNode<Label>("HUD/Instructions").Text =
            $"{GameTitle} | W/S: {LeftName} | ↑/↓: {RightName} | Space: serve | R: jauna partija";
        PrepareServe();
        message.Text = $"{Mission} Uzvara pie {TargetScore} punktiem. Nospied Space!";
        UpdateScore();
    }

    public override void _Process(double delta)
    {
        if (Input.IsActionJustPressed("restart"))
        {
            GetTree().ReloadCurrentScene();
            return;
        }
        if (GameOver) return;

        if (ball.ExitSide != 0)
        {
            AddPoint(ball.ExitSide > 0);
            return;
        }

        if (!ball.IsMoving && Input.IsActionJustPressed("serve"))
        {
            ball.Serve(serveDirection);
            message.Text = $"Pirmais līdz {TargetScore} punktiem uzvar!";
        }
    }

    private void AddPoint(bool leftScored)
    {
        if (leftScored) ScoreLeft++;
        else ScoreRight++;
        UpdateScore();

        if (ScoreLeft >= TargetScore || ScoreRight >= TargetScore)
        {
            GameOver = true;
            ball.Stop();
            left.IsActive = false;
            right.IsActive = false;
            left.Velocity = Vector2.Zero;
            right.Velocity = Vector2.Zero;
            string winner = ScoreLeft >= TargetScore ? LeftName : RightName;
            message.Text = $"Uzvar {winner}! {VictoryText} Nospied R jaunai partijai.";
        }
        else
        {
            serveDirection = -serveDirection;
            PrepareServe();
        }
    }

    private void PrepareServe()
    {
        ball.ResetBall();
        left.Position = new Vector2(60, 360);
        right.Position = new Vector2(1220, 360);
        left.Velocity = Vector2.Zero;
        right.Velocity = Vector2.Zero;
        message.Text = "Nākamā izspēle: nospied Space!";
    }

    private void UpdateScore()
    {
        score.Text = $"{ScoreLeft} : {ScoreRight}";
    }
}
