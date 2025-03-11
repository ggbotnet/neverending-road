extends Node2D

onready var root = get_node(".")

func _ready():
	set_fixed_process(true)

func _fixed_process(delta):
	if not Global.gameover:
		root.set_pos(Vector2(root.get_pos().x, root.get_pos().y + Global.speed_ground))
		if root.get_global_pos().y > get_viewport_rect().size.y:
			queue_free()
