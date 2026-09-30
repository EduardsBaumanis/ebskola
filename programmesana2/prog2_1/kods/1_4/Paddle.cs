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
}
