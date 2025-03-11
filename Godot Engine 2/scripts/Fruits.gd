extends Node2D

var pos = [80, 113, 146, 179]
var fruit_graphic = [
	preload("res://graphics/fruit1.png"), 
	preload("res://graphics/fruit2.png"),
	preload("res://graphics/fruit3.png"),
	preload("res://graphics/fruit4.png"),
]
onready var sprite = get_node("Sprite")
onready var root = get_node(".")

func _ready():
	set_fixed_process(true)
	root.set_global_pos(Vector2(pos[randi() % pos.size()], root.get_global_pos().y))
	sprite.texture = fruit_graphic[randi() % fruit_graphic.size()]

func _fixed_process(delta):
	if not Global.gameover:
		root.set_pos(Vector2(root.get_pos().x, root.get_pos().y + Global.speed_ground))
		if root.get_global_pos().y > get_viewport_rect().size.y:
			queue_free()

func _on_Area2D_body_enter( body ):
	if body.is_in_group("Player"):
		Global.score += 10
		for node in get_tree().get_nodes_in_group("Player"):
			node.PickUp_Fruit()
		queue_free()
