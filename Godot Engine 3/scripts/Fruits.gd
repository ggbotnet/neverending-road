extends Node2D

var pos = [80, 113, 146, 179]
var pos_new: int
var fruit_graphic = [
	preload("res://graphics/fruit1.png"), 
	preload("res://graphics/fruit2.png"),
	preload("res://graphics/fruit3.png"),
	preload("res://graphics/fruit4.png"),
]
onready var sprite = $Sprite

func _ready():
	pos_new = pos[randi() % pos.size()]
	position.x = pos_new
	sprite.texture = fruit_graphic[randi() % fruit_graphic.size()]

func _physics_process(_delta: float) -> void:
	if not Global.gameover:
		position.y += Global.speed_ground
		if position.y > get_viewport_rect().size.y:
			queue_free()

func _on_Area2D_body_entered(body):
	if body.is_in_group("Player"):
		Global.score += 10
		get_tree().call_group("Player", "PickUp_Fruit", self)
		queue_free()
