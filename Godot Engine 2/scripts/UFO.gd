extends Node2D

onready var root = get_node(".")

func _ready():
	set_fixed_process(true)
	root.set_pos(Vector2(rand_range(48,206), 272))

func _fixed_process(delta):
	if not Global.gameover:
		root.set_pos(Vector2(root.get_pos().x, root.get_pos().y - 120 * delta))
