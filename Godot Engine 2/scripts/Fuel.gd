extends Node2D

var pos = [80, 113, 146, 179]
onready var root = get_node(".")

func _ready():
	set_fixed_process(true)
	root.set_global_pos(Vector2(pos[randi() % pos.size()], root.get_global_pos().y))

func _fixed_process(delta):
	if not Global.gameover:
		root.set_pos(Vector2(root.get_pos().x, root.get_pos().y + Global.speed_ground))
		if root.get_global_pos().y > get_viewport_rect().size.y:
			queue_free()

func _on_Area2D_body_enter( body ):
	if body.is_in_group("Player"):
		Global.fuel = 60
		for node in get_tree().get_nodes_in_group("Player"):
			node.PickUp_Fuel()
		queue_free()
