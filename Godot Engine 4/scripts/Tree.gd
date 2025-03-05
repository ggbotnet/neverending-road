extends Node2D

func _physics_process(_delta: float) -> void:
	if not Global.gameover:
		position.y += Global.speed_ground
		if position.y > get_viewport_rect().size.y:
			queue_free()
