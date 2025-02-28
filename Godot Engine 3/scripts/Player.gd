extends KinematicBody2D

const pos_limit: int = 33
const max_left: int = 80
const max_right: int = 146
var car = preload("res://graphics/player.png")
var cardmg = preload("res://graphics/player_dmg.png")
onready var root = $"."
onready var sprite = $Sprite
onready var timer = $Timer
onready var effect_hit = $effect_hit
onready var animation_player = $AnimationPlayer
onready var timer_reset = $Timer_reset
onready var pickup_text = $pickuptext
onready var audio_pickup = $Audio_PickUp
onready var audio_crash = $Audio_Crash

func _ready():
	sprite.set_texture(car)
	effect_hit.hide()
	pickup_text.hide()

func _input(event: InputEvent) -> void:
	if Global.gameover:
		return
	if timer.is_stopped():
		control_movement(event)

func control_movement(event: InputEvent) -> void:
	if event.is_action_pressed("keyboard_left") and position.x > max_left:
		player_move(Vector2.LEFT)
	if event.is_action_pressed("keyboard_right") and position.x <= max_right:
		player_move(Vector2.RIGHT)

func player_move(dir: Vector2) -> void:
	var new_position = position + dir * pos_limit
	var tween = get_tree().create_tween()
	tween.tween_property(self, "position", new_position, 0.2).set_trans(Tween.TRANS_SINE)
	timer.start()

func PickUp_Fuel(_delta):
	if timer_reset.is_stopped():
		audio_pickup.play()
		pickup_text.show()
		pickup_text.text = "FUEL"
		timer_reset.start()

func PickUp_Fruit(_delta):
	if timer_reset.is_stopped():
		audio_pickup.play()
		pickup_text.show()
		pickup_text.text = "10"
		timer_reset.start()

func Game_Over(_delta):
	Global.gameover = true
	sprite.set_texture(cardmg)
	effect_hit.show()
	animation_player.play("hit")
	audio_crash.play()
	yield(get_tree().create_timer(0.4), "timeout")
	# warning-ignore:return_value_discarded
	get_tree().change_scene("res://scenes/GameOver.tscn")

func _on_Timer_reset_timeout():
	pickup_text.hide()
