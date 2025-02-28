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
var dir: int
var speed: int
var texture_normal: Texture
var texture_damaged: Texture
onready var sprite = $Sprite

func _ready():
	randomize()
	dir = randi() % 2
	var car = CARS[dir]
	speed = car["speed"]
	texture_normal = car["texture_normal"]
	texture_damaged = car["texture_damaged"]
	position.x = car["pos"][randi() % car["pos"].size()]
	sprite.texture = texture_normal

func _physics_process(_delta: float) -> void:
	if not Global.gameover:
		position.y += speed
		if position.y > get_viewport_rect().size.y:
			queue_free()

func _on_Area2D_body_entered(body):
	if body.is_in_group("Player"):
		get_tree().call_group("Player", "Game_Over", self)
		sprite.texture = texture_damaged
