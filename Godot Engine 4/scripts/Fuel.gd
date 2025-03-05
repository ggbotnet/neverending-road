extends Node2D

var pos = [80, 113, 146, 179]
var pos_new: int

func _ready():
	pos_new = pos[randi() % pos.size()]
	position.x = pos_new

func _physics_process(_delta: float) -> void:
	if not Global.gameover:
		position.y += Global.speed_ground
		if position.y > get_viewport_rect().size.y:
			queue_free()

func _on_Area2D_body_entered(body):
	if body.is_in_group("Player"):
		Global.fuel = 60
		get_tree().call_group("Player", "PickUp_Fuel", self)
		queue_free()
