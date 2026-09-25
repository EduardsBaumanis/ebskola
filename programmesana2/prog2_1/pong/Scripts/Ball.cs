using Godot;

public partial class Ball : CharacterBody2D
{
    [Export] public float BaseSpeed = 420.0f;
    public bool IsMoving { get; private set; } = false;
    // -1: bumba izgājusi pa kreisi; 1: pa labi; 0: nav iziešanas.
    public int ExitSide { get; private set; } = 0;

    public override void _Ready()
    {
        ResetBall();
        Serve(1); // 1.5 stundā bumba sāk kustēties pati.
    }

    public void ResetBall()
    {
        Stop();
        Position = new Vector2(640, 360);
        ExitSide = 0;
    }

    public void Serve(int horizontalDirection)
    {
        float verticalDirection = (float)GD.RandRange(0.25, 0.6);
        if (GD.Randf() < 0.5f) verticalDirection = -verticalDirection;
        Velocity = new Vector2(horizontalDirection, verticalDirection).Normalized() * BaseSpeed;
        IsMoving = true;
    }

    public void Stop()
    {
        IsMoving = false;
        Velocity = Vector2.Zero;
    }

    public override void _PhysicsProcess(double delta)
    {
        if (!IsMoving) return;

        KinematicCollision2D collision = MoveAndCollide(Velocity * (float)delta);
        if (collision != null)
            Velocity = Velocity.Bounce(collision.GetNormal());

        if (Position.X < -10)
        {
            ExitSide = -1;
            Stop();
        }
        else if (Position.X > 1290)
        {
            ExitSide = 1;
            Stop();
        }
    }
}
