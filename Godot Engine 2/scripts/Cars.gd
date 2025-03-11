extends StaticBody2D

enum { UP, DOWN }
const CARS = {
	UP: {
		"pos": [146, 179],
		"speed": 2,
		"texture_normal": preload("res://graphics/car_up.png"),
		"texture_damaged": preload("res://graphics/car_up_dmg.png")
	},
	DOWN: {
		"pos": [80, 113],
		"speed": 5,
		"texture_normal": preload("res://graphics/car_down.png"),
		"texture_damaged": preload("res://graphics/car_down_dmg.png")
	}
}
var dir
var speed
var texture_normal
var texture_damaged
onready var sprite = get_node("Sprite")
onready var root = get_node(".")

func _ready():
	set_fixed_process(true)
	randomize()
	dir = randi() % 2
	var car = CARS[dir]
	speed = car["speed"]
	texture_normal = car["texture_normal"]
	texture_damaged = car["texture_damaged"]
	root.set_global_pos(Vector2(car["pos"][randi() % car["pos"].size()], root.get_global_pos().y))
	sprite.texture = texture_normal

func _fixed_process(delta):
	if not Global.gameover:
		root.set_pos(Vector2(root.get_pos().x, root.get_pos().y + speed))
		if root.get_global_pos().y > get_viewport_rect().size.y:
			queue_free()

func _on_Area2D_body_enter( body ):
	if body.is_in_group("Player"):
		for node in get_tree().get_nodes_in_group("Player"):
			node.Game_Over()
		sprite.texture = texture_damaged
