extends Node2D

func _ready():
	position.x = rand_range(48,206)
	position.y = 272

func _physics_process(delta: float) -> void:
	if not Global.gameover:
		position.y -= 120 * delta
