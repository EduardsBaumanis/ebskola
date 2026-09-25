using Godot;

public partial class Paddle : CharacterBody2D
{
    [Export] public float Speed = 420.0f;
    [Export] public string InputUp = "p1_up";
    [Export] public string InputDown = "p1_down";
    public bool IsActive { get; set; } = true;

    public override void _Ready()
    {
        GD.Print($"{Name}: ātrums {Speed}, vadība {InputUp}/{InputDown}, aktīva {IsActive}");
    }

    public override void _PhysicsProcess(double delta)
    {
        if (!IsActive)
        {
            Velocity = Vector2.Zero;
            return;
        }

        float direction = Input.GetAxis(InputUp, InputDown);
        Velocity = new Vector2(0, direction * Speed);
        MoveAndSlide();
    }
}
